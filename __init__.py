"""
Blender Terrain Generator Plugin
Generates 3D terrain using Perlin noise with customizable parameters
"""

bl_info = {
    "name": "Terrain Generator",
    "author": "QuickBoyz",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Terrain Generator",
    "description": "Generate 3D terrain using Perlin noise with customizable parameters and biome support",
    "category": "Add Mesh",
}

import bpy
from bpy.props import IntProperty, FloatProperty, EnumProperty, BoolProperty
from bpy.types import Operator, Panel, PropertyGroup
from mathutils import Vector
import random
import math


# Perlin Noise Implementation
class PerlinNoise:
    """Perlin noise generator for terrain generation"""
    
    def __init__(self, seed=0):
        self.seed = seed
        random.seed(seed)
        self.permutation = list(range(256))
        random.shuffle(self.permutation)
        self.permutation *= 2
    
    def fade(self, t):
        """Fade function for smooth interpolation"""
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    def lerp(self, t, a, b):
        """Linear interpolation"""
        return a + t * (b - a)
    
    def grad(self, hash_val, x, y):
        """Calculate gradient"""
        h = hash_val & 3
        u = x if h < 2 else y
        v = y if h < 2 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)
    
    def noise(self, x, y):
        """Generate 2D Perlin noise value"""
        # Find unit grid cell containing point
        X = int(math.floor(x)) & 255
        Y = int(math.floor(y)) & 255
        
        # Get relative xy coordinates within cell
        x -= math.floor(x)
        y -= math.floor(y)
        
        # Compute fade curves
        u = self.fade(x)
        v = self.fade(y)
        
        # Hash coordinates of the 4 cube corners
        A = self.permutation[X] + Y
        AA = self.permutation[A]
        AB = self.permutation[A + 1]
        B = self.permutation[X + 1] + Y
        BA = self.permutation[B]
        BB = self.permutation[B + 1]
        
        # Blend results from corners
        return self.lerp(v,
            self.lerp(u, self.grad(self.permutation[AA], x, y),
                         self.grad(self.permutation[BA], x - 1, y)),
            self.lerp(u, self.grad(self.permutation[AB], x, y - 1),
                         self.grad(self.permutation[BB], x - 1, y - 1))
        )
    
    def octave_noise(self, x, y, octaves=1, persistence=0.5, lacunarity=2.0):
        """Generate multi-octave Perlin noise"""
        total = 0
        frequency = 1
        amplitude = 1
        max_value = 0
        
        for _ in range(octaves):
            total += self.noise(x * frequency, y * frequency) * amplitude
            max_value += amplitude
            amplitude *= persistence
            frequency *= lacunarity
        
        return total / max_value


# Biome System
class Biome:
    """Base class for terrain biomes"""
    
    def __init__(self, name):
        self.name = name
    
    def modify_height(self, height, x, y):
        """Modify height value based on biome characteristics"""
        return height
    
    def get_material_color(self):
        """Get material color for the biome"""
        return (0.3, 0.5, 0.2, 1.0)  # Default green


class DefaultBiome(Biome):
    """Default terrain biome"""
    
    def __init__(self):
        super().__init__("Default")
    
    def get_material_color(self):
        return (0.3, 0.5, 0.2, 1.0)  # Green


class ForestBiome(Biome):
    """Forest biome with elevated features"""
    
    def __init__(self):
        super().__init__("Forest")
    
    def modify_height(self, height, x, y):
        # Add slight variation for forest floor
        return height * 1.1
    
    def get_material_color(self):
        return (0.2, 0.4, 0.15, 1.0)  # Dark green


class BeachBiome(Biome):
    """Beach biome with flatter terrain"""
    
    def __init__(self):
        super().__init__("Beach")
    
    def modify_height(self, height, x, y):
        # Flatten the terrain for beach
        return height * 0.3
    
    def get_material_color(self):
        return (0.76, 0.70, 0.50, 1.0)  # Sandy color


class SavannaBiome(Biome):
    """Savanna biome with gentle rolling hills"""
    
    def __init__(self):
        super().__init__("Savanna")
    
    def modify_height(self, height, x, y):
        # Gentle rolling hills
        return height * 0.7
    
    def get_material_color(self):
        return (0.73, 0.67, 0.42, 1.0)  # Dry grass color


# Biome Registry
BIOME_REGISTRY = {
    'DEFAULT': DefaultBiome(),
    'FOREST': ForestBiome(),
    'BEACH': BeachBiome(),
    'SAVANNA': SavannaBiome(),
}


# Property Group for Terrain Parameters
class TerrainGeneratorProperties(PropertyGroup):
    """Properties for terrain generation"""
    
    size_x: IntProperty(
        name="Size X",
        description="Terrain size in X direction",
        default=50,
        min=2,
        max=500
    )
    
    size_y: IntProperty(
        name="Size Y",
        description="Terrain size in Y direction",
        default=50,
        min=2,
        max=500
    )
    
    height_amplitude: FloatProperty(
        name="Height Amplitude",
        description="Maximum height of the terrain",
        default=5.0,
        min=0.1,
        max=100.0
    )
    
    noise_scale: FloatProperty(
        name="Noise Scale",
        description="Scale of the noise pattern (smaller = more detailed)",
        default=10.0,
        min=0.1,
        max=100.0
    )
    
    octaves: IntProperty(
        name="Octaves",
        description="Number of noise layers (more = more detail)",
        default=4,
        min=1,
        max=8
    )
    
    persistence: FloatProperty(
        name="Persistence",
        description="Amplitude multiplier for each octave (affects roughness)",
        default=0.5,
        min=0.0,
        max=1.0
    )
    
    lacunarity: FloatProperty(
        name="Lacunarity",
        description="Frequency multiplier for each octave",
        default=2.0,
        min=1.0,
        max=4.0
    )
    
    seed: IntProperty(
        name="Seed",
        description="Random seed for terrain generation",
        default=0,
        min=0,
        max=999999
    )
    
    biome: EnumProperty(
        name="Biome",
        description="Terrain biome type",
        items=[
            ('DEFAULT', "Default", "Standard terrain"),
            ('FOREST', "Forest", "Dense forest terrain with elevated features"),
            ('BEACH', "Beach", "Flat sandy beach terrain"),
            ('SAVANNA', "Savanna", "Gentle rolling savanna hills"),
        ],
        default='DEFAULT'
    )
    
    apply_material: BoolProperty(
        name="Apply Material",
        description="Apply biome-specific material to terrain",
        default=True
    )


# Terrain Generation Operator
class TERRAIN_OT_generate(Operator):
    """Generate terrain mesh using Perlin noise"""
    bl_idname = "terrain.generate"
    bl_label = "Generate Terrain"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.terrain_generator
        
        # Get biome
        biome = BIOME_REGISTRY[props.biome]
        
        # Initialize Perlin noise generator
        noise_gen = PerlinNoise(seed=props.seed)
        
        # Create mesh
        mesh = bpy.data.meshes.new("Terrain")
        obj = bpy.data.objects.new("Terrain", mesh)
        context.collection.objects.link(obj)
        
        # Generate vertices
        vertices = []
        faces = []
        
        size_x = props.size_x
        size_y = props.size_y
        
        # Generate heightmap and vertices
        for y in range(size_y):
            for x in range(size_x):
                # Calculate noise coordinates
                nx = x / props.noise_scale
                ny = y / props.noise_scale
                
                # Get noise value
                height = noise_gen.octave_noise(
                    nx, ny,
                    octaves=props.octaves,
                    persistence=props.persistence,
                    lacunarity=props.lacunarity
                )
                
                # Apply biome modification
                height = biome.modify_height(height, x, y)
                
                # Scale by amplitude
                height *= props.height_amplitude
                
                # Create vertex
                vertices.append(Vector((x, y, height)))
        
        # Generate faces (quads)
        for y in range(size_y - 1):
            for x in range(size_x - 1):
                v1 = y * size_x + x
                v2 = v1 + 1
                v3 = v1 + size_x + 1
                v4 = v1 + size_x
                faces.append((v1, v2, v3, v4))
        
        # Create mesh
        mesh.from_pydata(vertices, [], faces)
        mesh.update()
        
        # Center terrain
        obj.location = (-size_x / 2, -size_y / 2, 0)
        
        # Apply material if requested
        if props.apply_material:
            self.apply_biome_material(obj, biome)
        
        # Select the new object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        context.view_layer.objects.active = obj
        
        self.report({'INFO'}, f"Terrain generated: {size_x}x{size_y} vertices, Biome: {biome.name}")
        
        return {'FINISHED'}
    
    def apply_biome_material(self, obj, biome):
        """Apply material to the terrain based on biome"""
        mat_name = f"Terrain_{biome.name}_Material"
        
        # Check if material exists, otherwise create it
        if mat_name in bpy.data.materials:
            mat = bpy.data.materials[mat_name]
        else:
            mat = bpy.data.materials.new(name=mat_name)
            mat.use_nodes = True
            nodes = mat.node_tree.nodes
            nodes.clear()
            
            # Create shader nodes
            node_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
            node_output = nodes.new(type='ShaderNodeOutputMaterial')
            
            # Set color
            color = biome.get_material_color()
            node_bsdf.inputs['Base Color'].default_value = color
            node_bsdf.inputs['Roughness'].default_value = 0.8
            
            # Link nodes
            links = mat.node_tree.links
            links.new(node_bsdf.outputs['BSDF'], node_output.inputs['Surface'])
        
        # Assign material to object
        if obj.data.materials:
            obj.data.materials[0] = mat
        else:
            obj.data.materials.append(mat)


# UI Panel
class TERRAIN_PT_main_panel(Panel):
    """Terrain Generator Panel"""
    bl_label = "Terrain Generator"
    bl_idname = "TERRAIN_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Terrain'
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.terrain_generator
        
        # Terrain Size
        box = layout.box()
        box.label(text="Terrain Size:", icon='MESH_GRID')
        box.prop(props, "size_x")
        box.prop(props, "size_y")
        
        # Height Settings
        box = layout.box()
        box.label(text="Height Settings:", icon='EMPTY_SINGLE_ARROW')
        box.prop(props, "height_amplitude")
        
        # Noise Settings
        box = layout.box()
        box.label(text="Noise Settings:", icon='FORCE_TURBULENCE')
        box.prop(props, "noise_scale")
        box.prop(props, "octaves")
        box.prop(props, "persistence")
        box.prop(props, "lacunarity")
        box.prop(props, "seed")
        
        # Biome Selection
        box = layout.box()
        box.label(text="Biome:", icon='WORLD')
        box.prop(props, "biome", text="")
        box.prop(props, "apply_material")
        
        # Generate Button
        layout.separator()
        layout.operator("terrain.generate", text="Generate Terrain", icon='LANDSCAPE')


# Registration
classes = (
    TerrainGeneratorProperties,
    TERRAIN_OT_generate,
    TERRAIN_PT_main_panel,
)


def register():
    """Register plugin classes"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.terrain_generator = bpy.props.PointerProperty(type=TerrainGeneratorProperties)


def unregister():
    """Unregister plugin classes"""
    del bpy.types.Scene.terrain_generator
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

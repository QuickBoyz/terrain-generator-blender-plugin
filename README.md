# Terrain Generator - Blender Plugin

A powerful Blender plugin for generating 3D terrain using Perlin noise with customizable parameters and multiple biome support.

## Features

- **Perlin Noise Generation**: High-quality procedural terrain generation using multi-octave Perlin noise
- **Customizable Parameters**:
  - Terrain size (X and Y dimensions)
  - Height amplitude control
  - Noise scale/detail factor
  - Random seed for reproducible results
  - Octaves for detail levels
  - Persistence for roughness control
  - Lacunarity for frequency control
- **Multiple Biomes**:
  - Default terrain
  - Forest (elevated features with dark green)
  - Beach (flat sandy terrain)
  - Savanna (gentle rolling hills)
- **Automatic Materials**: Biome-specific material application
- **Easy to Extend**: Modular biome system for adding new terrain types

## Installation

1. Download the `__init__.py` file from this repository
2. Open Blender (version 3.0 or higher)
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` button
5. Navigate to the downloaded `__init__.py` file and select it
6. Enable the plugin by checking the box next to "Add Mesh: Terrain Generator"

## Usage

1. Open Blender and switch to any 3D Viewport
2. Press `N` to open the sidebar if it's not visible
3. Click on the `Terrain` tab in the sidebar
4. Configure your terrain parameters:
   - **Size X/Y**: Set the dimensions of your terrain grid
   - **Height Amplitude**: Control the maximum height of the terrain
   - **Noise Scale**: Adjust the scale of noise pattern (smaller = more detailed)
   - **Octaves**: Add more detail layers (higher = more detailed)
   - **Persistence**: Control roughness (0.0 = smooth, 1.0 = rough)
   - **Lacunarity**: Control frequency increase between octaves
   - **Seed**: Set a random seed for reproducible results
   - **Biome**: Choose from Default, Forest, Beach, or Savanna
   - **Apply Material**: Toggle automatic material application
5. Click `Generate Terrain` button

## Parameter Guide

### Terrain Size
- **Size X/Y**: Number of vertices in each direction (2-500)
- Higher values create more detailed terrain but take longer to generate

### Height Settings
- **Height Amplitude**: Maximum height deviation (0.1-100.0)
- Controls how tall your mountains and deep your valleys are

### Noise Settings
- **Noise Scale**: (0.1-100.0)
  - Lower values = zoomed in, more detailed features
  - Higher values = zoomed out, larger features
- **Octaves**: (1-8)
  - Number of noise layers combined together
  - More octaves = more detail but longer generation time
- **Persistence**: (0.0-1.0)
  - Controls amplitude of each octave
  - Lower = smoother terrain, Higher = rougher terrain
- **Lacunarity**: (1.0-4.0)
  - Controls frequency increase between octaves
  - Higher = more varied detail levels
- **Seed**: (0-999999)
  - Random seed for reproducible terrains
  - Same seed with same parameters = identical terrain

### Biomes
- **Default**: Standard green terrain with natural features
- **Forest**: Slightly elevated terrain with dark green coloring
- **Beach**: Flattened terrain with sandy color
- **Savanna**: Gentle rolling hills with dry grass color

## Extending the Plugin

The plugin is designed to be easily extensible. To add a new biome:

1. Create a new biome class inheriting from `Biome`:
```python
class MountainBiome(Biome):
    def __init__(self):
        super().__init__("Mountain")
    
    def modify_height(self, height, x, y):
        # Amplify heights for dramatic mountains
        return height * 1.5
    
    def get_material_color(self):
        return (0.5, 0.5, 0.5, 1.0)  # Gray rocky color
```

2. Register the biome in `BIOME_REGISTRY`:
```python
BIOME_REGISTRY = {
    'DEFAULT': DefaultBiome(),
    'FOREST': ForestBiome(),
    'BEACH': BeachBiome(),
    'SAVANNA': SavannaBiome(),
    'MOUNTAIN': MountainBiome(),  # Add new biome
}
```

3. Add the biome to the enum property:
```python
biome: EnumProperty(
    name="Biome",
    description="Terrain biome type",
    items=[
        ('DEFAULT', "Default", "Standard terrain"),
        ('FOREST', "Forest", "Dense forest terrain"),
        ('BEACH', "Beach", "Flat sandy beach"),
        ('SAVANNA', "Savanna", "Gentle rolling hills"),
        ('MOUNTAIN', "Mountain", "Dramatic mountain terrain"),  # Add here
    ],
    default='DEFAULT'
)
```

## Technical Details

- **Noise Algorithm**: Multi-octave Perlin noise implementation
- **Mesh Type**: Quad-based mesh for smooth terrain
- **Material System**: Principled BSDF shader nodes
- **Blender API**: Compatible with Blender 3.0+

## Tips

- Start with smaller terrain sizes (50x50) for quick previews
- Use higher octaves (6-8) for realistic natural terrain
- Adjust persistence to control terrain roughness (0.5 is a good default)
- Use different seeds to explore terrain variations
- Combine with Blender's modifiers (Subdivision Surface, Displace) for extra detail

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for:
- New biome types
- Additional noise algorithms
- Performance improvements
- Bug fixes
- Documentation improvements

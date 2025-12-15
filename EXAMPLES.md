# Terrain Generator - Usage Examples

This document provides practical examples for using the Terrain Generator plugin.

## Basic Examples

### 1. Simple Rolling Hills
Perfect for beginners - creates gentle, natural-looking terrain.

```
Size X: 50
Size Y: 50
Height Amplitude: 3.0
Noise Scale: 15.0
Octaves: 3
Persistence: 0.5
Lacunarity: 2.0
Seed: 12345
Biome: Default
```

### 2. Dramatic Mountain Range
Creates tall, jagged mountains with lots of detail.

```
Size X: 100
Size Y: 100
Height Amplitude: 15.0
Noise Scale: 20.0
Octaves: 6
Persistence: 0.6
Lacunarity: 2.5
Seed: 98765
Biome: Default
```

### 3. Smooth Desert Dunes
Large, smooth undulations perfect for desert landscapes.

```
Size X: 80
Size Y: 80
Height Amplitude: 5.0
Noise Scale: 30.0
Octaves: 2
Persistence: 0.3
Lacunarity: 1.5
Seed: 54321
Biome: Savanna
```

### 4. Detailed Rocky Terrain
Lots of small details and rough surfaces.

```
Size X: 60
Size Y: 60
Height Amplitude: 8.0
Noise Scale: 8.0
Octaves: 7
Persistence: 0.7
Lacunarity: 2.8
Seed: 11111
Biome: Default
```

## Biome-Specific Examples

### Forest Terrain
```
Size X: 70
Size Y: 70
Height Amplitude: 6.0
Noise Scale: 12.0
Octaves: 4
Persistence: 0.5
Lacunarity: 2.0
Seed: 22222
Biome: Forest
Apply Material: Yes
```

### Beach Coastline
```
Size X: 100
Size Y: 50
Height Amplitude: 2.0
Noise Scale: 25.0
Octaves: 2
Persistence: 0.4
Lacunarity: 1.8
Seed: 33333
Biome: Beach
Apply Material: Yes
```

### Savanna Plains
```
Size X: 120
Size Y: 120
Height Amplitude: 4.0
Noise Scale: 35.0
Octaves: 3
Persistence: 0.45
Lacunarity: 2.0
Seed: 44444
Biome: Savanna
Apply Material: Yes
```

## Advanced Techniques

### Creating Varied Landscapes
Generate multiple terrains with different biomes and arrange them:

1. Generate a beach terrain (flat, low amplitude)
2. Move it to one side
3. Generate a forest terrain (medium amplitude)
4. Position it next to the beach
5. Generate a mountain range (high amplitude)
6. Place it at the back

### Fine-tuning Parameters

**For more detail:**
- Increase Octaves (5-8)
- Decrease Noise Scale (5-10)

**For smoother terrain:**
- Decrease Octaves (1-3)
- Decrease Persistence (0.2-0.4)
- Increase Noise Scale (20-50)

**For rougher terrain:**
- Increase Persistence (0.6-0.8)
- Increase Lacunarity (2.5-4.0)
- Increase Octaves (5-8)

**For larger features:**
- Increase Noise Scale (30-100)

**For smaller features:**
- Decrease Noise Scale (5-15)

### Performance Considerations

- Small terrain (50x50): Fast generation, good for testing
- Medium terrain (100x100): Balanced detail and performance
- Large terrain (200x200+): High detail, slower generation

Start with smaller sizes to find the right parameters, then scale up.

## Workflow Tips

1. **Start Simple**: Begin with default parameters and adjust one at a time
2. **Use Seeds**: Once you find a terrain you like, note the seed for reproducibility
3. **Layer Terrains**: Generate multiple terrains with different parameters and combine them
4. **Post-Processing**: Use Blender's modifiers:
   - Subdivision Surface for smoother appearance
   - Displacement modifier with textures for extra detail
   - Decimate for reducing poly count
5. **Materials**: Disable auto-material if you want to apply your own custom materials

## Common Parameter Combinations

### Natural Landscape
- Octaves: 4-5
- Persistence: 0.5-0.6
- Lacunarity: 2.0-2.2
- Noise Scale: 10-20

### Alien Landscape
- Octaves: 6-8
- Persistence: 0.7-0.8
- Lacunarity: 3.0-4.0
- Noise Scale: 5-15

### Gentle Hills
- Octaves: 2-3
- Persistence: 0.3-0.4
- Lacunarity: 1.5-2.0
- Noise Scale: 25-40

### Sharp Mountains
- Octaves: 6-7
- Persistence: 0.6-0.7
- Lacunarity: 2.5-3.0
- Noise Scale: 15-25

## Troubleshooting

**Terrain is too flat:**
- Increase Height Amplitude
- Increase Persistence
- Decrease Noise Scale

**Terrain is too spiky:**
- Decrease Height Amplitude
- Decrease Persistence
- Increase Noise Scale

**Not enough detail:**
- Increase Octaves
- Decrease Noise Scale

**Too noisy/chaotic:**
- Decrease Octaves
- Increase Noise Scale
- Decrease Persistence

**Generation is slow:**
- Decrease Size X/Y
- Decrease Octaves

## Experimental Settings

Try these unusual combinations for unique results:

### "Crystalline"
```
Octaves: 8, Persistence: 0.9, Lacunarity: 3.5, Noise Scale: 6.0
```

### "Flowing"
```
Octaves: 2, Persistence: 0.3, Lacunarity: 1.3, Noise Scale: 40.0
```

### "Fractal"
```
Octaves: 7, Persistence: 0.8, Lacunarity: 3.8, Noise Scale: 8.0
```

## Best Practices

1. Always test with smaller terrain sizes first
2. Document seed values for terrains you want to recreate
3. Use consistent biomes for connected terrain pieces
4. Combine with Blender's other tools for maximum effect
5. Experiment with different random seeds - each one is unique!

Happy terrain generating!

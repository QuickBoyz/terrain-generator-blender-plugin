# Quick Start Guide

Get up and running with the Terrain Generator in 5 minutes!

## Installation (2 minutes)

1. **Download** the `__init__.py` file
2. **Open Blender** (version 3.0 or higher)
3. Go to **Edit → Preferences → Add-ons**
4. Click **Install...** button
5. Select the `__init__.py` file
6. **Enable** the checkbox next to "Add Mesh: Terrain Generator"

✅ Installation complete!

## Your First Terrain (1 minute)

1. In Blender's 3D Viewport, press **N** to show the sidebar
2. Click the **Terrain** tab
3. Click **Generate Terrain** button

🎉 You've created your first terrain!

## Customizing Your Terrain (2 minutes)

Try these quick modifications:

### Make it Bigger
```
Size X: 100
Size Y: 100
```

### Make it Taller
```
Height Amplitude: 10.0
```

### Add More Detail
```
Octaves: 6
```

### Change the Look
```
Biome: Forest (or Beach, Savanna)
```

### Get Different Terrain
```
Seed: 12345 (try any number!)
```

## Next Steps

### Experiment with Parameters
- Try different **Seeds** to explore variations
- Adjust **Noise Scale** to change feature size
- Modify **Persistence** for roughness control

### Learn More
- Read the [README.md](README.md) for detailed parameter explanations
- Check [EXAMPLES.md](EXAMPLES.md) for specific use cases
- Review [FEATURES.md](FEATURES.md) for complete feature list

### Advanced Usage
- Combine multiple terrains with different biomes
- Use Blender's modifiers for extra detail (Subdivision Surface, Displace)
- Apply custom materials and textures
- Export for use in games or other applications

## Common Tasks

### Create a Mountain Range
```
Size: 100x100
Height Amplitude: 20.0
Noise Scale: 15.0
Octaves: 6
Persistence: 0.7
Seed: 98765
```

### Create Rolling Hills
```
Size: 80x80
Height Amplitude: 5.0
Noise Scale: 30.0
Octaves: 3
Persistence: 0.4
Seed: 54321
```

### Create a Beach
```
Size: 100x50
Height Amplitude: 2.0
Noise Scale: 25.0
Octaves: 2
Biome: Beach
Seed: 33333
```

## Tips

💡 **Start Small**: Test with 50x50 terrain first, then increase size  
💡 **Use Seeds**: Save seed numbers for terrains you like  
💡 **Layer Terrains**: Create multiple terrains with different settings  
💡 **Iterate**: Adjust one parameter at a time to learn its effect  

## Troubleshooting

**Terrain is too flat?**
→ Increase Height Amplitude

**Terrain is too spiky?**
→ Decrease Persistence or increase Noise Scale

**Need more detail?**
→ Increase Octaves

**Generation is slow?**
→ Decrease Size X/Y or Octaves

## Resources

- Full Documentation: [README.md](README.md)
- Usage Examples: [EXAMPLES.md](EXAMPLES.md)
- Feature Overview: [FEATURES.md](FEATURES.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

## Need Help?

- Check the documentation files
- Open an issue on GitHub
- Review the code examples

Happy terrain generating! 🏔️🌲🏖️

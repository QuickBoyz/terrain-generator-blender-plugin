# Contributing to Terrain Generator

Thank you for your interest in contributing to the Terrain Generator Blender Plugin! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers and help them get started
- Focus on what's best for the community
- Show empathy towards other contributors

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- Blender version
- Plugin version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots if applicable
- Any error messages from Blender's console

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- Clear description of the feature
- Why it would be useful
- Example use cases
- Mockups or examples if applicable

### Pull Requests

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and relatively small
- Comment complex algorithms

### Adding a New Biome

To add a new biome, follow these steps:

1. **Create the Biome Class**:
```python
class YourBiome(Biome):
    def __init__(self):
        super().__init__("YourBiomeName")
    
    def modify_height(self, height, x, y):
        # Your height modification logic
        return height * modifier
    
    def get_material_color(self):
        # Return RGBA tuple
        return (r, g, b, 1.0)
```

2. **Register in BIOME_REGISTRY**:
```python
BIOME_REGISTRY = {
    'DEFAULT': DefaultBiome(),
    'YOUR_BIOME': YourBiome(),
}
```

3. **Add to UI Enum**:
```python
biome: EnumProperty(
    items=[
        ('YOUR_BIOME', "Your Biome", "Description"),
    ]
)
```

### Adding New Parameters

1. Add property to `TerrainGeneratorProperties` class
2. Use in `TERRAIN_OT_generate.execute()` method
3. Add UI element in `TERRAIN_PT_main_panel.draw()` method
4. Document in README.md and EXAMPLES.md

### Testing

- Test with multiple Blender versions if possible
- Test all parameter combinations
- Verify materials apply correctly
- Check performance with large terrain sizes
- Ensure no console errors or warnings

### Documentation

When adding features:
- Update README.md with new functionality
- Add examples to EXAMPLES.md if applicable
- Update CHANGELOG.md
- Add inline code comments for complex logic

## Project Structure

```
terrain-generator-blender-plugin/
├── __init__.py           # Main plugin file
├── test_perlin_noise.py  # Test suite
├── README.md             # User documentation
├── EXAMPLES.md           # Usage examples
├── CONTRIBUTING.md       # This file
├── CHANGELOG.md          # Version history
├── LICENSE               # License file
└── .gitignore           # Git ignore rules
```

## Architecture Overview

### Main Components

1. **PerlinNoise Class**: Generates 2D Perlin noise
2. **Biome Classes**: Define terrain characteristics and materials
3. **TerrainGeneratorProperties**: Blender property group for parameters
4. **TERRAIN_OT_generate**: Operator that generates the mesh
5. **TERRAIN_PT_main_panel**: UI panel in sidebar

### Data Flow

1. User sets parameters in UI panel
2. User clicks "Generate Terrain"
3. Operator reads properties
4. PerlinNoise generates heightmap
5. Biome modifies height values
6. Mesh is created from heightmap
7. Material is applied
8. Mesh is added to scene

## Feature Ideas

Here are some ideas for future contributions:

### New Biomes
- Mountain (sharp peaks, high amplitude)
- Desert (smooth dunes with specific pattern)
- Tundra (frozen, minimal variation)
- Volcanic (sharp features with crater-like formations)
- Canyon (erosion patterns, layered appearance)

### New Features
- **Erosion Simulation**: Add thermal and hydraulic erosion
- **Water Level**: Generate water plane at specified height
- **Multi-biome Blending**: Smooth transitions between biomes
- **Vegetation System**: Procedural tree/grass placement
- **Texture Baking**: Bake procedural textures to terrain
- **LOD System**: Multiple detail levels for performance
- **Preset System**: Save/load terrain configurations
- **Animation**: Animated terrain morphing
- **Export Options**: Export heightmaps as images
- **Alternative Noise**: Simplex, Worley, Voronoi noise types

### Improvements
- GPU acceleration for large terrains
- Undo/Redo support improvements
- Progress bar for long operations
- Preview mode (low-res quick preview)
- Batch generation of terrain tiles
- Custom material system
- Terrain sculpting tools integration

## Questions or Help

If you have questions or need help:
- Open an issue with the "question" label
- Check existing documentation
- Look at code examples in EXAMPLES.md

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

## Recognition

All contributors will be recognized in the project. Significant contributions may be highlighted in release notes.

Thank you for contributing to Terrain Generator! 🎉

# Changelog

All notable changes to the Terrain Generator Blender Plugin will be documented in this file.

## [1.0.0] - 2025-12-15

### Added
- Initial release of Terrain Generator plugin for Blender
- Perlin noise-based terrain generation with multi-octave support
- Customizable parameters:
  - Terrain size (X and Y dimensions, 2-500 vertices)
  - Height amplitude (0.1-100.0 units)
  - Noise scale for detail control (0.1-100.0)
  - Octaves for layer detail (1-8)
  - Persistence for roughness control (0.0-1.0)
  - Lacunarity for frequency control (1.0-4.0)
  - Random seed for reproducibility (0-999999)
- Biome system with four built-in biomes:
  - Default: Standard green terrain
  - Forest: Elevated features with dark green color
  - Beach: Flat sandy terrain with beige color
  - Savanna: Gentle rolling hills with dry grass color
- Automatic material generation and application
- UI panel in Blender's 3D View sidebar (Terrain tab)
- Quad-based mesh generation for smooth terrain
- Comprehensive documentation:
  - README with installation and usage instructions
  - EXAMPLES with practical usage scenarios
  - Extension guide for adding custom biomes
- Standalone test suite for Perlin noise validation

### Technical Details
- Compatible with Blender 3.0+
- Pure Python implementation
- No external dependencies beyond Blender's API
- Extensible architecture for future enhancements

### Future Enhancements (Planned)
- Additional biomes (Mountain, Desert, Tundra, Volcanic)
- Erosion simulation
- Water level control
- Vegetation placement system
- Multiple noise algorithms (Simplex, Worley)
- Terrain texture baking
- Performance optimizations for large terrains
- Export/import terrain presets

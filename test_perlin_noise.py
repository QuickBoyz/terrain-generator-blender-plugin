#!/usr/bin/env python3
"""
Test script for Perlin noise generation
This tests the core noise functionality without requiring Blender
"""

import random
import math


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


def test_perlin_noise():
    """Test Perlin noise generation"""
    print("Testing Perlin Noise Generator...")
    
    # Test 1: Basic noise generation
    print("\n1. Testing basic noise generation...")
    noise_gen = PerlinNoise(seed=42)
    value = noise_gen.noise(1.5, 2.5)
    assert -1.0 <= value <= 1.0, "Noise value should be between -1 and 1"
    print(f"   ✓ Basic noise value: {value:.4f}")
    
    # Test 2: Deterministic behavior with same seed
    print("\n2. Testing deterministic behavior...")
    noise_gen1 = PerlinNoise(seed=123)
    noise_gen2 = PerlinNoise(seed=123)
    val1 = noise_gen1.noise(3.14, 2.71)
    val2 = noise_gen2.noise(3.14, 2.71)
    assert val1 == val2, "Same seed should produce same values"
    print(f"   ✓ Both generators produced: {val1:.4f}")
    
    # Test 3: Different seeds produce different values
    print("\n3. Testing different seeds...")
    noise_gen3 = PerlinNoise(seed=456)
    val3 = noise_gen3.noise(3.14, 2.71)
    assert val1 != val3, "Different seeds should produce different values"
    print(f"   ✓ Seed 123: {val1:.4f}, Seed 456: {val3:.4f}")
    
    # Test 4: Octave noise
    print("\n4. Testing octave noise...")
    noise_gen = PerlinNoise(seed=0)
    octave_val = noise_gen.octave_noise(1.0, 1.0, octaves=4, persistence=0.5, lacunarity=2.0)
    assert -1.0 <= octave_val <= 1.0, "Octave noise should be normalized"
    print(f"   ✓ Octave noise value: {octave_val:.4f}")
    
    # Test 5: Generate small heightmap
    print("\n5. Testing heightmap generation (10x10)...")
    noise_gen = PerlinNoise(seed=12345)
    heightmap = []
    for y in range(10):
        row = []
        for x in range(10):
            height = noise_gen.octave_noise(
                x / 10.0, y / 10.0,
                octaves=3,
                persistence=0.5,
                lacunarity=2.0
            )
            row.append(height)
        heightmap.append(row)
    
    # Check heightmap properties
    min_height = min(min(row) for row in heightmap)
    max_height = max(max(row) for row in heightmap)
    avg_height = sum(sum(row) for row in heightmap) / (10 * 10)
    
    print(f"   ✓ Heightmap generated successfully")
    print(f"     Min height: {min_height:.4f}")
    print(f"     Max height: {max_height:.4f}")
    print(f"     Avg height: {avg_height:.4f}")
    
    # Test 6: Visualize small terrain (ASCII art)
    print("\n6. Visualizing 20x20 terrain (ASCII art)...")
    noise_gen = PerlinNoise(seed=999)
    chars = " .:-=+*#%@"
    for y in range(20):
        line = ""
        for x in range(20):
            height = noise_gen.octave_noise(
                x / 5.0, y / 5.0,
                octaves=4,
                persistence=0.5,
                lacunarity=2.0
            )
            # Map -1 to 1 range to 0 to 9
            idx = int((height + 1) / 2 * 9)
            idx = max(0, min(9, idx))
            line += chars[idx]
        print(f"   {line}")
    
    print("\n" + "="*50)
    print("All tests passed! ✓")
    print("="*50)


if __name__ == "__main__":
    test_perlin_noise()

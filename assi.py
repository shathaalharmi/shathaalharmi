total_width = 100
tile_width = 5
tiles = total_width // tile_width
if tiles % 2 == 0:
    tiles = tiles - 1
used_width = tiles * tile_width
gap = total_width - used_width
gap_each_side = gap / 2
print("number of tiles:", tiles)
print("gap on each side:", gap_each_side)
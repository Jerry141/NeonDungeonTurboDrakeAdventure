from typing import Text, Tuple

import numpy as np # type: ignore


# Tile graphics structured type compatibile with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint
        ("fg", "3B"), # 3 unsigned bytes, for RGP colors, foreground
        ("bg", "3B"), # background (similar to foreground)
    ]
)

# Tile structure for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool), # True if tile can be walked over
        ("transparent", np.bool), # True if tile doesn't block FOV
        ("dark", graphic_dt), # Graphics for when this tile is not in FOV
        ("light", graphic_dt), # Graphics for when this tile is in FOV
    ]
)


def new_tile(
    *, # enforce the use of keywords - order of parameters is not important
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    # Helper func for defining individual tile types
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord("`"), (69, 95, 101), (44, 4, 82)), dtype=graphic_dt)


floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("."), (255, 255, 255), (255,41,117)),
    light=(ord("."), (255, 255, 255), (140,30,255)),
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("#"), (255,211,25), (255,144,31)),
    light=(ord("#"), (255,144,31), (255,211,25)),
)

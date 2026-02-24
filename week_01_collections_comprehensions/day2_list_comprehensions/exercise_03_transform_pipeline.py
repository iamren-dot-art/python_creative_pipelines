# Render output paths need to be generated from scene data
project_name = "hero_spot"
render_layers = ["beauty", "diffuse", "specular", "shadow", "ao"]
frame_range = list(range(1, 25))  # Frames 1-24

# 1. Generate output folder names from render layers:
#    ["output/hero_spot_beauty", "output/hero_spot_diffuse", ...]
folders = [f"output/{project_name}_{layer}" for layer in render_layers]
print("--- Render layer output folders ---")
print(folders)

# 2. Generate filenames for frame 1 of each layer:
#    ["hero_spot_beauty.0001.exr", "hero_spot_diffuse.0001.exr", ...]
#    Hint: use :04d for 4-digit frame padding
fr1_files = [f"output/{project_name}_{layer}.0001.exr" for layer in render_layers]
print("\n--- Frame 1 filenames ---")
print(fr1_files)

# 3. Generate ALL filenames for the "beauty" layer across all frames:
#    ["hero_spot_beauty.0001.exr", "hero_spot_beauty.0002.exr", ... ]
beauty_files = [
    f"output/{project_name}_beauty.{frame:04d}.exr" for frame in frame_range
]
print("\n--- All beauty layers ---")
print(beauty_files)

# 4. Generate a flat list of ALL filenames for ALL layers across ALL frames
#    This requires a nested comprehension:
#    [expression for layer in layers for frame in frames]
#    How many total files should there be?
all_files = [
    f"{project_name}_{layer}.{frame:04d}.exr"
    for layer in render_layers
    for frame in frame_range
]
print("\n--- All Layers ---")
print(all_files)

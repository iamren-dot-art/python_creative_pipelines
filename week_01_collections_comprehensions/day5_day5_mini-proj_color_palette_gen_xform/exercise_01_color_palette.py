# Color palette — each color is a dict with name and RGB values
palette = [
    {"name": "midnight", "rgb": [15, 10, 40]},
    {"name": "ocean", "rgb": [0, 105, 148]},
    {"name": "coral", "rgb": [255, 127, 80]},
    {"name": "sand", "rgb": [194, 178, 128]},
    {"name": "cloud", "rgb": [236, 240, 241]},
]

# 1. Extract just the color names into a list
#    ["midnight", "ocean", "coral", "sand", "cloud"]
just_names = list(c["name"] for c in palette)
print(f"[ --- Color Names --- ]\n{just_names}\n")

# 2. Build a lookup dict: name -> rgb
#    {"midnight": [15, 10, 40], "ocean": [0, 105, 148], ...}
lookup = {c["name"]: c["rgb"] for c in palette}
print(f"[ --- Name -> RGB --- ]\n{lookup}\n")

# 3. Extract just the red channel (index 0) from each color
#    [15, 0, 255, 194, 236]
red_ch = [r["rgb"][0] for r in palette]
print(f"[ --- Red Channels --- ]\n{red_ch}\n")

# 4. Find the brightest color by averaging each color's RGB values
#    Build a dict of name -> average brightness (R+G+B / 3)
#    Then print the name with the highest average
#    Hint: max() can take a key= argument
avg_col = {c["name"]: round(sum(c["rgb"]) / 3, 2) for c in palette}
# print(avg_col)
print(f"[ --- Brightest Color --- ]\n{max(avg_col, key=avg_col.get)}\n")

# 5. Normalize all RGB values to 0.0-1.0 range (divide by 255)
#    Build a new list of dicts with the same structure but float values
#    [{"name": "midnight", "rgb": [0.059, 0.039, 0.157]}, ...]
#    Round to 3 decimal places
norm_rgb = [round(v / 255, 3) for v in c["rgb"]]
print(norm_rgb)

# 6. Generate a CSS-style export: list of strings like
#    ["--midnight: rgb(15, 10, 40);", "--ocean: rgb(0, 105, 148);", ...]

# 7. Split the palette into two groups:
#    "warm" colors where red channel > 150
#    "cool" colors where blue channel > red channel
#    Some colors may be neither. Build two separate lists of names.

# Print everything with clear labels

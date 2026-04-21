# Starting Data
palette = [
    {"name": "Cyber_Cyan", "rgb": (0, 255, 255)},
    {"name": "Neon_Pink", "rgb": (255, 20, 147)},
    {"name": "Matrix_Green", "rgb": (0, 255, 65)},
    {"name": "Void_Black", "rgb": (15, 15, 20)},
]

# Your Task: Write a list comprehension that extracts just the "name" of each color from the palette list. Print the resulting list.
color_names = [color["name"] for color in palette]

"""
color_names = []
for color in palette:
    color_names.append(color["name"])
"""
print(color_names)

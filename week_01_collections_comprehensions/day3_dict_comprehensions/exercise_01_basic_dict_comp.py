scene_objects = [
    {"name": "Hero_Cube", "type": "mesh"},
    {"name": "Key_Light", "type": "light"},
    {"name": "Fill_Light", "type": "light"},
    {"name": "Camera_Main", "type": "camera"},
    {"name": "Logo_Text", "type": "mesh"},
    {"name": "Env_Sphere", "type": "mesh"},
]

# 1. Build a lookup dict: name -> type
#    {"Hero_Cube": "mesh", "Key_Light": "light", ...}
lookup = {obj["name"]: obj["type"] for obj in scene_objects}
print("--- Lookup Dict: name -> type ---")
print(lookup, end="\n\n")

# 2. Build a count dict: how many of each type?
#    {"mesh": 3, "light": 2, "camera": 1}
#    Hint: first get unique types, then count with a comprehension
#    len() and list comprehension can work together here
types = {obj["type"] for obj in scene_objects}
count = {t: len([obj for obj in scene_objects if obj["type"] == t]) for t in types}

print("--- Count Dict: How many of each type? ---")
print(count, end="\n\n")

# 3. Build a dict of only mesh objects: name -> type
#    (filter inside the comprehension)
# mesh_obj = {obj["name"] for obj in scene_objects if obj["type"] == "mesh"}
mesh_count = {
    obj["name"]: obj["type"] for obj in scene_objects if obj["type"] == "mesh"
}

print("--- Mesh Dict: only meshes")
print(mesh_count)


# Print all three

scene = [
    {"name": "Hero_Cube", "type": "mesh", "visible": True, "poly_count": 8200},
    {"name": "BG_Plane", "type": "mesh", "visible": True, "poly_count": 2},
    {"name": "Key_Light", "type": "light", "visible": True, "poly_count": 0},
    {"name": "Fill_Light", "type": "light", "visible": False, "poly_count": 0},
    {"name": "Logo_Text", "type": "mesh", "visible": True, "poly_count": 45000},
    {"name": "Camera_Main", "type": "camera", "visible": True, "poly_count": 0},
    {"name": "Debris_Chunk", "type": "mesh", "visible": False, "poly_count": 1200},
]

# 1. Get a list of all object names (just the names)
obj_names = [obj["name"] for obj in scene]
print(obj_names)

# 2. Get names of only visible objects
obj_visibile = [obj["name"] for obj in scene if obj["visible"]]
print(obj_visibile)

# 3. Get names of only mesh objects that are visible
obj_mesh_visible = [
    obj["name"] for obj in scene if obj["visible"] and obj["type"] == "mesh"
]
print(obj_mesh_visible)

# 4. Get names of meshes with poly_count over 1000
polycount_1000 = [
    obj["name"] for obj in scene if obj["type"] == "mesh" and obj["poly_count"] > 1000
]
print(polycount_1000)

# 5. Get total poly count of all visible meshes (hint: sum() works on lists)
total_poly = sum(
    obj["poly_count"] for obj in scene if obj["visible"] and obj["type"] == "mesh"
)
print(total_poly)

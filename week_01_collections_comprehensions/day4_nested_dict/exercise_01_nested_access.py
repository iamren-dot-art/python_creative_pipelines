# C4D project config
project = {
    "name": "Brand_Launch_2026",
    "client": "Acme Corp",
    "timeline": {"fps": 24, "start_frame": 0, "end_frame": 240, "duration_seconds": 10},
    "render_settings": {
        "engine": "arnold",
        "resolution": {"width": 3840, "height": 2160},
        "output": {"format": "exr", "path": "/renders/brand_launch", "padding": 4},
    },
    "scenes": [
        {
            "name": "intro",
            "frame_range": [0, 72],
            "objects": ["logo", "bg_plane", "particles"],
        },
        {
            "name": "product_reveal",
            "frame_range": [73, 168],
            "objects": ["product_hero", "turntable_rig", "key_light", "fill_light"],
        },
        {
            "name": "end_card",
            "frame_range": [169, 240],
            "objects": ["logo", "legal_text", "cta_button"],
        },
    ],
}

# 1. Print the render engine name
# print(project["render_settings"]["engine"])
render = project.get("render_settings", {})
engine = render.get("engine")
print(engine)

# 2. Print the output resolution as "3840x2160"
print(
    f"{project['render_settings']['resolution']['width']}x{project['render_settings']['resolution']['height']}"
)

# 3. Print the name of the second scene
print(f"{project['scenes'][1]['name']}")

# 4. Print the frame range of the last scene (use negative indexing)
print(f"{project['scenes'][-1]['frame_range']}")

# 5. Print all object names from the "product_reveal" scene
for obj in project["scenes"][1]["objects"]:
    print(obj)

# 6. Print total number of objects across all scenes
#    Hint: sum() with a comprehension over project["scenes"]
total_obj = sum([len(scene["objects"]) for scene in project["scenes"]])
print(total_obj)

# 7. Safely get a key called "color_space" from render_settings with a default of "sRGB"
color = project["render_settings"].get("color_space", "sRGB")
print(color)

# Same project dict from Exercise 1 (paste it at the top)
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

# 1. Build a list of all scene names using a comprehension
#    ["intro", "product_reveal", "end_card"]
all_scenes = list(scene["name"] for scene in project["scenes"])
print(f"{all_scenes}, \n")

# 2. Build a flat list of ALL object names across ALL scenes
#    Hint: nested comprehension — for scene in scenes for obj in scene's objects
# for every scene in scene for obj in
all_obj = [obj for scene in project["scenes"] for obj in scene["objects"]]
print(f"{all_obj}, \n")

# 3. Build a dict mapping scene name to object count
#    {"intro": 3, "product_reveal": 4, "end_card": 3}
scene_objs = {scene["name"]: len(scene["objects"]) for scene in project["scenes"]}
print(f"{scene_objs}, \n")

# 4. Build a dict mapping scene name to frame duration
#    Duration = end_frame - start_frame from each scene's frame_range
#    {"intro": 72, "product_reveal": 95, "end_card": 71}
scene_frames = {
    scene["name"]: scene["frame_range"][1] - scene["frame_range"][0]
    for scene in project["scenes"]
}
print(scene_frames)

# Print all four

# C4D render layer setup
layer_names = ["beauty", "diffuse", "specular", "shadow", "ao"]
output_formats = ["exr", "exr", "exr", "png", "png"]

# 1. Use enumerate to print each layer with its index (starting at 1)
#    Expected: "Layer 1: beauty", "Layer 2: diffuse", etc.
for i, layer in enumerate(layer_names, start=1):
    print(f"Layer {i}: {layer}")

# 2. Use zip to pair each layer with its format and print
#    Expected: "beauty -> exr", "diffuse -> exr", etc.
for layer, ext in zip(layer_names, output_formats):
    print(f"{layer} -> {ext}")

# 3. Combine both: use enumerate AND zip together to print:
#    "Layer 1: beauty (exr)", "Layer 2: diffuse (exr)", etc.
for i, (layer, fmt) in enumerate(zip(layer_names, output_formats), start=1):
    print(f"Layer {i}: {layer} ({fmt})")

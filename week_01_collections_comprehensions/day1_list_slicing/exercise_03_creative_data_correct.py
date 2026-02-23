# Keyframe data from a C4D anim curve
frame_numbers = [0, 6, 12, 18, 24, 30, 36, 42, 48]
position_y = [0.0, 2.5, 8.0, 12.0, 14.5, 12.0, 8.0, 2.5, 0.0]

# 1. Get only the first half of the animation (use slicing)
#    Hint: you can use len() to find the midpoint
anim_duration = len(frame_numbers)
mid_index = anim_duration // 2
first_half = frame_numbers[: mid_index + 1]

# print(anim_duration)
# print(mid_index)
print("--- First Half ---")
print(f"{first_half}\n")

# 2. Get every 3rd keyframe pair using zip and slicing together
#    Expected output: pairs at frames 0, 18, 36
for frame, y in zip(frame_numbers[::3], position_y[::3]):
    print(f"Frame {frame} -> Y: {y}")

# 3. Use enumerate + zip to print a formatted keyframe sheet:
#    "Key 1: Frame 0 -> Y: 0.0"
#    "Key 2: Frame 6 -> Y: 2.5"
#    etc.
print("--- Enumerate + Zip Key Sheet ---")
for i, (frame, pos_y) in enumerate(zip(frame_numbers, position_y), start=1):
    print(f"Key {i}: Frame {frame} -> Y: {pos_y}")

print("\n")


# 4. Reverse the position_y values and zip with the original frame_numbers
#    to create a "mirror" animation. Print the result.
#    Expected: Frame 0 gets the value that was at Frame 48, etc.
position_y_inv = position_y[::-1]

print("--- Enumerate + Zip Key Sheet (reverse Y) ---")
for i, (frame, pos_y) in enumerate(zip(frame_numbers, position_y_inv), start=1):
    print(f"Key {i}: Frame {frame} -> Y: {pos_y}")

print("\n")

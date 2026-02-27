objects = ["logo", "title_card", "lower_third", "bug", "endcard"]
y_positions = [0.0, 150.0, -80.0, 45.0, 0.0]

# 1. Build a dict mapping object name to Y position
#    {"logo": 0.0, "title_card": 150.0, ...}
#    Hint: zip() gives you pairs, dict comprehension builds the dict
name_to_y = {name: y for name, y in zip(objects, y_positions)}
print(name_to_y, end="\n\n")

# 2. Build a dict of only objects that are above Y=0 (positive Y)
#    Filter inside the comprehension
above_y0 = {name: y for name, y in zip(objects, y_positions) if y > 0}
print(above_y0, end="\n\n")

# 3. Build a dict with normalized Y positions (divide each by the max absolute value)
#    Hint: max(abs(v) for v in y_positions) gets the largest magnitude
#    Result should have values between -1.0 and 1.0
max_abs = max(abs(v) for v in y_positions)
# y_positions_norm = {name: y / max_abs for name, y in zip(objects, y_positions)}
y_positions_norm = {name: y / max_abs for name, y in zip(objects, y_positions)}
print(max_abs, y_positions_norm, sep="\n\n")

# Print all three

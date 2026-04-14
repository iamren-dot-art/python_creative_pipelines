'''
Write a list comprehension that creates a list of just the camera "name" values, but only if their "lens" value is 50 or greater. Print the resulting list.
'''

# Data
cameras = [
    {"name": "Cam_Wide", "lens": 24},
    {"name": "Cam_Portrait", "lens": 50},
    {"name": "Came_Macro", "lens": 100}
]

'''
# Standard Loop
long_lenses = []

for cam in cameras:
    if cam["lens"] >= 50:
        long_lenses.append(cam["name"])

print(long_lenses)
'''

long_lenses = [ cam["name"] for cam in cameras if cam["lens"] >= 50 ]
print(long_lenses)
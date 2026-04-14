'''
Your Task: Write a dictionary comprehension using zip() that maps the material to its roughness, but only if the roughness is strictly greater than 0.0. Print the resulting dictionary.
(Hint: Your blueprint is { [KEY]: [VALUE] for [KEY], [VALUE] in zip(...) if [CONDITION] })
'''

# Data
materials = ["Wood", "Metal", "Glass"]
roughness = [0.8, 0.4, 0.0]


'''
# Standard Loop
rough_mats = {}

for mat, rough in zip(materials, roughness):
    if rough > 0.0:
        rough_mats[mat] = rough

print(rough_mats)
'''
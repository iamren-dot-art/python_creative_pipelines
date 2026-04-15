'''
Use zip() and a dict comprehension to create a dictionary called scene_state that maps the object name to its visibility. Print scene_state.

* * * * * * `

Deconstructing the Standard Loop

Think of a standard for loop exactly like the C4D timeline. You are telling Python to move the playhead forward one step at a time, look at the data at that specific moment, and execute an action before moving to the next step.
Python

scene_state = {}  # 1. The Setup

for obj, vis in zip(objects, visibility):  # 2. The Engine
    scene_state[obj] = vis                 # 3. The Action

    The Setup: We create an empty container. Think of this like dropping a new, empty Null object into your Object Manager.

    The Engine: zip() groups our lists into pairs: ("Cube", 1), then ("Sphere", 0), then ("Cloner", 1). The for command tells Python to step through those pairs one by one. obj and vis are just temporary labels (like naming a variable in an Xpresso node) that hold the data for the current step.

    The Action: On step one, obj is "Cube" and vis is 1. We tell Python: "Go to the scene_state dictionary, create a key called 'Cube', and set its value to 1." Then the loop automatically advances to the next step.

Bridging to the Comprehension

A comprehension is just the standard loop folded in on itself. Python developers realized that creating an empty container, looping, and appending to that container was so common that they built a shortcut.

A comprehension strips away the setup and the repetitive assignment code, leaving only the core logic wrapped inside the container brackets.

Here is the exact structural mapping:

Standard Loop:
for [Engine]:
add [Action]

Dict Comprehension:
{ [Action] for [Engine] }

    [Action]: obj: vis (This is the shape of the data we want to inject into the dictionary).

    [Engine]: obj, vis in zip(objects, visibility) (This is how we step through the data).

Put them together inside curly braces, and you get exactly what you wrote:
{obj: vis for obj, vis in zip(objects, visibility)}
'''

objects = ["Cube", "Sphere", "Cloner"]
visibility = [1, 0, 1]

'''
scene_state = {}

# Unpack the zipped pairs in to 'obj' and 'vis' variables
for obj, vis in zip(objects, visibility):
    scene_state[obj] = vis
'''

scene_state = {obj : vis for obj, vis in zip(objects, visibility)}

print(scene_state)
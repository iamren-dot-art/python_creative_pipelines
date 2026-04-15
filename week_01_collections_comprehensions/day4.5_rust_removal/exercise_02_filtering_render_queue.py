'''
Write a list comprehension that outputs a list of just the "take" names, only if their "render" key is True.

Because you are building a list, you use square brackets []. Because there is a condition, the blueprint looks like this:

[ [ACTION] for [ITEM] in [LIST] if [CONDITION] ]

Write the standard for loop first if you need to see the timeline step-by-step. Then fold it into the comprehension. Post your code and the exact output when you have it.
'''

# DATA
takes = [
    {"take": "Main", "render": True},
    {"take": "Shadow_Pass", "render": False},
    {"take": "Ambient_Occlusion", "render": True}
]

'''
# Standard Loop
render_takes = []

for job in takes:
    if job["render"] is True:
        render_takes.append(job["take"])

print(render_takes)

'''

# List comprehension
render_takes = [job["take"] for job in takes if job["render"]]
print(render_takes)
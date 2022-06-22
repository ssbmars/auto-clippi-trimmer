import os
import json
frames = 160	# choose how many frames you want to trim off the end (whole numbers only)

for filename in os.listdir():
    if not filename.endswith('json'): continue
    if filename.endswith('_trimmed.json'): continue
    with open(filename) as old, open(filename.replace('.json', '_trimmed.json'), 'w') as new:
        my_dict = json.load(old)
        for clip in my_dict['queue']:
            clip['endFrame'] -= frames # number of frames
        json.dump(my_dict, new, indent=2)
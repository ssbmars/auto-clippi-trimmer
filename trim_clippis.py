import os
import json
sec = 3		# choose how many seconds you want to trim off the end

for filename in os.listdir():
    if not filename.endswith('json'): continue
    with open(filename) as old, open(filename.replace('.json', '.new.json'), 'w') as new:
        my_dict = json.load(old)
        for clip in my_dict['queue']:
            clip['endFrame'] -= sec*60 # number of frames
        json.dump(my_dict, new, indent=2)
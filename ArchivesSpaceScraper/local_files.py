import os
import json

def load_json_file(fpath):
    return json.loads(open(fpath).read())

def load_json_dir(resource_dir):
    ret = []
    print("Loading %s" % resource_dir)
    for fname in os.listdir(resource_dir):
        if not fname.endswith(".json"): 
            continue
        fpath = os.path.join(resource_dir, fname)
        ret.append(load_json_file(fpath))
    return ret
        

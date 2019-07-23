from .asnake_client import get_client
from .local_files import load_json_file
import os
import json
from pathlib import Path
from urllib.parse import urlparse

def mkdir(directory):
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)

class ArchiveCloner:

    def __init__(self, repo_id, 
        root="./out", 
        credentials={}):

        self.repo_id = repo_id
        self.client = get_client(credentials)
        self.root = root

    def local_path(self, ref):
        
        return os.path.join(self.root, ref[1:] + ".json")
    
        # return path
    
    def update_resource(self, ref, new_json):

        self.client.post(ref, json=new_json)
    
    
    def get_resource(self, ref, redownload=False):

        return self.client.get(ref)
    
    def copy_resource(self, ref, redownload=False):

        fpath = self.local_path(urlparse(ref).path)

        # check to see if we already have the file
        if not redownload and os.path.isfile(fpath): 
            return load_json_file(fpath)

        # get the data
        resp = self.get_resource(ref, redownload=redownload)

        # check if something went wrong
        if (resp is None or resp.status_code) != 200:
            raise Exception ("Error downloading data")

        # save JSON file
        data = resp.json()

        dir_path = os.path.split(fpath)[0]

        mkdir(dir_path)

        open(fpath, "w").write(json.dumps(data, indent=2))

        return data



#     def copy_resource(self, ref, redownload=False):


#         fpath = self.local_path(urlparse(ref).path)

#         if not redownload and os.path.isfile(fpath): return

#         dir_path = os.path.split(fpath)[0]

#         mkdir(dir_path)

#         data = self.client.get(ref).json()

#         open(fpath, "w").write(json.dumps(data, indent=2))

        
        
        
        
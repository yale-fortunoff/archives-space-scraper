# uname = os.environ['ARCHIVESSPACE_USERNAME']
# pword = os.environ['ARCHIVESSPACE_PASSWORD']
import os
import yaml
from pathlib import Path
home = str(Path.home())

import configparser

def get_from_env():
    return {
        "baseurl":os.environ['ARCHIVESSPACE_BASE_URL'],
        "username":os.environ['ARCHIVESSPACE_USERNAME'],
        "password":os.environ['ARCHIVESSPACE_PASSWORD']
    }

def get_from_file(
    fpath=Path(home, ".archives-space-scraper", "credentials"),
    profile="default"):
    config = configparser.ConfigParser()
    fpath = os.path.expanduser(fpath)
    config.read(fpath)
    return dict(config._sections[profile])
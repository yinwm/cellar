# -*- coding:utf-8 -*-
# cellar

import yaml

settings = None

class Settings(dict):
    def __init__(self, yaml_file):
        with open(yaml_file) as f:
            self.update(yaml.load(f))

def build_settings(yaml_file):
    global settings
    settings = Settings(yaml_file)
    return settings
        

    

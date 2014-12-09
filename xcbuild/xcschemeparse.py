import os
import sys
import xml.etree.ElementTree as xml
import BSPathObject

def SchemeName(x):
    return x.name;

class xcschemeparse(object):
    path = {};
    contents = {};
    name = '';
    
    def __init__(self, path):
        self.path = BSPathObject.BSPathObject(path, '');
        self.name = os.path.basename(path).split('.xcscheme')[0];
        try:
            self.contents = xml.parse(self.path.obj_path);
        except:
            self.contents = {};
    
    def isValid(self):
        return self.contents != {};
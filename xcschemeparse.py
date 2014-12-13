import os
import sys
import xml.etree.ElementTree as xml
import xcbPathObject

def GetSharedPath(path):
    return os.path.join(path, 'xcshareddata/xcschemes');

def GetUserPath(path):
    return os.path.join(path, 'xcuserdata/'+os.getlogin()+'.xcuserdatad/xcschemes/');

def ParseDirectoryForXCSchemes(dir_path):
    schemes = [];
    if os.path.exists(dir_path) == True:
        for scheme_file in os.listdir(dir_path):
            scheme_file_path = os.path.join(dir_path, scheme_file);
            if not scheme_file.startswith('.') and scheme_file_path.endswith('.xcscheme') and os.path.isfile(scheme_file_path):
                scheme_xml = xcschemeparse(scheme_file_path);
                if scheme_xml.isValid() == True:
                    schemes.append(scheme_xml);
    return schemes;

def SchemeName(x):
    return x.name;

class xcschemeparse(object):
    path = {};
    contents = {};
    name = '';
    
    def __init__(self, path):
        self.path = xcbPathObject.xcbPathObject(path, '');
        self.name = os.path.basename(path).split('.xcscheme')[0];
        try:
            self.contents = xml.parse(self.path.obj_path);
        except:
            self.contents = {};
    
    def isValid(self):
        return self.contents != {};
from __future__ import absolute_import
import os
import sys
import xml.etree.ElementTree as xml

from ..Path import *

from .xcrun import *

from .XCSchemeActions.BuildAction import BuildAction
from .XCSchemeActions.TestAction import TestAction
from .XCSchemeActions.LaunchAction import LaunchAction
from .XCSchemeActions.ProfileAction import ProfileAction
from .XCSchemeActions.AnalyzeAction import AnalyzeAction
from .XCSchemeActions.ArchiveAction import ArchiveAction

def XCSchemeGetSharedPath(path):
    return os.path.join(path, 'xcshareddata/xcschemes');

def XCSchemeGetUserPath(path):
    return os.path.join(path, 'xcuserdata/'+os.getlogin()+'.xcuserdatad/xcschemes/');

def XCSchemeParseDirectory(dir_path):
    schemes = [];
    if os.path.exists(dir_path) == True:
        for scheme_file in os.listdir(dir_path):
            scheme_file_path = os.path.join(dir_path, scheme_file);
            if not scheme_file.startswith('.') and scheme_file_path.endswith('.xcscheme') and os.path.isfile(scheme_file_path):
                scheme_xml = xcscheme(scheme_file_path);
                if scheme_xml.isValid() == True:
                    schemes.append(scheme_xml);
    return schemes;

def XCSchemeName(x):
    return x.name;

class xcscheme(object):
    path = {};
    contents = {};
    name = '';
    
    def __init__(self, path):
        self.path = Path(path, '');
        self.name = os.path.basename(path).split('.xcscheme')[0];
        try:
            self.contents = xml.parse(self.path.obj_path);
        except:
            self.contents = {};
    
    def isValid(self):
        return self.contents != {};
    
    def getAction(self, action_type):
        for item in list(self.contents.getroot()):
            if item.tag == action_type:
                return item;
        return {};
    
    def buildAction(self, container):
        action = BuildAction(self.getAction('BuildAction'));
        for child in action.children:
            print xcrun.resolvePathFromLocation(child.target.ReferencedContainer, container.path.base_path, container.path.base_path);
    
    def testAction(self, container):
        action = TestAction(self.getAction('TestAction'));
    
    def launchAction(self, container):
        action = LaunchAction(self.getAction('LaunchAction'));
    
    def profileAction(self, container):
        action = ProfileAction(self.getAction('ProfileAction'));
    
    def analyzeAction(self, container):
        action = AnalyzeAction(self.getAction('AnalyzeAction'));
    
    def archiveAction(self, container):
        action = ArchiveAction(self.getAction('ArchiveAction'));
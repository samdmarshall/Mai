from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXTargetDependency(object):
    target = {};
    proxy = {};
    
    def __init__(self, dictionary, project):
        if 'target' in dictionary.keys():
            self.target = PBXResolver(project.objects()[dictionary['target']], project);
        if 'targetProxy' in dictionary.keys():
            self.target = PBXResolver(project.objects()[dictionary['targetProxy']], project);
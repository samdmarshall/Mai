from __future__ import absolute_import
import Cocoa
import Foundation
import os

class PBXFrameworkBuildPhase(object):
    frameworks = [];
    
    def __init__(self, dictionary, project):
        if 'files' in dictionary.keys():
            for file in dictionary['files']:
                self.frameworks.append(file);
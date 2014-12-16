import Cocoa
import Foundation
import os

class pbxframeworkbuildphase(object):
    self.frameworks = [];
    
    def __init__(self, dictionary, project):
        if 'files' in dictionary.keys():
            for file in dictionary['files']:
                self.frameworks.append(file);
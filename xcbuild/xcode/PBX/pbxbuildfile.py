from __future__ import absolute_import
import Cocoa
import Foundation
import os

class PBXBuildFile(object):
    reference = {};
    
    def __init__(self, dictionary, project):
        if 'fileRef' in dictionary.keys():
            self.reference = dictionary['fileRef'];
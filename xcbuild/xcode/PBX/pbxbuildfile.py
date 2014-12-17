from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXBuildFile(object):
    fileRef = {};
    
    def __init__(self, dictionary, project):
        if 'fileRef' in dictionary.keys():
            self.fileRef = PBXResolver(project.objects()[dictionary['fileRef']], project);
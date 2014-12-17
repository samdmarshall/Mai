from __future__ import absolute_import
import Cocoa
import Foundation
import os

class pbxfilereference(object):
    name = '';
    path = '';
    ftype = '';
    
    def __init__(self, dictionary, project):
        if 'path' in dictionary.keys():
            self.path = dictionary['path'];
            self.name = os.path.basename(self.path);
        if 'lastKnownFileType' in dictionary.keys():
            self.ftype = dictionary['lastKnownFileType'];
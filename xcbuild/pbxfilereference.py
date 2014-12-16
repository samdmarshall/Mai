import Cocoa
import Foundation
import os

class pbxfilereference(object):
    name = '';
    path = '';
    ftype = '';
    owner = {};
    
    def __init__(self, dictionary, proj):
        self.owner = proj;
        if 'path' in dictionary.keys():
            self.path = dictionary['path'];
            self.name = os.path.basename(self.path);
        if 'lastKnownFileType' in dictionary.keys():
            self.ftype = dictionary['lastKnownFileType'];
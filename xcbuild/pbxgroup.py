import Cocoa
import Foundation
import os

class pbxgroup(object):
    self.name = '';
    self.children = [];
    
    def __init__(self, dictionary, project):
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'children' in dictionary.keys():
            for child in dictionary['children']:
                self.children.append(child)
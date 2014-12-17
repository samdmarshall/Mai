from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXVariantGroup(object):
    name = '';
    path = '';
    children = [];
    
    def __init__(self, dictionary, project):
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'path' in dictionary.keys():
            self.path = dictionary['path'];
        if 'children' in dictionary.keys():
            for child in dictionary['children']:
                self.children.append(PBXResolver(project.objects()[child], project));
from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXGroup(object):
    name = '';
    path = '';
    children = [];
    
    def __init__(self, lookup_func, dictionary, project):
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'children' in dictionary.keys():
            for child in dictionary['children']:
                result = lookup_func(project.objects()[child]);
                if result[0] == True:
                    self.children.append(result[1](lookup_func, project.objects()[child], project));
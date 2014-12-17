from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXAggregateTarget(object):
    buildConfigurationList = {};
    buildPhases = [];
    dependencies = [];
    name = '';
    productName = '';
    
    def __init__(self, dictionary, project):
        if 'buildConfigurationList' in dictionary.keys():
            self.buildConfigurationList = PBXResolver(project.objects()[dictionary['buildConfigurationList']], project);
        if 'buildPhases' in dictionary.keys():
            for phase in dictionary['buildPhases']:
                self.buildPhases.append(PBXResolver(project.objects()[phase], project));
        if 'dependencies' in dictionary.keys():
            for dep in dictionary['dependencies']:
                # this may need to be changed to PBXTargetDependency
                self.dependencies.append(dep);
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'productName' in dictionary.keys():
            self.productName = dictionary['productName'];
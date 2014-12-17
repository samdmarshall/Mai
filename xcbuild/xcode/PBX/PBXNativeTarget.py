from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXNativeTarget(object):
    buildConfigurationList = {};
    buildPhases = [];
    buildRules = [];
    dependencies = [];
    name = '';
    productName = '';
    productReference = {};
    productType = '';
    
    def __init__(self, dictionary, project):
        if 'buildConfigurationList' in dictionary.keys():
            self.buildConfigurationList = PBXResolver(project.objects()[dictionary['buildConfigurationList']], project);
        if 'buildPhases' in dictionary.keys():
            for phase in dictionary['buildPhases']:
                self.buildPhases.append(PBXResolver(project.objects()[phase], project));
        if 'buildRules' in dictionary.keys():
            for rule in dictionary['buildRules']:
                self.buildRules.append(PBXResolver(project.objects()[rule], project));
        if 'dependencies' in dictionary.keys():
            for dep in dictionary['dependencies']:
                # this may need to be changed to PBXTargetDependency
                self.dependencies.append(dep);
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'productName' in dictionary.keys():
            self.productName = dictionary['productName'];
        if 'productReference' in dictionary.keys():
            self.productReference = PBXResolver(project.objects()[dictionary['productReference']], project);
        if 'productType' in dictionary.keys():
            self.productType = dictionary['productType'];
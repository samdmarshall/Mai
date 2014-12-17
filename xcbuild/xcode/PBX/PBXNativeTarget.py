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
    
    def __init__(self, lookup_func, dictionary, project):
        if 'buildConfigurationList' in dictionary.keys():
            result = lookup_func(project.objects()[dictionary['buildConfigurationList']])
            if result[0] == True:
                self.buildConfigurationList = result[1](lookup_func, project.objects()[dictionary['buildConfigurationList']], project);
        if 'buildPhases' in dictionary.keys():
            for phase in dictionary['buildPhases']:
                result = lookup_func(project.objects()[phase]);
                if result[0] == True:
                    self.buildPhases.append(result[1](lookup_func, project.objects()[phase], project));
        if 'buildRules' in dictionary.keys():
            for rule in dictionary['buildRules']:
                result = lookup_func(project.objects()[rule]);
                if result[0] == True:
                    print project.objects()[rule]
                    self.buildRules.append(result[1](lookup_func, project.objects()[rule], project));
        if 'dependencies' in dictionary.keys():
            for dep in dictionary['dependencies']:
                # this may need to be changed to PBXTargetDependency
                self.dependencies.append(dep);
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'productName' in dictionary.keys():
            self.productName = dictionary['productName'];
        if 'productReference' in dictionary.keys():
            result = lookup_func(project.objects()[dictionary['productReference']]);
            if result[0] == True:
                self.productReference = result[1](lookup_func, project.objects()[dictionary['productReference']], project);
        if 'productType' in dictionary.keys():
            self.productType = dictionary['productType'];
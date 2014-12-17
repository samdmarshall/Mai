from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXApplicationTarget(object):
    buildConfigurationList = {};
    buildPhases = [];
    dependencies = [];
    name = '';
    productName = '';
    productInstallPath = '';
    productReference = {};
    productSettingsXML = '';
    
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
        if 'dependencies' in dictionary.keys():
            for dep in dictionary['dependencies']:
                # this may need to be changed to PBXTargetDependency
                self.dependencies.append(dep);
        if 'name' in dictionary.keys():
            self.name = dictionary['name'];
        if 'productName' in dictionary.keys():
            self.productName = dictionary['productName'];
        if 'productInstallPath' in dictionary.keys():
            self.productInstallPath = dictionary['productInstallPath'];
        if 'productSettingsXML' in dictionary.keys():
            self.productSettingsXML = dictionary['productSettingsXML'];
        if 'productReference' in dictionary.keys():
            result = lookup_func(project.objects()[dictionary['productReference']]);
            if result[0] == True:
                self.productReference = result[1](lookup_func, project.objects()[dictionary['productReference']], project);
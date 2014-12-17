from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class XCConfigurationList(object):
    buildConfigurations = [];
    defaultConfigurationIsVisible = 0;
    defaultConfigurationName = '';
    
    def __init__(self, lookup_func, dictionary, project):
        if 'buildConfigurations' in dictionary.keys():
            for configuration in dictionary['buildConfigurations']:
                result = lookup_func(project.objects()[configuration]);
                if result[0] == True:
                    self.buildConfigurations.append(result[1](lookup_func, project.objects()[configuration], project));
        if 'defaultConfigurationName' in dictionary.keys():
            self.defaultConfigurationName = dictionary['defaultConfigurationName'];
        if 'defaultConfigurationIsVisible' in dictionary.keys():
            self.defaultConfigurationIsVisible = dictionary['defaultConfigurationIsVisible'];
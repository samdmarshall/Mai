from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXProject(object):
    attributes = {};
    buildConfigurationList = {};
    compatibilityVersion = '';
    developmentRegion = '';
    hasScannedForEncodings = 0;
    knownRegions = [];
    mainGroup = {};
    projectDirPath = '';
    projectRoot = '';
    targets = {};
    
    def __init__(self, dictionary, project):
        if 'attributes' in dictionary.keys():
            self.attributes = dictionary['attributes'];
        if 'buildConfigurationList' in dictionary.keys():
            self.buildConfigurationList = PBXResolver(project.objects()[dictionary['buildConfigurationList']], project);
        if 'compatibilityVersion' in dictionary.keys():
            self.compatibilityVersion = dictionary['compatibilityVersion'];
        if 'developmentRegion' in dictionary.keys():
            self.developmentRegion = dictionary['developmentRegion'];
        if 'hasScannedForEncodings' in dictionary.keys():
            self.hasScannedForEncodings = dictionary['hasScannedForEncodings'];
        if 'knownRegions' in dictionary.keys():
            self.knownRegions = dictionary['knownRegions'];
        if 'mainGroup' in dictionary.keys():
            self.mainGroup = PBXResolver(project.objects()[dictionary['mainGroup']], project);
        if 'projectDirPath' in dictionary.keys():
            self.projectDirPath = dictionary['projectDirPath'];
        if 'projectRoot' in dictionary.keys():
            self.projectRoot = dictionary['projectRoot'];
        if 'targets' in dictionary.keys():
            for target in dictionary['targets']:
                self.targets.append(PBXResolver(project.objects()[target], project));
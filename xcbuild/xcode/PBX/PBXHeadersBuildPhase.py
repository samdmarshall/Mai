from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXHeadersBuildPhase(object):
    buildActionMask = 0;
    files = [];
    runOnlyForDeploymentPostprocessing = 0;
    
    def __init__(self, dictionary, project):
        if 'buildActionMask' in dictionary.keys():
            self.buildActionMask = dictionary['buildActionMask'];
        if 'files' in dictionary.keys():
            for file in dictionary['files']:
                self.files.append(PBXResolver(project.objects()[file], project));
        if 'runOnlyForDeploymentPostprocessing' in dictionary.keys():
            self.runOnlyForDeploymentPostprocessing = dictionary['runOnlyForDeploymentPostprocessing'];
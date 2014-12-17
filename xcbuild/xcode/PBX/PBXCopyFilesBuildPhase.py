from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXCopyFilesBuildPhase(object):
    buildActionMask = '';
    dstPath = '';
    dstSubfolderSpec = 0;
    files = [];
    runOnlyForDeploymentPostprocessing = 0;
    
    def __init__(self, dictionary, project):
        if 'buildActionMask' in dictionary.keys():
            self.buildActionMask = dictionary['buildActionMask'];
        if 'dstPath' in dictionary.keys():
            self.dstPath = dictionary['dstPath'];
        if 'dstSubfolderSpec' in dictionary.keys():
            self.dstSubfolderSpec = dictionary['dstSubfolderSpec'];
        if 'files' in dictionary.keys():
            for file in dictionary['files']:
                self.files.append(PBXResolver(project.objects()[file], project));
        if 'runOnlyForDeploymentPostprocessing' in dictionary.keys():
            self.runOnlyForDeploymentPostprocessing = dictionary['runOnlyForDeploymentPostprocessing'];
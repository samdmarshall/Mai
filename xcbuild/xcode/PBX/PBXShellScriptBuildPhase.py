from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXResolver import *

class PBXShellScriptBuildPhase(object):
    buildActionMask = 0;
    files = [];
    inputPaths = [];
    outputPaths = [];
    shellPath = '';
    shellScript = '';
    runOnlyForDeploymentPostprocessing = 0;
    
    def __init__(self, dictionary, project):
        if 'buildActionMask' in dictionary.keys():
            self.buildActionMask = dictionary['buildActionMask'];
        if 'files' in dictionary.keys():
            for file in dictionary['files']:
                self.files.append(PBXResolver(project.objects()[file], project));
        if 'runOnlyForDeploymentPostprocessing' in dictionary.keys():
            self.runOnlyForDeploymentPostprocessing = dictionary['runOnlyForDeploymentPostprocessing'];
        if 'shellScript' in dictionary.keys():
            self.shellScript = dictionary['shellScript'];
        if 'shellPath' in dictionary.keys():
            self.shellPath = dictionary['shellPath'];
        if 'inputPaths' in dictionary.keys():
            for inputPath in dictionary['inputPaths']:
                self.inputPaths.append(PBXResolver(project.objects()[inputPath], project));
        if 'outputPaths' in dictionary.keys():
            for outputPath in dictionary['outputPaths']:
                self.outputPaths.append(PBXResolver(project.objects()[outputPath], project));
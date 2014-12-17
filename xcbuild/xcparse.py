from .xcodeproj import *
from .xcworkspace import *
from .Logger import *
import os
import importlib

class xcparse(object):
    root = {};
    projects = [];
    name = '';
    root_path = '';
    
    def __init__(self, path):
        if os.path.exists(path) == True:
            self.root_path = path;
            self.name = os.path.basename(path);
            if self.name.endswith('.xcodeproj') or self.name.endswith('.pbproj'):
                project_file = xcodeproj(path);
                self.projects.append(project_file);
                self.root = project_file;
            elif self.name.endswith('.xcworkspace'):
                workspace_file = xcworkspace(path);
                self.root = workspace_file;
                for project_file in workspace_file.projects():
                    self.projects.append(project_file);
            else:
                Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Invalid file!'), Logger.colour('reset', True)]);
        else:
            Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Could not find file!'), Logger.colour('reset', True)]);
    
    def schemes(self):
        project_schemes = [];
        for project_file in self.projects:
            for scheme in project_file.schemes():
                project_schemes.append(scheme);
        root_schemes = self.root.schemes();
        return root_schemes + project_schemes;
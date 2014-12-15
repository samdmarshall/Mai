from .xcprojparse import *
from .xcwsparse import *
import os
import importlib

class xcparse():
    root = {};
    projects = [];
    name = '';
    root_path = '';
    
    def __init__(self, path):
        if os.path.exists(path) == True:
            self.root_path = path;
            self.name = os.path.basename(path);
            if self.name.endswith('.xcodeproj') or self.name.endswith('.pbproj'):
                project_file = xcprojparse.xcprojparse(path);
                self.projects.append(project_file);
                self.root = project_file;
            elif self.name.endswith('.xcworkspace'):
                workspace_file = xcwsparse.xcwsparse(path);
                self.root = workspace_file;
                for project_file in workspace_file.projects():
                    self.projects.append(project_file);
            else:
                print 'invalid file';
        else:
            print 'Could not find file';
    
    def iterateProjectsForCall(self, call):
        items = [];
        for project_file in self.projects:
            project_items = getattr(project_file, call)();
            for item in project_items:
                items.append(item);
        return items;
        
    def schemes(self):
        project_schemes = self.iterateProjectsForCall('schemes');
        root_schemes = self.root.schemes();
        return root_schemes + project_schemes;
        
    def targets(self):
        project_targets = self.iterateProjectsForCall('targets');
        root_targets = [];
        return root_targets + project_targets;
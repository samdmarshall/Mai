import xcprojparse
import xcwsparse
import os
import importlib

class xcparse(object):
    projects = [];
    
    def __init__(self, path):
        if os.path.exists(path) == True:
            extension = os.path.basename(path);
            if extension.endswith('.xcodeproj') or extension.endswith('.pbproj'):
                project_file = xcprojparse.xcprojparse(path);
                self.projects.append(project_file);
            elif extension.endswith('.xcworkspace'):
                workspace_file = xcwsparse.xcwsparse(path);
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
        return self.iterateProjectsForCall('schemes');
        
    def targets(self):
        return self.iterateProjectsForCall('targets');
import xcbPathObject
import xcprojparse
import xml.etree.ElementTree as xml
import os
import sys
import developer_tools
import xcschemeparse

class xcwsparse(object):
    path = {};
    data = {};
    
    def __init__(self, xcworkspace_path):
        self.path = xcbPathObject.xcbPathObject(xcworkspace_path, 'contents.xcworkspacedata');
        
        if os.path.exists(self.path.root_path) == True:
            try:
                self.data = xml.parse(self.path.root_path);
            except:
                self.data = {};
        else:
            print 'Invalid xcworkspace file!';
    
    def isValid(self):
        return self.data != {};
    
    def ResolvePathFromXMLItem(self, node, path):
        file_relative_path = node.attrib['location'];
        path_type, item_path = file_relative_path.split(':');
        if path_type == 'group':
            return os.path.join(path, item_path);
        elif path_type == 'absolute':
            return item_path;
        elif path_type == 'developer':
            return os.path.join(developer_tools.resolve_developer_path(), item_path);
        elif path_type == 'container':
            return os.path.join(self.path.base_path, item_path);
        else:
            print 'Invalid item path name!';
            return item_path;
    
    def ParsePathsFromXMLItem(self, node, path):
        results = [];
        item_path = self.ResolvePathFromXMLItem(node, path);
        if node.tag == 'FileRef':
            if os.path.exists(item_path) == True:
                project_parse = xcprojparse.xcprojparse(item_path);
                if project_parse.isValid() == True:
                    results.append(project_parse);
        if node.tag == 'Group':
            path = os.path.join(path, item_path);
            for child in node:
                group_results = self.ParsePathsFromXMLItem(child, path);
                for item in group_results:
                    results.append(item);
        return results;
    
    def projects(self):
        indexed_projs = [];
        if self.data != '':
            workspace_base_path = self.path.base_path;
            workspace_root = self.data.getroot();
            for child in workspace_root:
                results = self.ParsePathsFromXMLItem(child, workspace_base_path);
                for item in results:
                    indexed_projs.append(item);
        return indexed_projs;
    
    def schemes(self):
        schemes = [];
        # shared schemes
        shared_path = xcschemeparse.GetSharedPath(self.path.obj_path);
        shared_schemes = xcschemeparse.ParseDirectoryForXCSchemes(shared_path);
        # user schemes
        user_path = xcschemeparse.GetUserPath(self.path.obj_path);
        user_schemes = xcschemeparse.ParseDirectoryForXCSchemes(user_path);
        # merge schemes
        for scheme in shared_schemes + user_schemes:
            schemes.append(scheme);
        return schemes;
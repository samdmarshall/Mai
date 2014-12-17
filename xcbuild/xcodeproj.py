import Cocoa
import Foundation
from .Path import *
from .xcscheme import *
from .Logger import *
import os
import sys

class xcodeproj(object):
    path = {};
    contents = {};
    
    def __init__(self, xcproj_path):
        if xcproj_path.endswith('.xcodeproj') or xcproj_path.endswith('.pbproj'):
            self.path = Path(xcproj_path, 'project.pbxproj');
            
            if os.path.exists(self.path.root_path) == True:
                # loading project file
                plistNSData, errorMessage = Foundation.NSData.dataWithContentsOfFile_options_error_(self.path.root_path, Foundation.NSUncachedRead, None);
                if errorMessage == None:
                    plistContents, plistFormat, errorMessage = Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(plistNSData, Foundation.NSPropertyListMutableContainers, None, None);
                    if errorMessage == None:
                        self.contents = plistContents;
                    else:
                        print errorMessage;
                else:
                    print errorMessage;
            else:
                Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Invalid xcodeproj file!'), Logger.colour('reset', True)]);
    
    def isValid(self):
        return self.contents != {};
    
    def objects(self):
        return self.contents['objects'];
    
    def rootObject(self):
        return self.objects()[self.contents['rootObject']];
    
    def targets(self):
        targets = [];
        target_ids = self.rootObject()['targets'];
        for target in target_ids:
            targets.append(self.objects()[target]);
        return targets;
    
    def schemes(self):
        schemes = [];
        # shared schemes
        shared_path = XCSchemeGetSharedPath(self.path.obj_path);
        shared_schemes = XCSchemeParseDirectory(shared_path);
        # user schemes
        user_path = XCSchemeGetUserPath(self.path.obj_path);
        user_schemes = XCSchemeParseDirectory(user_path);
        # merge schemes
        for scheme in shared_schemes + user_schemes:
            schemes.append(scheme);
        return schemes;
    
    def iterateObjectsForType(self, isa_key, callback):
        items = [];
        objects = self.objects();
        for item in objects:
            if objects[item]['isa'] == isa_key:
                new_item = callback(objects[item], self.contents);
                items.append(new_item);
        return items;
    
    def files(self):
        return self.iterateObjectsForType('PBXFileReference', pbxfilereference);
    
    def groups(self):
        return self.iterateObjectsForType('PBXGroup', pbxgroup);
    
    def frameworks(self):
        return self.iterateObjectsForType('PBXFrameworksBuildPhase', pbxframeworkbuildphase);
    
    def buildfiles(self):
        return self.iterateObjectsForType('PBXBuildFile', pbxframeworkbuildphase);
    
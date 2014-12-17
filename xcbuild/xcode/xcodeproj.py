from __future__ import absolute_import
import Cocoa
import Foundation
import os
import sys

from ..Path import *
from ..Logger import *

from .xcscheme import *

from .PBX.PBXResolver import PBXResolver

class xcodeproj(object):
    path = {};
    contents = {};
    rootObject = {};
    
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
                        result = PBXResolver(self.objects()[self.contents['rootObject']])
                        if result[0] == True:
                            self.rootObject = result[1](PBXResolver, self.objects()[self.contents['rootObject']], self);
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
    
    def targets(self):
        if self.rootObject != {}:
            return self.rootObject.targets;
        else:
            return [];
    
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
    
    def hasSchemeWithName(self, scheme_name):
        schemes = self.schemes();
        result = scheme_name in list(map(XCSchemeName, schemes));
        found_scheme = {};
        for scheme in schemes:
            if scheme.name == scheme_name:
                found_scheme = scheme;
                break;
        return (result, found_scheme);
    
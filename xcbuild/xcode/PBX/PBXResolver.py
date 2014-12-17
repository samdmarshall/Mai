from __future__ import absolute_import
import Cocoa
import Foundation
import os

from .PBXBuildFile import *
from .PBXFileReference import *
from .PBXFrameworkBuildPhase import *
from .PBXGroup import *
from .PBXNativeTarget import *
from .PBXHeadersBuildPhase import *
from .XCConfigurationList import *
from .XCBuildConfiguration import *
from .PBXSourcesBuildPhase import *
from .PBXVariantGroup import *
from .PBXTargetDependency import *
from .PBXAggregateTarget import *
from .PBXApplicationTarget import *
from .PBXContainerItemProxy import *
from .PBXCopyFilesBuildPhase import *
from .PBXProject import *
from .PBXResourcesBuildPhase import *
from .PBXRezBuildPhase import *
from .PBXShellScriptBuildPhase import *
from .PBXGenericBuildPhase import *

TYPE_RESOLVER = {
    'PBXBuildFile': PBXBuildFile,
    'PBXFileReference': PBXFileReference,
    'PBXFrameworkBuildPhase': PBXFrameworkBuildPhase,
    'PBXGroup': PBXGroup,
    'PBXNativeTarget': PBXNativeTarget,
    'PBXHeadersBuildPhase': PBXHeadersBuildPhase,
    'XCConfigurationList': XCConfigurationList,
    'XCBuildConfiguration': XCBuildConfiguration,
    'PBXSourcesBuildPhase': PBXSourcesBuildPhase,
    'PBXVariantGroup': PBXVariantGroup,
    'PBXTargetDependency': PBXTargetDependency,
    'PBXAggregateTarget': PBXAggregateTarget,
    'PBXApplicationTarget': PBXApplicationTarget,
    'PBXContainerItemProxy': PBXContainerItemProxy,
    'PBXCopyFilesBuildPhase': PBXCopyFilesBuildPhase,
    'PBXProject': PBXProject,
    'PBXResourcesBuildPhase': PBXResourcesBuildPhase,
    'PBXRezBuildPhase': PBXRezBuildPhase,
    'PBXShellScriptBuildPhase': PBXShellScriptBuildPhase
};

def PBXResolver(dictionary, project):
        if dictionary['isa'] in TYPE_RESOLVER.keys():
            return TYPE_RESOLVER[dictionary['isa']](dictionary, project);
        else:
            return {};
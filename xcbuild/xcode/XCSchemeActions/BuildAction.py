from __future__ import absolute_import
import xml.etree.ElementTree as xml

from .BuildActionEntry import *
from ..xcrun import *
from ..PBX.PBXResolver import *

class BuildAction(object):
    # contents = {};
    # children = [];
    # parallel = False;
    # implicit = False;
    
    def __init__(self, action_xml):
        self.contents = action_xml;
        if 'parallelizeBuildables' in self.contents.keys():
            self.parallel = self.contents.get('parallelizeBuildables');
        if 'buildImplicitDependencies' in self.contents.keys():
            self.implicit = self.contents.get('buildImplicitDependencies');
        children = [];
        for build_entry in list(self.contents.find('./BuildActionEntries')):
            children.append(BuildActionEntry(build_entry));
        self.children = children;
    
    def performAction(self, container, project_constructor, scheme_config_settings):
        for child in self.children:
            project_path = xcrun.resolvePathFromLocation(child.target.ReferencedContainer, container[2].path.base_path, container[2].path.base_path);
            project = project_constructor(project_path);
            
            build_command = 'xcodebuild -project "'+project.path.obj_path+'" -scheme "'+container[1].name+'" ';
            for item in scheme_config_settings:
                build_command+=str(item)+' ';
            result = xcrun.make_subprocess_call(build_command, True);
            print result[0];
            
            # target_constructor = PBXResolver(project.objects()[child.target.BlueprintIdentifier]);
            # if target_constructor[0] == True:
            #     target = target_constructor[1](PBXResolver, project.objects()[child.target.BlueprintIdentifier], project);
            #     print target.name;
            #     for phase in target.buildPhases:
            #         phase.performPhase();
from __future__ import absolute_import
import xml.etree.ElementTree as xml

from .BuildActionEntry import *

class BuildAction(object):
    contents = {};
    children = [];
    parallel = False;
    implicit = False;
    
    def __init__(self, action_xml):
        self.contents = action_xml;
        if 'parallelizeBuildables' in self.contents.keys():
            self.parallel = self.contents.get('parallelizeBuildables');
        if 'buildImplicitDependencies' in self.contents.keys():
            self.implicit = self.contents.get('buildImplicitDependencies');
        for build_entry in list(self.contents.find('./BuildActionEntries')):
            self.children.append(BuildActionEntry(build_entry));
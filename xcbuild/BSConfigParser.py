import os
import sys
import ConfigParser
import collections

class BSConfigParser():
    path = '';
    contents = {};
    
    def __init__(self, config_path):
        if os.path.exists(config_path) == True:
            self.path = config_path;
            self.contents = ConfigParser.ConfigParser(dict_type=collections.OrderedDict);
            self.contents.read(self.path);
    
    def sections(self):
        return self.contents.sections();
    
    def options(self, section):
        return self.contents.options(section);
    
    def ValidateSections(self, scheme_list):
        scheme_set = set(scheme_list);
        section_set = set(self.sections());
        return (section_set.issubset(scheme_set), section_set.difference(scheme_set));
    
    def ValidateSetting(self, scheme, settings_list):
        for setting in settings_list:
            print setting+': '+self.contents.get(scheme, setting);
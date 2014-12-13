import os
import sys
import ConfigParser
import collections
import xcschemeparse
import re

class xcbConfigParser():
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
    
    def ParseSetting(self, scheme, option):
        value = self.contents.get(scheme, option);
        def interpolate_func(match):
            d = match.groupdict();
            section = d.get('section', scheme);
            key = d.get('key');
            return self.contents.get(section, key);
        subvalue = re.sub(re.compile(r"\$\[(?:(?P<section>[^:]+):)?(?P<key>[^}]+)\]"), interpolate_func, value);
        if value == subvalue:
            return value;
        else:
            return subvalue;
    
    def ValidateSections(self, scheme_list):
        scheme_set = set(list(map(xcschemeparse.SchemeName, scheme_list)));
        section_set = set(self.sections());
        return (section_set.issubset(scheme_set), section_set.difference(scheme_set));
    
    def ValidateSetting(self, scheme, settings_list):
        config_args = [];
        for setting in settings_list:
            config_args.append(str(setting.upper()+'="'+self.ParseSetting(scheme, setting)+'"'));
        return config_args;
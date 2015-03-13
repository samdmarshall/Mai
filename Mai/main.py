from __future__ import absolute_import
import os
import sys
import argparse

from .Config import *
from .xcode.xcparse import xcparse
from .xcode.xcparse.Xcode.BuildSystem import xcbuildsystem
from .xcode.xcparse.Xcode import xcodeproj
from .xcode.xcparse.Xcode import xcscheme
from .xcode.xcparse.Helpers import xcrun_helper

# Main
def main():
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-c', '--config', help='path to the build config file', action='store');
    parser.add_argument('-a', '--action', help='action to perform: "build", "test", "analyze", or "archive"', action='store');
    args = parser.parse_args();
    
    xcparser = xcparse(args.filename);
    
    build_system = xcbuildsystem();
    
    if args.list == True:
        print 'Schemes';
                        
        scheme_list = xcparser.schemes();
        high_count = 0;
        for scheme in scheme_list:
            if high_count < len(scheme.name):
                high_count = len(scheme.name);
        name_formatter = '%'+str(high_count)+'s';
        
        print '%*s' % (high_count, '='*(high_count+12+1));
        
        for scheme in scheme_list:
            shared_status = 'user ';
            if scheme.shared == True:
                shared_status = 'shared';
            print '[%*s] (%6s) # %s (%s)' % (high_count, scheme.name, shared_status, os.path.basename(scheme.container.obj_path), os.path.relpath(scheme.container.obj_path, start=os.path.dirname(xcparser.root_path)));
            
        sys.exit();
    
    if args.config != None and os.path.exists(args.config) == True:
        config_file = Config(args.config);
        
        all_schemes = set(map(lambda scheme: scheme.name, xcparser.schemes()));
        validate_config_schemes = config_file.validateSections(all_schemes);
        if validate_config_schemes[0] == False:
            print 'Could not find Schemes with names: ';
            
            for invalid_scheme in list(validate_config_schemes[1]):
                print str(invalid_scheme);
            
            sys.exit();
        
        for scheme in config_file.sections():
            config_scheme_settings = config_file.options(scheme);
            
            validate_config_scheme_settings = config_file.validateSetting(scheme, config_scheme_settings);
            
            result = xcparser.findSchemeWithName(scheme)[0];
            if result[0] == True and args.action != None:
                action_func = result[1].actionLookup(args.action);
                if action_func != None:
                    action_item = action_func(result[2]);
                    action_item.performAction(build_system, result, xcparser, validate_config_scheme_settings);
                else:
                    print 'Please supply an action: "build", "test", "analyze", or "archive"';
            else:
                print 'Please specify an action with the -a/--action flag';

if __name__ == "__main__":
    main();
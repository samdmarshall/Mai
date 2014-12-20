from __future__ import absolute_import
import os
import sys
import argparse

from .Logger import *
from .Config import *
from .xcode import xcparse
from .xcode import xcodeproj
from .xcode import xcscheme
from .xcode import xcrun

# Main
def main():
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-c', '--config', help='path to the build config file', action='store');
    parser.add_argument('-a', '--action', help='action to perform: "build", "test", "analyze", or "archive"', action='store');
    args = parser.parse_args();
    
    xcparser = xcparse(args.filename);
    
    if args.list == True:
        Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Schemes'), Logger.colour('reset', True)]);
        Logger.debuglog([Logger.colour('blue',True), Logger.string('%s', '========================'), Logger.colour('reset', True)]);
        for scheme in xcparser.schemes():
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', '['+scheme.name+'] # '+os.path.basename(scheme.container.obj_path)), Logger.colour('reset', True)]);
        sys.exit();
    
    if args.config != None and os.path.exists(args.config) == True:
        config_file = Config(args.config);
        
        validate_config_schemes = config_file.validateSections(xcparser.schemeNameSet());
        if validate_config_schemes[0] == False:
            Logger.debuglog([Logger.colour('black',True), Logger.string('%s', 'Could not find Schemes with names: '), Logger.colour('reset', True)]);
            for invalid_scheme in list(validate_config_schemes[1]):
                Logger.debuglog([Logger.colour('red',True), Logger.string('%s', str(invalid_scheme)), Logger.colour('reset', True)]);
            sys.exit();
        
        for scheme in config_file.sections():
            config_scheme_settings = config_file.options(scheme);
            
            validate_config_scheme_settings = config_file.validateSetting(scheme, config_scheme_settings);
            
            result = xcparser.containerForSchemeWithName(scheme);
            if result[0] == True and args.action != None:
                action_func = result[1].actionLookup(args.action);
                if action_func != None:
                    action_item = action_func(result[2]);
                    action_item.performAction(result, xcodeproj, validate_config_scheme_settings);
                else:
                    Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Please supply an action: "build", "test", "analyze", or "archive"'), Logger.colour('reset', True)]);
            else:
                Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Please specify an action with the -a/--action flag'), Logger.colour('reset', True)]);

if __name__ == "__main__":
    main();
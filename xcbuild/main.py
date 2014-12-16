import os
import sys
import argparse
from .developer_tools import *
from .xcparse import *
from .print_utils import *
from .xcbconfigparser import *
from .xcschemeparse import *
# Main
def main():
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-c', '--config', help='path to the build config file', action='store');
    args = parser.parse_args();
    
    xcparser = xcparse(args.filename);
    
    if args.list == True:
        PrintUtils_debuglog([PrintUtils_Colour('black',True), PrintUtils_String('%s', 'Schemes'), PrintUtils_Colour('reset', True)]);
        PrintUtils_debuglog([PrintUtils_Colour('blue',True), PrintUtils_String('%s', '========================'), PrintUtils_Colour('reset', True)]);
        for scheme in xcparser.schemes():
            PrintUtils_debuglog([PrintUtils_Colour('black',True), PrintUtils_String('%s', scheme.name), PrintUtils_Colour('reset', True)]);
        sys.exit();
    
    if args.config != None and os.path.exists(args.config) == True:
        config_file = xcbconfigparser(args.config);
        
        validate_config_schemes = config_file.validateSections(xcparser.schemes());
        if validate_config_schemes[0] == False:
            PrintUtils_debuglog([PrintUtils_Colour('black',True), PrintUtils_String('%s', 'Could not find Schemes with names: '), PrintUtils_Colour('reset', True)]);
            for invalid_scheme in list(validate_config_schemes[1]):
                PrintUtils_debuglog([PrintUtils_Colour('red',True), PrintUtils_String('%s', str(invalid_scheme)), PrintUtils_Colour('reset', True)]);
            sys.exit();
        
        for scheme in config_file.sections():
            config_scheme_settings = config_file.options(scheme);
            
            validate_config_scheme_settings = config_file.validateSetting(scheme, config_scheme_settings);
            
            for project in xcparser.projects:
                if scheme in list(map(xcschemeparseSchemeName, project.schemes())):
                    build_command = 'xcodebuild -project "'+project.path.obj_path+'" -scheme "'+scheme+'" ';
                    for item in validate_config_scheme_settings:
                        build_command+=str(item)+' ';
                    result = developer_tools.make_subprocess_call(build_command, True);
                    print result[0];

if __name__ == "__main__":
    main();
import os
import sys
import argparse
from .developer_tools import *
from .xcparse import *
# Main
def main(argv):
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-c', '--config', help='path to the build config file', action='store');
    args = parser.parse_args();
    
    xcparser = xcparse.xcparse(args.filename);

    if args.list == True:
        print 'Schemes';
        print '========================';
        for scheme in xcparser.schemes():
            print scheme.name;
        sys.exit();

    if args.config != None and os.path.exists(args.config) == True:
        config_file = xcbConfigParser.xcbConfigParser(args.config);

        validate_config_schemes = config_file.ValidateSections(xcparser.schemes());
        if validate_config_schemes[0] == False:
            print 'Could not find Schemes with names: '+str(list(validate_config_schemes[1]));
            sys.exit();

        for scheme in config_file.sections():
            config_scheme_settings = config_file.options(scheme);

            validate_config_scheme_settings = config_file.ValidateSetting(scheme, config_scheme_settings);

            for project in xcparser.projects:
                if scheme in list(map(xcschemeparse.SchemeName, project.schemes())):
                    build_command = 'xcodebuild -project "'+project.path.obj_path+'" -scheme "'+scheme+'" ';
                    for item in validate_config_scheme_settings:
                        build_command+=str(item)+' ';
                    result = developer_tools.make_subprocess_call(build_command, True);
                    print result[0];

if __name__ == "__main__":
    main(sys.argv[1:]);
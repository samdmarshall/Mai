import xcparse
import argparse
import xcschemeparse
import sys
import os
import BSConfigParser
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
        config_file = BSConfigParser.BSConfigParser(args.config);
        
        validate_config_schemes = config_file.ValidateSections(list(map(xcschemeparse.SchemeName, xcparser.schemes())));
        if validate_config_schemes[0] == False:
            print 'Could not find Schemes with names: '+str(list(validate_config_schemes[1]));
            sys.exit();
        
        for scheme in config_file.sections():
            config_scheme_settings = config_file.options(scheme);
            
            validate_config_scheme_settings = config_file.ValidateSetting(scheme, config_scheme_settings);
            
            #print validate_config_scheme_settings;

if __name__ == "__main__":
    main(sys.argv[1:]);
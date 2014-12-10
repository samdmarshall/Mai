import xcparse
import argparse
import xcschemeparse
import sys
import os
# Main
def main(argv):
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-s', '--scheme', help='name of scheme to examine', action='store');
    parser.add_argument('-c', '--config', help='path to the build config file', action='store');
    args = parser.parse_args();
    
    xcparser = xcparse.xcparse(args.filename);
    
    if args.list == True:
        print 'Schemes';
        print '========================';
        for scheme in xcparser.schemes():
            print scheme.name;
        sys.exit();
    
    if args.scheme != None:
        all_schemes = xcparser.schemes();
        found_scheme = args.scheme in list(map(xcschemeparse.SchemeName, all_schemes));
        if found_scheme == True:
            print 'Selecting Scheme \"'+args.scheme+'\"...';
        else:
            print 'Could not find \"'+args.scheme+'\" on \"'+xcparser.name+'\".';
            sys.exit();

if __name__ == "__main__":
    main(sys.argv[1:]);
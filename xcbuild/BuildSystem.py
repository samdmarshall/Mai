import xcparse
import argparse
import sys
import os
# Globals
kVerboseLogLevel = 0;
# Helper Functions
def v_log(message, level, kVerboseLogLevel):
    if kVerboseLogLevel >= level:
        print message;
# Main
def main(argv):
    parser = argparse.ArgumentParser(description='Resolve target dependencies');
    parser.add_argument('filename', help='path to xcodeproj or xcworkspace');
    parser.add_argument('-l', '--list', help='list schemes', action='store_true');
    parser.add_argument('-s', '--scheme', help='name of scheme to examine', action='store');
    parser.add_argument('-v', '--verbose', help='add verbosity', action='count');
    args = parser.parse_args();
    
    if args.verbose == None:
        kVerboseLogLevel = 0;
    else:
        kVerboseLogLevel = args.verbose;
    
    xcparser = xcparse.xcparse(args.filename);
    
    if args.list == True:
        print 'Schemes';
        print '========================';
        for scheme in xcparser.schemes():
            print scheme.name;
        sys.exit();
    
    

if __name__ == "__main__":
    main(sys.argv[1:]);
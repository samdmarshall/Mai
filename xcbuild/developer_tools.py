import os
import sys
import subprocess

class developer_tools(object):
    
    def make_subprocess_call(call_args, shell_state=False):
        error = 0;
        output = '';
        try:
            output = subprocess.check_output(call_args, shell=shell_state);
            error = 0;
        except CalledProcessError as e:
            output = e.output;
            error = e.returncode;
            return (output, error);
    
    def resolve_developer_path():
        platform_path = '';
        xcrun_result = make_subprocess_call(('xcode-select', '-p'));
        if xcrun_result[1] != 0:
            PrintUtils_debuglog([PrintUtils_Colour('red',True), PrintUtils_String('%s', 'Please run Xcode first!'), PrintUtils_Colour('reset', True)]);
            sys.exit();
        developer_path = xcrun_result[0].rstrip('\n');
        return developer_path;
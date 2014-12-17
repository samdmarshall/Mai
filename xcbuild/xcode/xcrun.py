import os
import sys
import subprocess

from ..Logger import *

class xcrun(object):
    
    @classmethod
    def make_subprocess_call(cls, call_args, shell_state=False):
        error = 0;
        output = '';
        try:
            output = subprocess.check_output(call_args, shell=shell_state);
            error = 0;
        except CalledProcessError as e:
            output = e.output;
            error = e.returncode;
        return (output, error);
    
    @classmethod
    def resolve_developer_path(cls):
        platform_path = '';
        xcrun_result = xcrun.make_subprocess_call(('xcode-select', '-p'));
        if xcrun_result[1] != 0:
            Logger.debuglog([Logger.colour('red',True), Logger.string('%s', 'Please run Xcode first!'), Logger.colour('reset', True)]);
            sys.exit();
        developer_path = xcrun_result[0].rstrip('\n');
        return developer_path;
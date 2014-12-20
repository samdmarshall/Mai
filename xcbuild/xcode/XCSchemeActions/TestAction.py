from __future__ import absolute_import

class TestAction(object):
    # contents = {};
    # children = [];
    # selectedDebuggerIdentifier = '';
    # selectedLauncherIdentifier = '';
    # shouldUseLaunchSchemeArgsEnv = '';
    # buildConfiguration = '';
    
    
    def __init__(self, action_xml):
        self.contents = action_xml;
        if 'selectedDebuggerIdentifier' in self.contents.keys():
            self.selectedDebuggerIdentifier = self.contents.get('selectedDebuggerIdentifier');
        if 'selectedLauncherIdentifier' in self.contents.keys():
            self.selectedLauncherIdentifier = self.contents.get('selectedLauncherIdentifier');
        if 'shouldUseLaunchSchemeArgsEnv' in self.contents.keys():
            self.shouldUseLaunchSchemeArgsEnv = self.contents.get('shouldUseLaunchSchemeArgsEnv');
        if 'buildConfiguration' in self.contents.keys():
            self.buildConfiguration = self.contents.get('buildConfiguration');
    
    def performAction(self, container, project_constructor, scheme_config_settings):
        print 'implement me!';
from __future__ import absolute_import

class ArchiveAction(object):
    # contents = {};
    # children = [];
    # buildConfiguration = '';
    # revealArchiveInOrganizer = '';
    
    
    def __init__(self, action_xml):
        self.contents = action_xml;
        if 'buildConfiguration' in self.contents.keys():
            self.buildConfiguration = self.contents.get('buildConfiguration');
        if 'revealArchiveInOrganizer' in self.contents.keys():
            self.revealArchiveInOrganizer = self.contents.get('revealArchiveInOrganizer');
    
    def performAction(self, container, project_constructor, scheme_config_settings):
        print 'implement me!';
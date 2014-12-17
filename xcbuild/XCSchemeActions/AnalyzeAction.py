from __future__ import absolute_import

class AnalyzeAction(object):
    contents = {};
    children = {};
    
    def __init__(self, action_xml):
        self.contents = action_xml;
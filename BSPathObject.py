import os

class BSPathObject(object):
    base_path = '';
    obj_path = '';
    root_path = '';
    
    def __init__(self, path, root):
        self.obj_path = path;
        self.base_path = os.path.dirname(path);
        if root == '':
            self.root_path = self.obj_path;
        else:
            self.root_path = os.path.join(path, root);
import maya.api.OpenMaya as om

class TemplateCmd(om.MPxCommand):
    
    COMMAND_NAME = "TemplateCmd"
    
    def __init__(self):
        super(TemplateCmd, self).__init__()
        
    def doIt(self, args):
        print("Template command.")
        
    @classmethod
    def creator(cls):
        return TemplateCmd()

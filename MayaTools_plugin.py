import maya.api.OpenMaya as om
import commands


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


def initializePlugin(plugin):
    """
    """
    
    vendor = "David Delaunay"
    version = "0.0.0"
    
    plugin_fn = om.MFnPlugin(plugin, vendor, version)
    
    for command in commands.commands:
        
        try: 
            plugin_fn.registerCommand(command.COMMAND_NAME, command.creator)
            om.MGlobal.displayInfo(f"Register command : {command.COMMAND_NAME}")
                        
        except:
            om.MGlobal.displayError(f"Failed to register command : {command}")
            
            
def uninitializePlugin(plugin):
    """
    """
    
    plugin_fn = om.MFnPlugin(plugin)
    
    for command in commands.commands:
        
        try: 
            plugin_fn.deregisterCommand(command.COMMAND_NAME)
            om.MGlobal.displayInfo(f"Deregister command : {command.COMMAND_NAME}")
            
        except:
            om.MGlobal.displayError(f"Failed to deregister command : {command}")

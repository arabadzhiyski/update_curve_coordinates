# Sets the 'coords' parameter of the Curve SOP
# Button callback script: hou.phm().setNewCoords(kwargs['node'])

import hou

def setNewCoords(node):
    inputs = node.inputs()
    target_node = None
    
    if (inputs):
        coords = node.geometry().findGlobalAttrib("coords").strings()[0]
        target_node = inputs[0]
        target_node.parm("coords").set(coords)
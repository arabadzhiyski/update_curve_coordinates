# Thanks for the help Alain2131 from odforce!

this_node = kwargs["node"]
inputs= this_node.inputs()

if (inputs):
    path = this_node.path()
    curve_sop = hou.nodeType(hou.sopNodeTypeCategory(), "curve")
    input_type = inputs[0].type()
    
    switch = hou.parm(path + "/switch/input")
    
    if input_type != curve_sop:
        switch.set(0)
    else:
        switch.set(1)
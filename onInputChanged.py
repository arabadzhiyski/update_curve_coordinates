# Cook the python node which checks the HDA input node type so
# that its error message can propagate upwards.

this_node = kwargs["node"]
inputs= this_node.inputs()

if (inputs):
    path = this_node.path() + "/check_input_type" # Is this the best way?
    
    try:
        hou.parm(path + "/switch/input").set(1) # (Re)set the switch
        hou.node(path + "/check_input_type").cook() # Check input type
    except:
        hou.parm(path + "/switch/input").set(0) # Set switch to error stream
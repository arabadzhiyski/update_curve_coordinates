# Cook the python node which checks the HDA input node type so
# that its error message can propagate upwards.

this_node = kwargs["node"]
inputs= this_node.inputs()

if (inputs):
    path = this_node.path() + "/check_input_type" # Is this the best way?
    try:
        if hou.node(path + "/check_input_type").cook(): # A bit hackish
            hou.parm(path + "/switch/input").set(1)
        else:
            hou.parm(path + "/switch/input").set(0) # Set switch to error branch so HDA won't output anything.
    except:
        None # Don't throw exception to the consol. It's distracting.
# Cook the python node which checks the HDA input node type so
# that its error message can propagate upwards.

this_node = kwargs["node"]
inputs= this_node.inputs()

if (inputs):
    path = this_node.path() + "/check_input_type" # Is this the best way?
    try:
        hou.node(path).cook()
    except:
        None # Don't throw exception to the consol. It's distracting.
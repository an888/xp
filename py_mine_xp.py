import nxbt

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

str_main_loop = """
    LOOP 25
        L R 0.1S
        L R A 0.1S
        0.1S
        L R 0.1S
        L R Y 0.1S
        0.1S
"""

macro = f"""
LOOP 1000
    {str_main_loop}
    DPAD_RIGHT 0.5S
    {str_main_loop}    
    DPAD_LEFT 0.5S
    {str_main_loop}    
    DPAD_UP 0.5S
    DPAD_UP 0.5S
    {str_main_loop}    
    DPAD_DOWN 0.5S
    DPAD_DOWN 0.5S
"""

print(str_macro)


# Run a macro on the Pro Controller
nx.macro(controller_index, macro)
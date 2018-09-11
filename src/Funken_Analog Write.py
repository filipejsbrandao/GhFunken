#########################################################################
##                            COMPONENT INFO                           ##
#########################################################################

"""
Description + license here
-
Provided by Funken 0.1
    Args:
        PIN: Description...
        VAL: Description...
        PORT: Description...
    Returns:
        VAL_OUT: Description...
"""

ghenv.Component.Name = "Funken_Analog Write"
ghenv.Component.NickName = 'AnalogWrite'
ghenv.Component.Message = 'VER 0.3.0'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc
import Grasshopper as gh
import time

def main(pin, value, port, id):
    
    if sc.sticky.has_key("pyFunken") == False:
        check_data = False
        msg = "No serial object available. Have you opened the serial port?"
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Error, msg)
        return
    
    if pin is None:
        check_data = False
        msg = "No pin provided."
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)
        return
    
    if value is None:
        value = 0
    
    if port is None:
        port = sc.sticky["pyFunken"].com_ports[0]
        msg = "No port provided. Port set to " + port
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    if id is None:
        id = sc.sticky['pyFunken'].ser_conn[port].devices_ids[0]
        msg = "No id provided. Id set to " + str(id)
        ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Remark, msg)
    
    comm = "AW " + str(PIN) + " " + str(value) + "\n"
    sc.sticky['pyFunken'].send_command(comm, port, id)
    return port, id

result = main(PIN, VAL, PORT, ID)

if result is not None:
    _PORT = result[0]
    _ID = result[1]
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
ghenv.Component.Message = 'VER 0.1\nNOV_30_2017'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Funken"
ghenv.Component.SubCategory = "0 | Funken"
try: ghenv.Component.AdditionalHelpFromDocStrings = "4"
except: pass

import scriptcontext as sc
import time

if PORT is None:
    PORT = sc.sticky['main_listener'].com_ports[0]

if ID is None:
    ID = 1

comm = "AW " + str(PIN) + " " + str(VAL) + "\n"
sc.sticky['main_listener'].send_command(comm, PORT, ID)

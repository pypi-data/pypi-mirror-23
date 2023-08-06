# -*- coding: utf-8 -*-
"""
Constant variables for radiation_daysim
"""

# Daysism radiation simulation parameters
RAD_PARMS = {
'RAD_N': 2,
'RAD_AF': 'file',
'RAD_AB': 4,
'RAD_AD': 512,
'RAD_AS': 256,
'RAD_AR': 128,
'RAD_AA': 0.15,
'RAD_LR': 8,
'RAD_ST': 0.15,
'RAD_SJ': 0.7,
'RAD_LW': 0.002,
'RAD_DJ': 0.7,
'RAD_DS': 0.15,
'RAD_DR': 3,
'RAD_DP': 512,
}
# Daysim Sensor parameters
SEN_PARMS = {
'X_DIM': 100, # aximum so there is only one point per surface
'Y_DIM': 100, # maximum so there is only one point per surface
'MIN_Z_DIR': -0.85,
'MAX_Z_DIR': 0.05,
}
# terrain parameters
TERRAIN_PARAMS = {'e_terrain': 0.8}

# simulation parameters
SIMUL_PARAMS = {'n_build_in_chunk':50, 'multiprocessing': True} # min number of buildings for multiprocessing # limit the number if running out of memory

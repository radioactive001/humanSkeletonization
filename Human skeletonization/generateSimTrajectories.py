import os
import automarkerlabel as aml

# --------------------------------------------------------------------------- #
# ----------------------------- PARAMETERS ---------------------------------- #
# --------------------------------------------------------------------------- #

# Path to .hdf5 file containing body kinematics of training data
bodykinpath = os.path.join('.','data','bodykinematics.hdf5')
# Path to .xml file of OpenSim marker set
markersetpath = os.path.join('.','data','MarkerSet.xml')
# Path to save .pickle file of training data
outputfile = os.path.join('.','data','simulatedTrajectories.pickle')

# Markers to use to align person such that they face +x. Suggest acromions or pelvis markers.
alignMkR = 'RAC'
alignMkL = 'LAC'
fs = 240 # Sampling frequency of data to be labelled
num_participants = 100 # number of participants to include in training data, must be <=100
max_len = 240 # Max length of data segments


data = aml.generateSimTrajectories(bodykinpath,markersetpath,outputfile,alignMkR,alignMkL,
                        fs,num_participants,max_len)

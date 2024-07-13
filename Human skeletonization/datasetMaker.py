# import numpy as np
from ezc3d import c3d
import os
from io import StringIO
# import glob
# import numpy as np
# import h5py
import automarkerlabel as aml

path=os.path.dirname(os.path.abspath(__file__))

# # Load the C3D data file
# c3dlist = glob.glob(os.path.join(path+"\\data\\c3dFiles",'*.c3d'))


c3d_file_path = path+"\\data\\c3dFiles\\TRAINDATA.c3d"


# pts, fs, labels = aml.import_raw_c3d(c3d_file_path,0)
# print(pts)
# print(labels)
# c3d_file_path = path+"\\data\\c3dFiles\\Data_27_june_06.c3d"
c3d_data = c3d(c3d_file_path)

# Access the motion data from the C3D file
print(c3d_data['parameters']['POINT']['RATE']['value'][0])
# # Assuming motion_data contains the 3D motion data
# mean = np.mean(motion_data, axis=(0, 1))  # Calculate the mean along dimensions 0 and 1
# std = np.std(motion_data, axis=(0, 1))  # Calculate the standard deviation along dimensions 0 and 1
# # Normalize the motion data
# normalized_data = (motion_data - mean) / std
# # Create a new C3D file
# normalized_c3d_file_path = path+"\\data\\c3dNormalized\\Normalized_Data_27_june_06.c3d"
# # normalized_c3d_data = c3d(normalized_c3d_file_path)
# normalized_c3d_data = c3d()
# # Update the motion data with the normalized values

# normalized_c3d_data.add_parameter(c3d_data['parameters'])
# normalized_c3d_data['data']['points'] = normalized_data
# # Save the modified C3D file
# # normalized_c3d_data.write_file()
# normalized_c3d_data.write(normalized_c3d_file_path)





# # Define the directory containing the C3D data files
# c3d_dir =  path+"\\data\\c3dFiles\\"

# # Initialize empty lists to store preprocessed data
# all_motion_data = []

# # Iterate over each C3D data file
# for filename in os.listdir(c3d_dir):
#     if filename.endswith('.c3d'):
#         # Load the C3D data file
#         c3d_file_path = os.path.join(c3d_dir, filename)
#         c3d_data = c3d(c3d_file_path)
        
#         # Get the motion data from the C3D file
#         motion_data = c3d_data['data']['points']
        
#         # Preprocess and organize the motion data
#         # preprocessed_data = preprocess_data(motion_data)  # Implement your own preprocessing function
        
#         # Append the preprocessed data to the list
#         all_motion_data.append(motion_data)

# # Convert the list to a numpy array
# all_motion_data = np.array(all_motion_data)


# # Create a new HDF5 file
# hdf5_file_path = 'path_to_output_hdf5_file.h5'
# hdf5_file = h5py.File(hdf5_file_path, 'w')

# # Save the motion data as a dataset in the HDF5 file
# hdf5_file.create_dataset('motion_data', data=all_motion_data)

# # You can add more datasets as needed
# # hdf5_file.create_dataset('labels', data=labels_data)
# # hdf5_file.create_dataset('timestamps', data=timestamps_data)

# # Close the HDF5 file
# hdf5_file.close()

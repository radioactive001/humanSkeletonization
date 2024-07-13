import os
import automarkerlabel as aml
import numpy as np
import time
import matplotlib.pyplot as plt
import numpy as np
import cv2

path=os.path.dirname(os.path.abspath(__file__)) # get current path to use as default

# File paths
modelpath = os.path.join(path,'data','model_2023-07-16.ckpt') 
trainvalpath = os.path.join(path,'data','trainingvals_2023-07-16.pickle') 
markersetpath = os.path.join(path,'data','markers_final.xml') 
filename = os.path.join(path,'data','Data_27_june_08.c3d') 
output_name = filename[:-4]+'_labelled.c3d'
video_name = os.path.join(path,'data','Data_27_june_08.mp4')

#Parameters
isVideo = True
angle = 0
windowSize = 120 # size of windows used to segment data for algorithm
markers, segment, uniqueSegs, segID, _, num_mks = aml.import_markerSet(markersetpath)
elev=14
azim=39

#Bone pair for skeleton making
bone_pairs = [ ["RHEAD", "LHEAD"], ["RHEAD", "RSHOL"], ["RSHOL", "RELB"],
                   ["RELB", "RHND"], ["RSHOL", "LSHOL"], ["LHEAD", "LSHOL"],["LSHOL", "LELB"],
                   ["LELB", "LHND"], ["RSHOL", "CHST"], ["LSHOL", "CHST"],
                   ["RSHOL", "SPNE"], ["LSHOL", "SPNE"], ["CHST", "STOM"], ["STOM", "RWAST"],
                   ["STOM", "LWAST"], ["SPNE", "RWAST"], ["SPNE", "LWAST"],
                   ["RWAST", "RHIP"], ["RHIP", "RKNEE"], ["RKNEE", "RCLF"], ["RCLF", "RANKL"],
                   ["LWAST", "LHIP"], ["LHIP", "LKNEE"], ["LKNEE", "LCLF"], ["LCLF", "LANKL"]]




#Load the data from c3d file 
outputdata=''
pts=''
fs=''
labels = ''


if (filename is not None):
    if os.path.exists(filename) and ('.c3d' in filename):
        outputdata=filename
        
        print('importing points')

        angle=float(angle)
        pts_c3d, fs, labels = aml.import_raw_c3d(filename, angle)
        
        pts = np.array(pts_c3d, dtype=np.float64)

    elif os.path.exists(filename) and ('.c3d' not in filename):
        outputdata = 'ERROR: File must be in .c3d format'
    else:
        outputdata = 'ERROR: file not found \n%s' % (filename)


#Label Loaded data
labels=''
confidence=''
body_segment=''
comment=''
timestamp=None
if (filename is not None) and (pts != ''):
    pts=np.array(pts) 
    print('finding labels and confidence scores')
    timestamp=time.time()
    labels_c3d, confidence_c3d,_ = aml.marker_label(pts,modelpath,trainvalpath,
                                                    markersetpath,fs,windowSize)
    print('done labelling')
    labels=np.array(labels_c3d)
    confidence=np.array(confidence_c3d)
    body_segment=1
    comment="Labels assigned"


# Get the number of frames and number of points
num_frames = pts.shape[0]
num_points = pts.shape[1]

# Create a plot to visualize the 3D points
fig = plt.figure()
canvas = fig.canvas
ax = fig.add_subplot(111, projection='3d')

#Define points
X = pts[:,:,0] 
Y = pts[:,:,1] 
Z = pts[:,:,2] 

# Set plot limits and labels
max_range = np.array([np.nanmax(X)-np.nanmin(X), np.nanmax(Y)-np.nanmin(Y),np.nanmax(Z)-np.nanmin(Z)]).max() / 2.0 
mid_x = (np.nanmax(X)+np.nanmin(X)) * 0.5  #middle value x, not necessarily 0
mid_y = (np.nanmax(Y)+np.nanmin(Y)) * 0.5  #middle value y
mid_z = (np.nanmax(Z)+np.nanmin(Z)) * 0.5  #middle value z

ax.set_xlim([mid_x - max_range,mid_x + max_range]) # Replace xmin and xmax with appropriate values
ax.set_ylim([mid_y - max_range, mid_y + max_range]) # Replace ymin and ymax with appropriate values
ax.set_zlim([mid_z - max_range, mid_z + max_range])  # Replace zmin and zmax with appropriate values
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=elev, azim=azim)
identified = (labels!='') | (labels!='None')
image_list = []
# Create a scatter plot for each frame
for i in range(num_frames):
    ax.cla()  # Clear the plot for each frame
    ax.set_xlim([mid_x - max_range,mid_x + max_range]) # Replace xmin and xmax with appropriate values
    ax.set_ylim([mid_y - max_range, mid_y + max_range]) # Replace ymin and ymax with appropriate values
    ax.set_zlim([mid_z - max_range, mid_z + max_range]) 
    xData = pts[i, :, 0]
    yData = pts[i, :, 1]
    zData = pts[i, :, 2]
    plot_points = ax.scatter(xData, yData, zData, c='b')
    
    ax.set_title('Frame {}'.format(i))

    for bone in bone_pairs:
        partFrom = bone[0]
        partTo = bone[1]

        if (partFrom in labels) and (partTo in labels):
            idFrom = list(labels).index(partFrom)
            idTo = list(labels).index(partTo)
            ax.plot([xData[idFrom],xData[idTo]],[yData[idFrom],yData[idTo]],[zData[idFrom],zData[idTo]])

    
    # image_flat = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')  
    # image[i] = image_flat.reshape(*reversed(canvas.get_width_height()), 3) 
    # plt.pause(0.001)
    # Convert the plot to an image and save it
    if isVideo:
        fig.canvas.draw()
        data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        image = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        image_list.append(image)
        print(f"Frame {i}/{num_frames} exported.")
    else:
        plt.pause(0.001)




if isVideo:
    height, width, _ = image_list[0].shape
    fps = 60  # Frames per second

    video_codec = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_name, video_codec, fps, (width, height))

    # Write the images to the video file
    for image in image_list:
        video_writer.write(image)

    # Release the VideoWriter
    video_writer.release()

    print(f"Video saved as: {video_name}")
else:
    plt.show()









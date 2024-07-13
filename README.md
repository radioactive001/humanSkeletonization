







Marker-Based Underwater Human Skeletonization


Abstract

Marker-based underwater human skeletonization is a process that involves extracting the human skeleton from underwater video footage using markers. This technique has applications in the study of human movement and biomechanics in aquatic environments. The process involves placing markers on the body, recording underwater video footage, and using specialized software to track the movement of the markers and reconstruct the skeleton. However, challenges such as distortion of the video footage caused by the refraction of light in water can lead to errors in the tracking and reconstruction process. The project dives deeps into leveraging deep neural networks(DNN) to construct human skeletons from 3D reference points, which is done by initial data acquisition using the Qualisys Miqus UW cameras. Thereafter, the collected 3D point data is refined and processed to be used to train the DNN. The DNN predicts the labels of each point in correspond to human body. Using these data a skeletal form is generated for the captured data.




















Introduction 

In the fields of biomechanics, forensic science, and sports sciences, the extraction of human skeletal information from underwater video footage is a significant issue. Researchers and practitioners have carefully looked for answers to address this complex conundrum over time, leading to the birth of a range of strategies designed to get around this obstacle. One of these techniques, the marker-based underwater human skeletonization methodology, has shown to be very successful. This innovative method is based on the strategic positioning of discreet markings on the human body in crucial locations that will act as key reference points. After placing the markers, underwater video footage is carefully taken to show how these markers interact with one another as they move through the aquatic environment. These subtle yet significant characteristics serve as the foundation for a reconstruction procedure that reveals the submerged human skeleton.

This method's core strength is its capacity to derive exact skeletal information from the motions of the markers. The movement of the human body across the water is traced by these marks. The underwater cameras used to record their movements provide the crucial information required for the subsequent reconstruction of the skeleton, thereby resurrecting the complex network of bones, joints, and connective tissues that comprise the human body.

This method has ramifications for a wide range of scientific studies. Researchers may analyze and understand human motions in aquatic environments by using the reconstructed skeletal information as a strong lens. Every stroke and pivot made by swimmers, divers, and athletes can be analyzed in detail. A new age of sophisticated training approaches enhanced by knowledge gained from the underwater world is introduced by this thorough examination.

The marker-based underwater human skeletonization method looks with interest at the biomechanics of aquatic creatures in addition to human dynamics. The delicate movements of marine life are shown via the prism of this approach, illuminating the mysteries of movement below the water's surface. New perspectives and sources of inspiration open up when researchers analyze the behavior of aquatic animals, possibly affecting subjects like biology and robotics. The method assumes a function of utmost significance in the field of forensic investigations. In situations of drowning victims, the submerged human skeleton, which was recreated from the movements of markers, is essential. The detailed analysis of the recorded movements by forensic professionals aims to untangle the record that contributed to the catastrophe, perhaps revealing crucial information that sheds light on the course of events and the cause of death.

The marker-based method stands out from competing underwater human skeletonization approaches, notably silhouette-based ones, by providing a wide range of benefits. The marker-based technique shines as a beacon of accuracy, whereas silhouette techniques may fail to accurately capture the subtleties of physical movement. An incredibly detailed map of joint angles and velocity is created by the markers, each of which is a distinct motion. This meticulous depiction, comparable to a work of art, overcomes the restrictions imposed by backdrop complexity and water visibility to provide a comprehensive perspective of human dynamics below the surface of water. The process of marker-based underwater human skeletonization is not without its difficulties, though. The video clip is distorted as a result of refraction when light passes through the water's surface. The accuracy of marker tracking and subsequent bone reconstruction are gravely threatened by this refractive distortion. Refraction-induced data introduces an element of uncertainty, necessitating the correction and improvement of data quality. 

Additionally, the implementation of this approach necessitates the fusion of specific tools and knowledge. A symphony of technical skills is required for the coordination of marker placement, video recording, and data processing. In order to ensure that the film acquired accurately depicts the markers' complex paths, underwater cameras must be precisely adjusted. The use of such equipment makes the process a project that requires devoted time, funds, and staff. It also demands the requirement for specialist knowledge.

Despite the difficulties, there is a renaissance of innovation taking on in the field of marker-based underwater human skeletonization. An increase in interest in recent years has sparked the creation of new approaches and the improvement of old ones. The trajectory of technology has undergone a radical change as a result of the constantly increasing frontiers of computer vision and machine learning. Deep learning algorithms and neural networks show strong promise, ready to reduce the impacts of refraction-induced distortion and improve marker tracking precision. These developments ignite a ray of optimism by having the ability to open up new spheres of accuracy and fidelity.

The study of human movement has been revolutionized by passive motion capture systems, which use a variety of infrared cameras to precisely track the three-dimensional locations of retroreflective markers. The inability of these technologies to immediately link the collected coordinates with particular physical markers is an inherent problem, though. This requires the necessary marker labeling procedure, which is a vital step in determining the anatomical relevance of each marker within the collected data. The task involves creating a seamless connection among three-dimensional coordinates and their related labels in the world of motion capture. The goal of this complex problem is to find an injective mapping that connects the locations of the markers to a list of labels that describe their anatomical identity, such as significant anatomical landmarks. In this idealized scenario, the motion capture data would elegantly connect motion to anatomical context by morphing into a cohesive picture of the human body's movement.

However, the reality of motion capture presents difficulties that contradict this idealized scenario. The recorded data could contain extraneous markers, sometimes referred to as "ghost markers," which are caused by reflection artifacts or markers that unintentionally enter the cameras' range of view. Similar to ghost markers, these markers add uncertainty to the mapping process since their coordinates move that is discordant and does not match any established label. An additional layer of complexity is added by the fluctuation of motion that occurs naturally in aquatic environments. Physical markers may occasionally, despite their careful placement, be briefly obscured from the cameras' field of vision by occlusions, leaving their labels blank for those brief intervals. The dense web of intricacy created by this dynamic interaction between visibility and occlusion may make it difficult to understand the motion capture.

When noise taints the data with its unexpected patterns, and occlusions shed fleeting shadows on markers' identities, the process of marker labeling unfolds as a challenging and time-consuming task. These layers of difficulties craft a story that closely reflects the motion capture industry's practical reality, where accuracy is frequently overshadowed by the subtleties of real-world intricacy. These challenges combine with the particular distortions that the underwater environment introduces in the world of underwater motion capture, where fluidity rules and markers must cross water currents. The subtle distortion of the collected images caused by the refraction of light via water might make marker identification much more difficult.

The complex process of marker labeling and its many-faceted difficulties set the setting for an intriguing inquiry as underwater motion capture is further analyzed. The strategies and advancements that have been developed to overcome these obstacles are revealed in the sections that follow. This deeper exploration culminates in the conversion of motion data collected from motion sensors into a logical and insightful representation of human movement beneath the waves.

The marker-based underwater human skeletonization method is a testament to human inventiveness; it provides a glimpse into the complex web of human motion hidden beneath the water's surface. Due to its versatility and capacity to decipher skeletal information from the cryptic movement of markers, it has a significant impact on the fields of biomechanics, forensic research, and sports sciences. The method offers the potential to revolutionize the understanding of aquatic movement as it navigates the currents of difficulties and embraces the tide of breakthroughs, ushering in a new era of discovery and insight under the water's surface.





























Previous Art


As shown by G. B. Guerra-Filho et al., optical motion capture (OMC) uses synchronized cameras to rebuild body posture from markers, while motion capture records real-world movement using 3D Cartesian coordinates. Techniques they used included data refining, tracking, marker triangulation, and camera calibration. Joint angles are computed using hierarchical models, and motion data are improved using methods such as volumetric reconstruction, inverse kinematics, and editing [1]. The effectiveness of this procedure, however, may be unsuccessful under certain circumstances. First off, a poor frame rate might jeopardize the marker labeling process' accuracy. If the frame rate isn't high enough, crucial times of marker movement or visibility may be lost in between frames, interfering with the smooth propagation of the label. Second, difficulties in appropriately associating labels with individual markers arise in situations when there is a dense arrangement of markers. The closeness of the markers in the set might cause confusion and false identification, which can cause labeling mistakes to spread to the following frames.

Another level of intricacy is added by the existence of "ghost markers," which are visual abnormalities such as reflection artifacts. These fake identifiers don't match to real objects, which causes difficulty while labeling. These ghost markers propagate mistakes forward in time when they are wrongly linked to labels, leading to problems across the whole motion capture session. Additionally, the constantly changing underwater environment might result in marker occlusion, in which marks periodically vanish and then later resurface for a variety of reasons. These label continuity disruptions caused by occlusion occurrences might result in mismatches and misalignments that echo over successive frames. Issues with slow frame rates, crowded marker layouts, ghost markers, and occlusion-reappearance dynamics can all affect how well markers are labeled. The importance of solving these problems rests in preventing mistakes from growing worse over time and preserving the accuracy and dependability of the motion data that has been acquired. As the area develops, methods for improving frame rates, fine-tuning marker placements, reducing ghost markers, and taking into account occlusion phenomena continue to be essential for improving the accuracy and legitimacy of automated marker labeling approaches.

Skeleton models have been included by researchers as a tactical solution to improve accuracy in response to the difficulties faced by marker labeling. These models assist in locating and confirming marker placements by utilizing skeletal features and their innate interactions between markers. This inclusion serves as a useful reference to reduce mistakes brought on by occlusions, ghost markers, and other complications inherent to the motion capture process in addition to providing a systematic framework for marker assignment [2][3].

An initialization pose or movement is frequently needed as a starting point for producing or scaling the model to meet each participant's particular characteristics in order to use skeleton models for marker tagging. The participant's body proportions and joint orientations are in line with this starting position, which acts as a reference configuration. The skeleton model is calibrated in this way, making subsequent marker assignments more precise and pertinent to the individual's anatomical structure.

Initialization entails setting up a virtual representation that closely resembles the subject's actual positioning by lining up the virtual skeleton with the participant's first posture or movement. This step is essential to ensuring that the marker labeling that follows precisely matches the participant's unique skeletal characteristics. Additionally, by including an initialization stance or movement, the skeleton model may adjust to differences in participant body types, joint angles, and limb lengths. This adaptability makes sure that the marker labeling procedure continues to be exact and consistent even when participants display different physical characteristics or movement patterns.

Researchers have looked into statistical approaches like graph matching and Gaussian mixture models as viable remedies in the effort to overcome the challenges of marker labeling [4][5]. These methods automate labeling and minimize manual involvement by using statistical analysis to build relationships between markers and their related labels.The process of building a graph representation of the marker data, where nodes stand in for the markers and edges show connections between them, is known as graph matching. The method attempts to discover an ideal alignment that optimizes the similarity between the graph structure and the anticipated marker labels by recasting the labeling issue as a graph-matching problem. Although graph matching is a promising approach, it has shown sensitivity to cases of marker occlusions, which occur when markers are momentarily hidden from view because of movement or other circumstances. These obstructions can prevent the graph from accurately aligning, which can result in incorrect labeling and decreased accuracy.

Similar to this, Gaussian mixture models employ probabilistic analysis to group markers according to statistical patterns found in the data. This method relies on the presumption that markers in the same cluster have comparable traits, making it easier to recognize and categorize them correctly. However, Gaussian mixture models have shown to be susceptible to marker occlusions, exactly as graph matching. The statistical patterns might be distorted and misclassification can result from the existence of occluded markers, which reduces the technique's overall effectiveness.

Recent efforts have embraced the transformational potential of machine learning to change automated marker tagging. Researchers have tapped into cutting-edge developments by converting the complex 3D marker coordinates into a depth picture format, as demonstrated by Han et al. [6] and Rosskamp et al. [7]. They used convolutional neural networks (CNNs), a kind of deep learning algorithm skilled at picture interpretation, to automate the marker tagging procedure by utilizing this representation. This method makes use of CNNs' ability to identify patterns and correlations in visual input, allowing them to deduce the meaning of markers in terms of anatomy and give the proper labels.

Ghorbani et al. [8] adopted a distinctive yet creative strategy and offered a fresh viewpoint on the issue. In order to retrieve the proper ranking of a shuffled marker set, they presented the marker labeling problem as a puzzle. They used the idea of permutation learning, a branch of machine learning specifically designed for figuring out sequences and permutations, to solve this challenge. Ghorbani and colleagues successfully achieved automated marker identification by considering the marker arrangement as a shuffled sequence and using permutation learning techniques to uncover the original marker order.

These innovative initiatives highlight how machine learning is revolutionizing marker labeling operations. Researchers are in a position to improve the precision, effectiveness, and resilience of marker labeling procedures by using the capabilities of neural networks and creative issue framing. The discipline has the possibility of opening new doors for understanding human movement and anatomical dynamics in great detail as the synergy between machine learning and motion capture develops.

Jiménez Bascones and colleagues [9] explored the world of machine learning in the area of marker labeling, using the AdaBoost algorithm as their compass. This method, which excels in ensemble learning, was used to plan the selection of the best possible group of weak classifiers. These classifiers were purposefully created to exploit the complex geometric connections between markers in a motion capture scenario. The Adaboost algorithm created a composite classifier by studying these geometric interactions, which may then assign suitable marker labels depending on the interconnectedness of markers within the recorded data.

This particular project uses a technique by Allison et al. [10] where labeled data is leveraged to achieve a deep neural network capable of predicting the label of a point. However, one significant limitation of machine learning-based approaches must be acknowledged. Machine learning has the potential to speed up marker labeling jobs significantly, but this depends on having access to a sizable corpus of precisely labeled data. This data serves as the basis for training and fine-tuning the machine-learning model. A new model is required for each different marker set, and the usefulness of these models depends on the quantity and caliber of the training data they are fed. This labeled dataset requires precise work, professional annotation, and a large time and resource commitment to put together.

The requirement for a large amount of labeled data highlights a significant obstacle for machine learning-based techniques for marker tagging. Obtaining a sizable and well-annotated dataset can be a challenging task, especially in situations involving several marker combinations or unique locations. In order to successfully blend computational innovation with data-driven realism, researchers must balance the intrinsic strength of machine learning with the practicalities of data collecting.





















Methodology

Motion Capture System: The Offshore Safety and Survival Center, a vital part of Memorial University's acclaimed Marine Institute, served as the site for the data gathering phase. Dr. Stephen Czarnuch, who oversaw the project, was essential in directing and assisting the study all along the way.

The state-of-the-art Qualisys Underwater Motion Capture System precisely records and captures underwater motion using underwater cameras and proprietary tracking software. These cameras, which were designed to survive underwater difficulties, perform in challenging and dynamic underwater situations and provide data of the highest caliber. Notably, Qualisys is the only manufacturer of commercially accessible optical motion capture cameras for underwater applications.

The precise installation of the Qualisys Underwater Motion Capture System was necessary to start the data collecting. Seven Qualisys Miqus underwater cameras were installed in seven different locations around the four-meter-deep pool. The accuracy and dependability of the motion data were guaranteed by these advanced cameras, which were designed specifically for underwater operation.

Reflective spheres were applied to various locations on the diver's body as part of the motion capture procedure. The Qualisys cameras were able to accurately capture and keep track of the diver's movements in real-time thanks to these reflective markings, which served as tracking points.

Data collection was carried out using the Qualisys Tracking Manager (QTM) program once the system had been set up and the reflective markers had been placed. This program, which was designed explicitly for Qualisys systems, enabled tracking and analysis capabilities. The cameras carefully observed the location and orientation of each reflected orb as the diver moved through the water, resulting in a large 3D dataset that finely represented the diver's underwater movements.

The final dataset, which was put up in the recommended C3D format, provided a plethora of priceless insights. Each reflecting marker was given precise 3D coordinates and motion routes, allowing for the careful investigation and delineation of the diver's kinematics. Researchers might analyze the data to find subtle differences in swimming styles, posture, and other important kinematic factors.

A pioneer in underwater motion capture technology, Qualisys' Miqus underwater cameras are a shining example of state-of-the-art engineering. These cameras were carefully created and constructed with the specific goal of following reflecting orbs beneath the water's surface. They play a function that is nothing short of brilliantly planned in the watery setting where motion capture is done. With an acute awareness of the relevance of their positioning, Qualisys crafts a painstaking arrangement that guarantees the flawless execution of thorough motion tracking.

These cameras are strategically placed in a pool that has been expertly planned. With a specific goal in mind, each camera moves into place around the aquatic environment at its allotted location. The choice of the quantity and configuration of these specialized devices is guided by this goal, which is frequently defined by the particular requirements of the research or application at hand. The complex patterns of aquatic motion are collected and weaved into usable data using this strategic location as the canvas.

The key to proper data collection is where the Miqus underwater cameras are placed. Their placements are carefully chosen and deftly adjusted to record the subject's motions from a variety of perspectives. These cameras capture the subject's aquatic movements from many angles, resulting in the trifecta of accuracy, dimensionality, and precision. This three-dimensional viewpoint helps to capture the precise core of the subject's aquatic expertise by transforming their dynamic movements into a unified digital picture. Additionally, the placements ensure maximum visibility of the markers.

However, these camera placements and angles have importance that goes beyond simple geometry. They are carefully selected to maneuver the intricate detection of occlusions or those instances when the subject's actions could be momentarily hidden. By carefully selecting angles, it is hoped to reduce these occlusions and preserve as much accurate and complete data as possible. Additionally, the strategic placement of the cameras demonstrates Qualisys' dedication to capture the most crucial elements of the diver or swimmer's action. It aims to capture each subtle movement, giving academics, professionals, and practitioners a comprehensive insight into the aquatic movements.

A crucial stage takes place prior to starting the data collection project: the calibration of the underwater camera system. The foundation of the system is established by the calibration procedure, which carefully establishes spatial correlations between the individual cameras. This foundation of accuracy is vital for reconstructing the subject's motions later in the vast three-dimensional space. Calibration is a crucial step that converts camera data into concrete, real-world coordinates, enabling a smooth conversion of filmed motion into an understandable account of aquatic motion.


This quest for accuracy puts a specific toolbox in the limelight. This toolkit, which was created exclusively for calibration, contains two basic elements that each play a crucial part.

The L-frame, a crucial geometrical construction, stands up as the first shining example. The L-frame, which is situated in the center of the watery area, is armed with marker orbs and ready for the camera system's attention. This complicated unfolds to reveal the origin of the space at the center of the monitoring system, from whence all measurements originate.

To complement this, the calibration step begins as the tracking wand becomes center stage. This process is done by the Qualisys Track Manager (QTM) software, a specialized tool created for the world of motion capture. The tracking wand orchestrates a series of motions inside the vision of the cameras as it pirouettes close to the L-frame with accuracy as its guiding star. This spatial symphony completes the calibration process with the accurate capture of the L Frame in the watery environment.

Ultimately, the calibration process uses  motions from the calibration tool and its size to compare with the L-Frame to construct a working space where motion can be tracked and size can be determined by the toolkit's strength. This serves as the canvas for the motion capture creativity to be engraved. Each motion-captured component is suffused with precision and authenticity thanks to a careful symphony of geometry and technology. The world of underwater motion capture is ready for a symphony of precision, as motions transcend the aquatic environment to build a harmonic tale in the language of data, as the stage is prepared and the toolkit's components come together.



Fitting Markers: A constellation of reflecting markers, like bright spheres, are tenaciously attached to certain anatomical landmarks on the subject's body in order to track and record the subject's complex motions. These marks, made from substances with the extraordinary capacity to reflect light, become recognizable beacons under the watchful eye of the cameras. The planning of marker placement follows well-established rules that are smoothly woven into the motion analysis's biomechanical foundation.


These nodes of significance—joints, body segments, and other critical junctures—are deliberately marked with marks that resemble shining points. The creativity inherently present in motion tracking is demonstrated by this precision-driven positioning. A combination of technical skill and anatomical knowledge is employed to orchestrate the movement with accuracy.

Beyond their appearance, these markings serve as crucial points of reference. Their presence initiates a complex synergy with the on-guard cameras. The cameras follow each marker's path throughout the motion-capturing session. Each delicate sway, each subtle turn, and each glide are tenaciously captured, creating a digital version of the aquatic motion.

The swimmer/diver turned into an object of study on which 21 marks were deliberately put in the waters. Each marker found its place in various areas of the body, each one a powerful testament to accuracy. This arrangement provided a bird's-eye view of the diver's aquatic movement, each movement being meticulously captured. This marker ensemble not only made it easier to extract exact movement data but also made the work of annotating the canvas of unmarked data simple.



Data Capture: The stage is set for the subject's underwater immersion and the subsequent data collection endeavor once all the intricate parts of the tracking system have been set up, with the cameras placed with calculated precision, markers securely attached to the subject's body, and the calibration process fine-tuned to completion. 

The diver begins a graceful series of precise motions as soon as they enter the underwater, which is carefully highlighted as the study's primary focus. The elegant undulations of strokes, the remarkable depths of diving, and even the interesting T-posing beneath the water's surface are all shown in this aquatic motion. Every delicate ripple and beautiful arc in this aquatic dance finds its archival home under the critical eye of the underwater cameras.



With a vast array of advanced tracking tools at their disposal, these submerged subject begins performing a series of movements. Their fixed attention is drawn to the reflecting markers positioned on the subject's profile. These markings, which resemble guiding stars, settle deliberately on joints, segments, and locations of considerable fascination, drawing the cameras' close attention.


The cameras focus with accuracy on the iridescent markers, whose luminance is reflected by the water. Each marker's precise three-dimensional coordinates are determined by the cameras working in unison to create a big triangulation that results in a temporal symphony. This symphony, which is performed in real-time, results in a lively data stream that changes in time with the subject's aquatic movement.

A quick series of videos is captured when the subject sets out on their watery voyage. Similar to temporal snapshots, these frames capture the subject's location and orientation at specific times. These shots are seamlessly combined to provide a visual trail that captures the subject's underwater journey as a concrete collection of documented moments. This tapestry of events, this symphony of frames, builds the foundation for all later analytical efforts.

The essential part of the data collected during this crucial period is contained in this collection of unmodified data. Each shot that is taken plays a significant part in the next steps, coordinating the precise positioning of markings on the subject's shape. The foundation for next analysis, ready to unfold the subject's aquatic stance in detail, is laid by this data.



The raw data collected during this section essentially consists of a detailed locations of marker coordinates that have been precisely mapped out in three dimensions and resulted in the C3D file format. This format is a digital archive. Unmarked coordinates in this C3D file find their resonance and weave together to highlight the diver's underwater movements.

Data Cleansing: The data gathered contain varying levels of noise in each frame of the dataset, which may jeopardize the accuracy of the deep learning algorithm's training. Data cleaning must be done in order to maximize the model's training accuracy and avoid this from impacting the training process. A case with noisy data is used to demonstrate this procedure.

The subject, a diver, is shown in the photograph in Fig 9 poised at the water's surface. The diver's presence on the pool's surface causes more noticeable waves and ripples than they originally appeared to. The motion-capturing attempts are presented with a dynamic challenge by these disturbances on the water's surface. Light being reflected and refracted on the water's surface is identified by the motion-capturing system as a reflective orb, which is not constant. These points flicker in and out of existence; these are known as “Ghost Markers” and represent as another layer of challenge. 



The marker coordinates linked to the subject's body in the aquatic environment are represented as a three-dimensional image that is obtained in Figure 9. This makes it possible for us to observe the subject's lower body in this watery setting. Due to their extraordinary sensitivity, these ghost markers appear. However, this introduces a complicated situation where it becomes extremely difficult to discern between the subject's motion and the water's surface.

While these recorded surface reflections do demonstrate the accuracy of the underwater camera system, they also cast doubt on the reliability of the data. The subject's actual motion and what seems to be a collection of unlabeled points within the recorded data might occasionally be difficult to distinguish when using the three-dimensional coordinates produced from these reflections.

Figure 10 shows that the undesirable noisy data remains trapped on the pool's surface even after the subject dives underwater. The data is inappropriate for immediate use due to the significant flood of unlabeled points caused by these surface reflections. When applying deep learning models, which are designed to identify patterns and extract features from datasets, which forces to navigate a more complex environment.

Clarity and accuracy are of utmost significance while developing the complex deep learning model for underwater motion analysis. The model thrives on accurately annotated data points that depict the subject's actual motions. The large number of unlabeled points, which are sculpted by the interaction of light and water, present a layer of disturbance that may make it difficult for the model to precisely estimate joint and bone motions, leading to inaccurate results.



These collected data must go through a rigorous data-refining procedure before they can be used to train the deep learning model designed for this complex underwater motion analysis. This involves painstakingly locating and isolating real marks on the subject's body, which successfully reduces noise caused by the interaction of light and water.

The dataset will be improved using a deliberate technique, making it ready for in-depth study. This entails identifying a certain area of the data that has the least amount of noise interference. Deliberately lowering the level is a wise choice when trying to reduce noise. Although it can result in a smaller pool of training data, this is significant since it allows the dataset to be compressed for better management and insights.

This focused data subset stands out as the best result of the motion capture. Its usefulness is increased by the lack of the distortions that are frequently present in surface reflections on a pool, which enables a finer interpretation and manipulation of the subject's real motions.

The curation process results in two key benefits. First, it produces a focused subset of data with increased analytical accuracy due to an enhanced signal-to-noise ratio. Second, it simplifies the entire dataset, fostering effective computing techniques and analytical approaches.

This strategy emphasizes the superiority of quality over quantity alone. The integrity of the analytical efforts is ensured by the careful selection of largely noise-free data, thereby removing undesired training data. This method leads to a more in-depth examination of the subject's actual motion, free of distortions brought on by the surface.



In short, this approach creates a harmonic interplay between human judgment and technological advancement. The 21 markers' coordinates are guaranteed to be included in the data using this procedure. From the entire dataset, eight succinct data clips were produced. The example figure shown in fig 11 serves as an illustration of how a simplified and polished dataset may look.

OpenSim Model: To remedy errors during deep learning network training, an OpenSim Skeleton model is employed. It resembles producing a unique replica of the markers used by the subject or diver. This digital model aids in enhancing the deep learning network's output. With several pieces that stand in for bodily components, including the pelvis, thigh, shank, and foot, this model is a lot like a jigsaw. Together, these components allow the model to move in a realistic manner.

Markers were placed on this model in the same locations as they were on the subject or diver. These marks serve as sort of indicators that explain the motions of the divers. It offers direction for comprehending how things move underwater. In general, the OpenSim model has three characteristics:

The OpenSim skeleton model is fundamentally made up of a number of segments, each of which is a digital depiction of a distinct bodily part. The complicated and complex motion of the body's anatomical divisions is embodied in these segments. The building blocks of the model's motion dynamics, such as the pelvis, thigh, shank, foot, and others, are carefully characterized.

Joint Connectivity: The OpenSim skeleton model's segments function as separate parts that click into place. Joints, which resemble the body's hinges, are used to bind these sections together. To make the model move similarly to how human bodies move organically, these joints are placed in specified locations. The model appears to be moving naturally thanks to these joints, much like a genuine human would. They keep things realistic by modeling the human body's flexibility and range of motion. Each joint can bend and move in numerous ways, similar to how it may twist and spin. This captures all the minute details of the subject's motions while they are submerged, conserving their mobility.

Marker Positioning: Special markers that fit on the OpenSim skeleton model can be added. To better comprehend mobility data, these markers were thoughtfully put in the same locations as those of the subject. They act as a kind of digital landmark, bridging the digital model and the subject's or diver's movements in the real world. The acquired movement data will accurately match the digital model if they are placed in the proper locations. 

This model aids in correcting deep learning network errors. These annotated markers can aid the network in correcting output faults because the data is unlabeled. It is enhanced by the markers to better reflect the subject's or diver's actual motions. The labeling of the OpenSim markers will aid the deep learning network in ensuring that it connects the appropriate markers to create a skeleton for the dataset. 


Pre-Processing Data: Several preparation steps were used to get the data ready for neural network input. The diver's orientation was initially aligned to the positive x-direction when the marker coordinates were first rotated around the vertical axis. In the training data, this rotation was carried out automatically based on acromion markers, but for the test data, user input was needed to approximate the rotation angle and align the data. Trajectory signals were low-pass filtered using a zero-phase second-order 6Hz Butterworth filter to improve data smoothness. Linear interpolation was used to fill in any gaps in the data that were less than 12 frames long. The marker trajectory data was then divided into windows, each of which had 120 frames for the test and validation data. The final window size was altered when the frame count wasn't divisible by 120 unless there were 12 or fewer frames left, in which case they were added to the window before them.

The window length for the training data fluctuated arbitrarily between 12 and 240 frames. The neural network needed to be able to handle windows of various sizes so that it could be ready for markers with various window sizes, which are normally present in the final window of each marker's trajectory.

The OpenSim marks that were the most apparent across the window were kept when there were more markers than were necessary for labeling. The OpenSim markers that were closest to the marker of interest were picked if numerous markers had equal visibility. The mean position of the maintained markers was used to fill in any gaps in the retained marker trajectories.



Deep Nural Network: A deep learning network can be successfully trained by combining the training dataset with the annotated skeleton model. The training dataset contains the wide variety of motions that a diver made, and the markers placed on the skeletal structure imitate the arrangement of a diver's body. The combined training strategy works together to provide the deep learning model the ability to recognize and correctly classify each marker. These designated indicators are then cleverly used to deduce the posture from the raw motion capture data.

A neural network design based on Long Short-Term Memory (LSTM) units was used to achieve this. A particular subset of recurrent neural networks (RNNs), LSTMs are skilled at handling long-term dependencies and maintaining knowledge across lengthy periods. Number of frames for each window is varied from 12 to 240 frames. With this intentional variance, the neural network is exposed to windows of various widths, specifically accommodating the last window of each marker. This strategy takes into account situations where there are 12 or fewer frames left.

The model's architecture consists of three successive LSTM layers, each of which has 256 cells and a dropout rate of 0.17. A fully linked network with 128 nodes connects these levels together. Notably, the network's iterative learning process is supported by a learning rate of 0.078.

The annotated skeletal model and the training data are processed using this painstakingly created neural network setup, which is based on LSTM units. The program learns to identify markers, assign precise labels, and finally extrapolate the underlying posture hidden inside the unmarked motion capture data through a well-planned training procedure.

Label assignment and skeleton making: For each window, the neural network output generated a vector of dimensions 1xNlbl that contained the probabilities related to the precision of each potential label. The strategy required segmenting trial marker data at frames where markers appeared or disappeared in order to create new windows. By ensuring separate marker labels for each window, this segmentation technique improved accuracy.
The complicated problem of possible label division spanning trajectories was addressed by approaching the assignment of labels to windows as an imbalanced assignment problem. A weighted bipartite graph was used to carry out this, and the Hungarian method was used since it is good at attaining optimal label assignment. The weighted mode was used to define a single label for the whole marker trajectory in order to achieve consistent labeling. Notably, probabilities were given weights, and situations where labels for markers that were simultaneously visible were duplicated were fixed by keeping the marker with the highest likelihood.
In relation to markers associated with certain body segments, the OpenSim marker set acts as a reference for local coordinates. This trait is used to identify incorrectly labeled markers. Mislabeled markers can be found by calculating the distances between markers attached to the same body segment and then comparing them to the training dataset. If markers on the same segment differ by more than three standard deviations from their counterparts in the training set, the assigned label is revoked.


Unmarked markers are given labels based on mean probabilities and distances from other markers that are within three standard deviations in order to achieve exact labeling. The marker is left unmarked if this requirement is not satisfied. Lastly, an effort is made to assign labels to body segments using the marker set, especially in cases where at least three markers are found, albeit some may still be unmarked. This comprehensive strategy highlights the importance of precise marker labeling, especially in difficult situations, eventually improving the precision and dependability of recorded motion data.

The creation of a skeletal framework by the connection of precisely identified markers according to their anatomical correlations is a critical step. The development of bones within the skeleton structure results from this interaction between markers.

The comparison of each pair of connections within the context of the labels given to each frame is required in the next stage. The connection is made, creating a link inside the skeleton if appropriate pairings are found. In contrast, a pair is skipped over or removed if it lacks correspondence.

This process is methodically carried out for each picture, making it possible to create a detailed 3D skeleton showing the subject's motions beneath the water's surface. This complex web of relationships visually represents the subject's posture and motion dynamics while also outlining the underlying skeletal structure.






Problems and Challanges

Refraction and Distortions: The refraction of light in water can distort the appearance and position of markers, leading to inaccuracies in the captured motion data. This refraction effect can be particularly pronounced near the water's surface, introducing errors in the spatial relationships between markers and hindering the accurate reconstruction of skeletal movements.

Surface Interference: Surface disturbances, such as waves and ripples, can introduce noise and inconsistencies into the captured motion data. These disturbances can create unwanted marker reflections and alter the appearance of the subject's movements, making it challenging to extract accurate skeletal information.

Visibility and Occlusions: Water can reduce visibility, especially in murky or turbulent conditions. This reduced visibility can lead to occlusions, where markers are obscured from view by other body parts, equipment, or water elements. Occlusions hinder the accurate tracking of markers and can result in incomplete or inaccurate skeletal representations.

Marker Displacement: Water currents and turbulence can displace markers from their intended positions on the body. This displacement can occur rapidly and unpredictably, leading to marker misalignment and introducing errors in the skeletal reconstruction.

Reflection Artefacts: Light reflections off the water's surface can create ghost markers or false marker detections. These artifacts can confuse the tracking system and result in erroneous skeletal representations.

Complex Biomechanics: Underwater motion involves complex biomechanical interactions between the body and the surrounding water. Buoyancy, hydrodynamics, and resistance can affect movement patterns and joint angles, making it challenging to accurately model and interpret skeletal motion.

Equipment and Setup: Setting up underwater motion capture systems requires specialized equipment and expertise. Ensuring proper waterproofing, camera calibration, and marker attachment can be technically demanding, and any equipment malfunctions or calibration errors can impact data quality.
Data Processing: The high dimensionality of 3D marker data and the complexities of underwater motion require sophisticated data processing and analysis techniques. Handling large volumes of data and mitigating noise while accurately reconstructing the skeletal motion pose computational challenges.

Limited Validation: Due to the underwater environment's unique challenges, validating the accuracy of the captured skeletal data can be difficult. Ground truth measurements and validation techniques commonly used in terrestrial motion capture may not directly apply.

Modeling Assumptions: Skeletal models used for motion analysis are often based on terrestrial biomechanics and may not fully account for the nuances of underwater motion. Adaptation and validation of these models for underwater conditions are essential but can be complex.























Conclusion

To sum up, the study of underwater human motion analysis is an intriguing but challenging field that combines the difficulties of biomechanics, technological development, and data processing. In order to solve the riddles of motion beneath the water's surface, optical motion capture devices, like the Qualisys Underwater Motion Capture System, have become vital. This enables recording and recreating human motions using these systems' specialized cameras and markers, which offer important insights into a variety of domains.

This endeavor does provide some difficulties, though. The very nature of the aquatic environment poses special challenges, from the influence of surface disturbances to the distortion of markers owing to light refraction. Accurate motion capture is challenging because of occlusions, noise, and the dynamic interaction of light and water. A multifaceted strategy combining cutting-edge technology, thorough calibration, and cutting-edge algorithms is required to tackle these problems.

Precision is required for marker tagging, a crucial step in the motion capture pipeline, in order to link measured coordinates with certain anatomical landmarks. Traditional approaches utilize skeletal modeling and manual labeling, although significant advancements have been made by using machine learning strategies. Marker labeling has been automated using convolutional neural networks, statistical methods, and deep learning architectures. Despite the necessity for a large amount of labeled data, these methods provide intriguing ways to improve accuracy and effectiveness.

Furthermore, considerable curation and refining are required in order to translate raw motion data into insightful information. To extract useful patterns and trends, it is necessary to clean noisy data, choose pertinent segments, and use deep learning networks. Anatomical linkages and data-driven connections were used to create a skeleton model that depicts human underwater mobility in great detail.

Collaboration between human expertise and computer skill will be crucial along this journey. A thorough grasp of aquatic biomechanics is produced through the convergence of subject expertise and technology developments. Applications of underwater human motion analysis are numerous and significant, ranging from improving swimming techniques to solving the mysteries of aquatic species.

The field of underwater human motion analysis has a bright future as technology advances and the understanding grows. These are prepared to uncover new dimensions of information below the water's surface with enhanced algorithms, better data quality, and multidisciplinary cooperation. This voyage advances scientific research while also having direct applications to therapeutic rehabilitation, athletic training, and other areas. These are paving the way to a deeper understanding of human mobility in the aquatic environment by overcoming the obstacles and seizing the opportunities.






























References

G. B. Guerra-Filho, "Optical motion capture: Theory and implementation", J. Theor. Appl. Informat., vol. 12, no. 2, pp. 61-89, 2005.
J. Meyer, M. Kuderer, J. Muller and W. Burgard, "Online marker labeling for fully automatic skeleton tracking in optical motion capture", Proc. IEEE Int. Conf. Robot. Automat., pp. 5652-5657, May 2014.
J. Maycock, T. Röhlig, M. Schröder, M. Bötsch and H. Ritter, "Fully automatic optical motion tracking using an inverse kinematics approach", Proc. IEEE-RAS 15th Int. Conf. Hum. Robots, pp. 461-466, Nov. 2015.
S. Xia, L. Su, X. Fei and H. Wang, "Toward accurate real-time marker labeling for live optical motion capture", Vis. Comput., vol. 33, no. 6, pp. 993-1003, Jun. 2017.
S. Alexanderson, C. O’Sullivan and J. Beskow, "Real-time labeling of non-rigid motion capture marker sets", Comput. Graph., vol. 69, pp. 59-67, Dec. 2017.
S. Han, B. Liu, R. Wang, Y. Ye, C. D. Twigg and K. Kin, "Online optical marker-based hand tracking with deep labels", ACM Trans. Graph., vol. 37, no. 4, pp. 1-10, Aug. 2018.
J. Rosskamp, R. Weller, T. Kluss, J. L. C. Maldonado and G. Zachmann, "Improved CNN-based marker labeling for optical hand tracking", Proc. Int. Conf. Virtual Reality Augmented Reality, pp. 165-177, 2020.
S. Ghorbani, A. Etemad and N. F. Troje, "Auto-labelling of markers in optical motion capture by permutation learning", Proc. Comput. Graph. Int. Conf., vol. 11542, pp. 167-178, 2019.
J. L. J. Bascones, M. Graña and J. M. Lopez-Guede, "Robust labeling of human motion markers in the presence of occlusions", Neurocomputing, vol. 353, pp. 96-105, Aug. 2019.
A. L. Clouthier, G. B. Ross, M. P. Mavor, I. Coll, A. Boyle, and R. B. Graham, "Development and Validation of a Deep Learning Algorithm and Open-Source Platform for the Automatic Labelling of Motion Capture Markers," in IEEE Access, vol. 9, pp. 36444-36454, 2021, doi: 10.1109/ACCESS.2021.3062748.





# Liveness_Face_Detection
                                                        
Project Report

                    CSE 3200: System Development Project

        Face Detection Home Security System




![Image](images/logo.png)



                                   
                                        Project Team

Sourav Mandol (Roll - 1607007)
                                      Sumon Mia (Roll - 1607014)

                                                             Supervised by
                              Dr. Sk. Mohammad Masudul Ahsan
                                       Professor
                Dept. of Computer Science and Engineering
                  Khulna University of Engineering & Technology



                                              INTRODUCTION
Background
Facial recognition is a biometric technology that goes beyond just detecting human faces in an image or video. It goes a bit further to determine whose face it is. A facial recognition system works by taking an image of a face and predicting whether the face matches another face stored in a dataset (or whether a face in one image matches a face in another). 
Face Recognition home security system is a security system that detects a face whether the guy is known or unknown. After detecting the person, it will open the door or unlock any security.

Purpose
High Accuracy Rates
Most facial recognition software being used in smart home locks can accurately determine whether the person trying to gain access to a home matches the database of people who have been authorized to enter. That said, some software programs are more accurate than others, especially when it comes to detecting faces from various angles and recognizing faces of different nationalities.

Automation
Once you’ve set up your smart home security system and granted access to the people you want to allow into your home, the system will automatically let those people in when it detects a match. No need for you to answer the doorbell, or to respond to a request to enter.
Facial recognition technology is here to stay, and will only get better with time and also better from biometric verification. 
Faster processing
The process of recognizing a face takes a second or less — and this is incredibly beneficial for the companies. In the era of constant cyber attacks and advanced hacking tools, companies need a technology that would be both secure and fast.
                         
                                               OBJECTIVES
i.	To developing an unlocking system based on face recognition
ii.	Security
iii.	IOT based project
iv.	User Friendly Interface connecting with Security
v.	Detect as many faces as possible in the training images
vi.	Minimum detection of non-process and Multiple detects
vii.	To Digitalize Home and Office.
viii.	Image  Acquisition
                                   

                                             Design (Data Flow Diagram)
                                     
                  Fig.1: Flow Chart of Face Detection Home Security System
                                          METHODOLOGY
The components of face recognition system are image acquisition, face detection and face recognition as shown by Fig 2.
           Fig.2: Block Diagram of Methodology of Face Recognition

Face detection performance is a key issue, so techniques for dealing with non‐frontal face detection are discussed. Subspace modeling and learning‐based dimension reduction methods are fundamental to many current face recognition techniques. Face recognition has merits of both high accuracy and low intrusive, so it has drawn the attention of the researches in various fields from psychology, image processing to computer vision.


 
 
	                               Implementation          
First, we input an image or video frame to our face recognition pipeline. Given the input image, we apply face detection to detect the location of a face in the image. Optionally, we can compute facial landmarks, enabling us to preprocess and align the face.
Face alignment, as the name suggests, is the process of (1) identifying the geometric structure of the faces and (2) attempting to obtain a canonical alignment of the face based on translation, rotation, and scale.
While optional, face alignment has been demonstrated to increase face recognition accuracy in some pipelines.
fig.3: How the deep learning face recognition model computes the face embedding.


We apply here deep learning and OpenCV together:
i. Detect faces
ii. Compute 128-d face embeddings to quantify a face
iii. Train a Support Vector Machine (SVM) on top of the embeddings
iv. Recognize faces in images and video streams
v. All of these tasks will be accomplished with OpenCV, enabling us to obtain a “pure” OpenCV face recognition pipeline.


                         








                             Graphical User Interface (GUI)
The user interface has all the options needed for the administration and other debugging purpose so that, we do not need to edit code for any management.
               
Fig.4: Home Window                                 Fig.5: Security Window
After Clicking ‘Security or Press Ctrl+A’ from Home window, then security window will open. Click ‘Start’ from security panel, then it will open a camera window which recognizes faces. If the face is in dataset, then it will show his/her name, else show unknown on his/her face. 
 
Fig.6: Recognise Face                               Fig.7: Admin Panel (Login)
                        Fig.8: Admin Section (Fully Accessible for Admin)
To entering the admin section, need a valid password .If the password is wrong, it will show wrong password else it will go to new admin page where admin can add any member, rename  any member if the person exists in database nor it will show “Member Not Found”.      
      Fig.9: Add member                        Fig.10: Rename Member  
     Fig.11: Remove Member       Fig.12: Password Change          
Admin can remove any member from database and also can change his password.

                         
Fig.13: About Window                              Fig.14: Help Window                         

A user friendly graphical interface is design for this system. Any user can easily use this system without any trouble. To make this interface, we used designer from pyqt5. A major advantage of GUIs is that they make computer operation more intuitive, and thus easier to learn and use.

 
                                        Key and Actions
Key	Action
Ctrl+A	Admin Panel
Ctrl+S	Security Panel
Ctrl+P	Password Change Panel
Ctrl+U	Help Panel
Ctrl+E	Exit
shoot	Picture Capture
Q	Capture Window Exit
                     Fig.15: Table for Key and Actions
                               Conclusion and Recommendation
Challenges
The designed algorithm was effectively able to detect the different type of faces specified on this project and recognize those faces which are known or unknown. The system is able to detect an object in both high and low light. The system has completely user friendly graphical interface (GUI). Every customer can able to use this system so easily even this customer don’t know how to use computer can able to user this. The system has more efficiency because it detects a customer within six (6) images putting on the dataset. Its accuracy is almost 90%. If an eyeglasses person is trained in system, the system can recognize his faces.
Limitations
If bright light appears behind object, the system takes some times to detect it but when the system detects the faces it’s easily recognize it. We also use liveness detection to make the security more strong. But livesness detection isn’t as strong as we want. But for average security, it works good. A person who put eyeglass in front camera but who is already trained without eyeglass, the system is slow to recognize him. 
Future Activities
In future, this system will be more fast and accurate. Liveness detection will be stronger and perfectly recognize real or fake person. Also, face will easily detect doesn’t matter the person will put eyeglasses or not in future. In every light combination, the system is able recognize object face accurately.
                                          References

[1]  ‘Design of face detection and recognition system for smart home security application’ , by Dwi Ana Ratna Wati , Dika Abadianto, Department of Electrical Engineering, Universitas Islam Indonesia, Yogyakarta, Indonesia.

[2]’ Facial recognition system’ by Wikipedia

[3] ‘Face Recognition System and It's Application’, by Xuehong Tian Published in: 2009 First International Conference on Information Science and Engineering

[4] ‘Research on Face Recognition Based on Embedded System’, by Hong Zhao, Xi-Jun Liang, and Peng Yang, School of Computer and Communication, Lanzhou University of Technology, Lanzhou 730050, China

[5] ‘Image-based Face Detection and Recognition:“State of the Art” ’,by Faizan Ahmad, Aaima Najam and Zeeshan Ahmed, Department of Computer Science & Engineering, Beijing University of Aeronautics & Astronautics


 

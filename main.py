import cv2
import os
import face_recognition
import csv
import numpy as np
from datetime import datetime
import time
from pkg import cvs


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1460)

#main images from main_img 
new1 = "kamlesh.png"
new2 = "ganesh.jpg"
new3 = "om.jpeg"

#profile images from profile_img
# to add in frame ratio are [111:111 + 229 , 971:971 + 217]
profile1 = "kamlesh.png"
profile2 = "ganesh.png"

#=======================================================================================


#for background images and modes images in cv2  

# to add ratio [190:190 + 480 , 80:80 + 640]
imgBackground = cv2.imread('bg_photos/bg.png')

#for diffrent modes 
img = cv2.imread('modes/attendance_checked.png')
empty = cv2.imread('modes/empty.png')

#=======================================================================================


#list of student with face , name and profile photo to display
# student no 1
img1 = face_recognition.load_image_file(f"img_of_students/main_img/{new1}")
img1_encoding = face_recognition.face_encodings(img1)[0]
img1 = cv2.imread(f"img_of_students/profile_img/{profile1}")

# student no 2
img2 = face_recognition.load_image_file(f"img_of_students/main_img/{new2}")
img2_encoding = face_recognition.face_encodings(img2)[0]
img2 =cv2.imread(f"img_of_students/profile_img/{profile2}")

# student no 3
img3 = face_recognition.load_image_file(f"img_of_students/main_img/{new3}")
img3_encoding = face_recognition.face_encodings(img3)[0]
img3 =cv2.imread(f"img_of_students/profile_img/{profile2}")

#for checking the list of student
known_face_encodings = [img1_encoding,img2_encoding]
known_face_names = ["kamlesh", "ganesh","om"]


#importing the profile pictures from the folder in the imgmodelist[]
folderModePath = 'img_of_students/profile_img/'
modePathList = os.listdir(folderModePath)
imgModeList = []



students = known_face_names.copy()

face_locations = []
face_encodings =[]


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

file = open(f"{current_date}.csv" , 'w+' , newline="")
lnwriter = csv.writer(file)

while True:
    _, frame = cap.read()
   
    imgBackground[190:190 + 480 , 80:80 + 640] =frame
    imgBackground[ 34:34 + 653 , 769:769 + 613] = empty
    small_frame = cv2.resize(frame,(0,0) ,fx=0.25 ,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame , cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame ,face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings ,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]
            for path in modePathList:
                imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

            if name in known_face_names:
                #time.sleep(1)
                imgBackground[61:61 + 229 , 971:971 + 217] = img1
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale = 1.5
                fontColor = (255,0,0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name +" Present", bottomLeftCornerOfText,font,fontScale, fontColor , thickness ,lineType)

                if name in students:
                    students.remove(name)

                    current_time = now.strftime("%H:%M:%S")
                    cvs.insert([name])
                    lnwriter.writerow([name, current_time])
                    print([name,current_time])
                    print("test")
        
    cv2.imshow("Camera",imgBackground)
    
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()

file.close()
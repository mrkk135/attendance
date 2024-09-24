import cv2
import os
import face_recognition
import numpy as np
from pkg import cvs
import s_name  as s_name


class livecamp:
    def __init__(self) :
            cap = cv2.VideoCapture(0)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1460)

        
            img_encoding = []
            known_face_encodings = []
            known_face_names = []
            path = s_name.img_path()
            name = s_name.student_name()

            for i in path:
                img_path = face_recognition.load_image_file(i)
                temp = face_recognition.face_encodings(img_path)[0]
                img_encoding.append(temp)

            #for checking the list of student


            known_face_encodings = img_encoding
            known_face_names = name


            #importing the profile pictures from the folder in the imgmodelist[]
            folderModePath = 'img_of_students/profile_img/'
            modePathList = os.listdir(folderModePath)
            imgModeList = []

            students = known_face_names.copy()

            face_locations = []
            face_encodings =[]


            while True:
                _, frame = cap.read()
                
                #imgBackground[190:190 + 480 , 80:80 + 640] =frame
                #imgBackground[ 34:34 + 653 , 769:769 + 613] = empty
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
                            #imgBackground[61:61 + 229 , 971:971 + 217] = img1
                            font = cv2.FONT_HERSHEY_TRIPLEX   
                            bottomLeftCornerOfText = (10,100)
                            fontScale = 1.5
                            fontColor = (255,0,0)
                            thickness = 3
                            lineType = 2
                            cv2.putText(frame, name +" Present", bottomLeftCornerOfText,font,fontScale, fontColor , thickness ,lineType)
                            if name in students:
                                students.remove(name)
                                print(name +" Present")
                                cvs.insert([name])
                                
                cv2.imshow("Camera",frame)

                cv2.waitKey(1)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                
            cap.release()

            cv2.destroyAllWindows()


livecamp()
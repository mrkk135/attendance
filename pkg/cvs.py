import csv
from datetime import datetime
import conn

def student_name():
    s_name = []
    r = conn.import_name()
    for name in r:
        s_name.append(name[1])

    return s_name


def insert(names):
    now = datetime.now()
    current_time =now.strftime('%I-%M-%p')        
    name =()
    t_name =  student_name()
    for  i in t_name:
        name +=([f'{i}'],)

    current_date = now.strftime("%Y-%m-%d")
    file = open(f'csv/{current_date}.csv' , 'a' , newline='')
    for i in range(len(name)):
        lnwriter = csv.writer(file, lineterminator='\n')
        if names == name[i]:
            lnwriter = csv.writer(file, lineterminator='\n')
            
            while True:
                lnwriter.writerow([names ,current_time])
                print(names)
                break
            file.close()
        else:
            i +=1

  

 #============================================


import csv
from datetime import datetime
import time



def insert(names):
    now = datetime.now()
    current_time =datetime.now()
    print(current_time)
    name =(['kamlesh'],['ganesh'],['Charlie'])
    current_date = now.strftime("%Y-%m-%d")
    file = open(f'csv/{current_date}.csv' , 'a' , newline='')
    for i in range(len(name)):
        if names == name[i]:
            lnwriter = csv.writer(file, lineterminator='\n')
            while True:
                lnwriter.writerow([names , current_time])
                print("Insert complete")
                break
            file.close()
        else:
            i +=1

  

 #============================================


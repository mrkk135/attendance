import conn as conn
def student_name():
    s_name = []
    r = conn.import_name()
    for name in r:
        s_name.append(name[1])

    return s_name

def img_path():
    mydb = conn.database()
    img = []
    photo =[]
    cur = mydb.cursor()
    cur.execute("SELECT s_path FROM student;")
    result = cur.fetchall()
    for i in result:
        img.append([*i])    
    
    for i in range(len(img)):
        photo.append(img[i][0])

    return photo

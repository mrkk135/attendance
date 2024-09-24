import shutil

def path_writer():
    f = open('pkg/path_name.txt', 'r')
    path = f.read()
    print(path)
    source_path =  path
    destination_path = 'img_of_students/main_img/'
    s_path = shutil.copy(source_path, destination_path)
    return s_path
def path(path):
    fw = open('pkg/path_name.txt', 'w')
    fw.write(path) 
    fw.close()
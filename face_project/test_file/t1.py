import os , cv2

folderPath = 'pkg/'
pathList   = os.listdir(folderPath)
imglist = []
for path in pathList:
    imglist.append(cv2.imread(os.path.join(folderPath,path)))



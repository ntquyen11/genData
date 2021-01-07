import cv2
import os
pathTrain='/media/ntquyen/DATA/ntquyen/Machine_Learning/images/train2017'
listFile=os.listdir(pathTrain)
listImg=[f for f in listFile if (f.find('.jpg')!=-1)]
i=0
with open('train.txt','w') as f:
    for i in range(len(listImg)):
        path=os.path.join('/media/ntquyen/DATA/ntquyen/Machine_Learning/images/train2017',listImg[i])
        f.write(path+'\n')
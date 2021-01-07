import cv2
import os
pathTrain='/media/ntquyen/DATA/ntquyen/Machine_Learning/genData/label/test'
listFile=os.listdir(pathTrain)
# listImg=[f for f in listFile if (f.find('.jpg')!=-1)]
i=0
saveDir='testJson.txt'
with open(saveDir,'w') as f:
    for i in range(len(listFile)):
        path=os.path.join(pathTrain,listFile[i])
        f.write(path+'\n')
        
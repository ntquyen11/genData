import os

import cv2
path='/media/ntquyen/DATA/ntquyen/Machine_Learning/images/train2017'
pth='/media/ntquyen/DATA/ntquyen/Machine_Learning/images/train2017'
listImg=[dir for dir in os.listdir(path) if (dir.find('jpg')!=-1)]
with open('/media/ntquyen/DATA/ntquyen/Machine_Learning/train.txt','w') as f:
    for dir in listImg:
        # Anno=dir.replace('jpg','txt')
        ImgDir=os.path.join(pth,dir)
        # AnnoDIr=os.path.join(pth,Anno)
        f.write(ImgDir+'\n')


# with open('test_name_size1.txt','w') as f:
#     for dir in listImg:
#         img=cv2.imread(os.path.join(path,dir))
#         w,h=img.shape[0],img.shape[1]
#         f.write(dir.replace('.jpg','')+' '+str(w)+' '+str(h)+'\n')
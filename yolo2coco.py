import os
import cv2
 
# 
path='/media/ntquyen/DATA/ntquyen/Machine_Learning/images/val2017'
originDir = '/media/ntquyen/DATA/ntquyen/Machine_Learning/images/val2017'
 # Converted file save path
saveDir = 'annosTest.txt'                                                                           
 # Picture path corresponding to the original label
# originImagesDir = ''
 
txtFileList = [dir for dir in os.listdir(originDir) if (dir.find('txt')!=-1)]
with open(saveDir, 'w') as fw:
    for txtFile in txtFileList:
        with open(os.path.join(originDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])
 
                # convert x,y,w,h to x1,y1,x2,y2
                imagePath = os.path.join(originDir,
                                         txtFile.replace('txt', 'jpg'))
                image = cv2.imread(imagePath)
                H, W, _ = image.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                                 # In order to match the coco label method, the label serial number is calculated from 1
                fw.write(txtFile.replace('txt', 'jpg') + ' {} {} {} {} {}\n'.format(int(label[0]) + 1, x1, y1, x2, y2))
 
        # print('{} done'.format(txtFile))
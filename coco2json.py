import json
import os
import cv2
 
 # ------------ Use os to extract the image name in the images folder, and read the BBox into it ------------
 #root path, which contains images (picture folder), annos.txt (bbox annotation), classes.txt (category label),
 # and annotations folder (created automatically if not, used to save the last json)
root_path = '/media/ntquyen/DATA/ntquyen/Machine_Learning/genData'
ImgDir='/media/ntquyen/DATA/ntquyen/Machine_Learning/images'
imgdir='/home/hoangphuong'
 # Used to create a training set or validation set
Phase = 'test2017' # need to be corrected
 
 # dataset is used to save image information and annotation information of all data
dataset = {'images': [],'categories': [] , 'annotations': []}
 
 # Open category label
with open('classes.txt') as f:
    classes = f.read().strip().split()
 
 # Establish the correspondence between category labels and numeric ids
for i, cls in enumerate(classes, 1):
    dataset['categories'].append({'id': i, 'name': cls, 'supercategory': cls})
 
 # Read the image name of the images folder
indexes =[dir for dir in os.listdir(ImgDir+'/val2017') if (dir.find('jpg')!=-1)]
 
 # Statistics Processing the number of pictures
global count
count = 0
 
 # Read Bbox information
with open(os.path.join(root_path, 'annosTest.txt')) as tr:
    annos = tr.readlines()
 
    # --------------- Then, the above data is converted to the format required by COCO ---------------
    for k, index in enumerate(indexes):
        count += 1
        # Read images with opencv to get the width and height of the image
        # print(os.path.join(ImgDir,'train2017',index))
        direct=os.path.join(ImgDir,'val2017',index)
        im = cv2.imread(direct)
        height, width, _ = im.shape
        fileName=os.path.join(imgdir,'val2017',index)
        # Add image information to the dataset
        dataset['images'].append({'file_name': fileName,
                                  'id': k,
                                  'width': width,
                                  'height': height})
 
        for ii, anno in enumerate(annos):
            parts = anno.strip().split()
            # print(parts)
            # Add a tag if the name of the image and the name of the tag are on
            if parts[0] == index:
                                 # 
                cls_id = parts[1]
                # x_min
                x1 = float(parts[2])
                # y_min
                y1 = float(parts[3])
                # x_max
                x2 = float(parts[4])
                # y_max
                y2 = float(parts[5])
                width = max(0, x2 - x1)
                height = max(0, y2 - y1)
                dataset['annotations'].append({
                    'area': width * height,
                    'bbox': [x1, y1, width, height],
                    'category_id': int(cls_id),
                    'id': i,
                    'image_id': k,
                    'iscrowd': 0,
                                         # mask, the rectangle is the four vertices clockwise from the top left corner
                    'segmentation': [[x1, y1, x2, y1, x2, y2, x1, y2]]
                })
                # print(dataset['annotations'])
        # json_name = os.path.join(root_path, 'label/test/{}.json'.format(index.rstrip('.jpg')))
        # with open(json_name, 'w') as f:
        #     json.dump(dataset, f)
        print('{} images handled'.format(count))
 
 #Save the resulting folder
folder = os.path.join(root_path, 'annotations')
# if not os.path.exists(folder):
#   os.makedirs(folder)
json_name = os.path.join(root_path, 'annotations/{}.json'.format(Phase))
with open(json_name, 'w') as f:
  json.dump(dataset, f)
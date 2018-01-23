from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
imagevideo1 = imread("00001.jpg")

image2 = imread("plane.jpg")
print imagevideo1.shape[0]
print image2.shape[0]

c = np.ones((image2.shape[0],image2.shape[1]))
difference = imagevideo1 - image2
number = 0
print (difference.shape)
point = np.zeros((81772,2))
for i in range(720):
    for j in range(1280):
        if difference[i][j][0]!=0 or difference[i][j][1]!=0 or difference[i][j][2]!=0:
            point[number][0] = i
            point[number][1] = j
            number+=1
            print number

print(number)
zeronumber = 0
shotpoint = np.zeros((5262,2))
for  i in range(81772):
    if point[i][0]>=192 and point[i][0]<=235 and point[i][1]>=630 and point[i][1]<=656:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=221 and point[i][0]<=249 and point[i][1]>=502 and point[i][1]<=531:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=347 and point[i][0]<=373 and point[i][1]>=475 and point[i][1]<=514:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=471 and point[i][0]<=505 and point[i][1]>=494 and point[i][1]<=538:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=487 and point[i][0]<=535 and point[i][1]>=626 and point[i][1]<=656:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=476 and point[i][0]<=505 and point[i][1]>=747 and point[i][1]<=784:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=344 and point[i][0]<=376 and point[i][1]>=766 and point[i][1]<=808:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
    if point[i][0]>=219 and point[i][0]<=251 and point[i][1]>=749 and point[i][1]<=787:
        shotpoint[zeronumber] = point[i]
        zeronumber += 1
shotpoint = shotpoint.astype('int')
def median(image,shotpoint,area):
    col = shotpoint[:, 1]
    row = shotpoint[:, 0]
    points = []
    for x in range(len(row)):
        b = (row[x],col[x])
        points.append(b)
    for i in points:###i is a tuple (row,col)
        low_height = i[0] - area
        high_height = i[0] + area
        low_weight = i[1] - area
        high_weight = i[1] + area
        c_part = c[low_height:high_height+1,low_weight:high_weight+1].astype(int)
        for channel in range(3):
            a_part = image[low_height:high_height+1,low_weight:high_weight+1,channel]
            hk = np.where(c_part > 0, a_part, 0)
            image[i[0], i[1], channel] = np.median(hk)
    return image
for x in range(3621):
    imagevideo2 = imread("C:\\Users\\Administrator\\Desktop\\uav\\" + "{:0>5d}" .format(x + 1)+ '.jpg')
    imagefree = median(imagevideo2, shotpoint,10)
    img = Image.fromarray(imagefree,'RGB')
    img.save("C:\\cv\\"+ "{:0>5d}" .format(x + 1)+ '.jpg')












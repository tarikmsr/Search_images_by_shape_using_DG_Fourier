from PIL import Image
from os import walk
import numpy as np
from PIL import Image
import math as math
import pickle
import json

# Traitement et les fonctions
#

gfd_temp=[]

def manhattan_distance(vec1, vec2):
    return np.sum(np.abs(vec1 - vec2))


def euclidean_distance(vec1, vec2):
    return np.linalg.norm(vec1-vec2)

def hamming_distance(vec1, vec2):
    return np.count_nonzero(vec1!=vec2)




def GFD(bw, m, n):
    # preprocess the image
    if len(bw.shape) > 2:
        bw = bw.max(axis = 2) / 255
    width = bw.shape[1]
    N = width
    maxR = math.sqrt((((N)//2)**2) + (((N)//2)**2))

    x = np.linspace(-(N-1)//2, (N-1)//2, N )
    y = x
    X, Y = np.meshgrid(x, y)

    radius = np.sqrt(np.power(X, 2) + np.power(Y, 2)) / maxR

    theta = np.arctan2(Y, X)
    theta[theta < 0] = theta[theta < 0] + 2+ np.pi

    FR = np.zeros((m,n))
    FI = np.zeros((m,n))
    FD = np.zeros((m*n,1))

    i = 0
    for rad in range(m):
        for ang in range(n):
            # e^(i * theta) = cos(theta) + i * sin(theta)
            # PF = FR + i * FI
            tempR = bw * np.cos(2 * np.pi * rad * radius + ang * theta)
            tempI = bw * np.sin(2 * np.pi * rad * radius + ang * theta)
            FR[rad, ang] = np.sum(tempR)
            FI[rad, ang] = np.sum(tempI)
            
            if rad == 0 and ang == 0:
                FD[i] = math.sqrt((2* (FR[0,0] * FR[0,0]))) / (np.pi* maxR * maxR)
            else:
                FD[i] = math.sqrt((FR[rad, ang] * FR[rad, ang]) + (FI[rad, ang] * FI[rad, ang])) / (math.sqrt((2* (FR[0,0] * FR[0,0]))))
            i = i + 1
    return FD



def getImages_names():
    
    images_name = []
    for (dirpath, dirnames, filenames) in walk("./images"):
        images_name.extend(filenames)
        break
    return images_name

    
images_name= []
images_name=getImages_names()

#images_name=['apple-1.png', 'apple-10.png', 'apple-11.png', 'apple-12.png', 'apple-13.png', 'apple-14.png', 'apple-15.png', 'apple-16.png', 'apple-17.png', 'apple-18.png', 'apple-19.png', 'apple-2.png', 'apple-20.png', 'apple-3.png', 'apple-4.png', 'apple-5.png', 'apple-6.png', 'apple-7.png', 'apple-8.png', 'apple-9.png', 'bat-1.png', 'bat-10.png', 'bat-11.png', 'bat-12.png', 'bat-13.png', 'bat-14.png', 'bat-15.png', 'bat-16.png', 'bat-17.png', 'bat-18.png', 'bat-19.png', 'bat-2.png', 'bat-20.png', 'bat-3.png', 'bat-4.png', 'bat-5.png']

"""
images = [{ 'name':image,'path':  'images/' + image , 'image': np.array(Image.open('./images/' + image )  ) } for image in images_name ]
print("db-start")
db = [ { 'name':image['name'],'path': image['path'], 'image': image['image'], 'descriptor': GFD(image['image'], 4, 9)} for image in images]




myfile = open("data.pkl", "wb")
pickle.dump(db, myfile)
myfile.close()

#read file
myfile = open("data.pkl", "rb")
output = pickle.load(myfile)
print("I did all of them!")
myfile.close()

print("db-end")
"""

myfile = open("data.pkl", "rb")
output = pickle.load(myfile)

def search_image(image_src):
    stats = []
    global gfd_temp

    try:
        image = np.array(Image.open(""+image_src))  
    except Exception:
        print(Exception) 
    gfd = GFD(image, 4, 9)
    gfd_temp = gfd
    print(gfd_temp)
    for db_image in output:
        stats.append({'name':db_image['name'],'distance': manhattan_distance(gfd, db_image['descriptor']), 'path': db_image['path'] })
        stats.sort(key=distance)  
    outstats = open('stats.txt', 'w')
    json.dump(stats, outstats)
    return stats


def distance(stat):
    return stat['distance']

"""def search_image_pertinance(image_src):
    myfile = open("stats1.txt", "r")
    oldstats = json.load(myfile)
    myfile.close()
    return oldstats"""



def find_index(my_str , my_list):
    for num , i in enumerate( my_list ):
        try:
            if my_str in i['path']:
                return num
        except:
            pass





def search_image_pertinance_down(image_src):
    newstats = []
    try:
        image = np.array(Image.open(""+image_src))  
    except Exception:
        print(Exception) 
    gfd = GFD(image, 4, 9)

    print("GFD")
    print(gfd)
    print("GFD TEMP")
    print(gfd_temp)

    myfile = open("stats.txt", "r")
    oldstats = json.load(myfile)
    dic = next(x for x in oldstats if x["path"] == image_src)
    old_distance = dic["distance"]

    new_distance = euclidean_distance(gfd_temp, gfd)
    print("NEW DISTANCE")
    print(new_distance)


    if old_distance < new_distance :
        old_distance = new_distance
        print(old_distance)
        dic["distance"] = old_distance

        print(dic)

        target_index = find_index(image_src, oldstats)

        oldstats[target_index]["distance"] = new_distance

    newstats = oldstats
    newstats.sort(key=distance)  

    outstats = open('stats.txt', 'w')
    json.dump(newstats, outstats)
    print("DONE!")
        #traitement new image

        #stats.append({'name':db_image['name'],'distance': manhattan_distance(gfd, db_image['descriptor']), 'path': db_image['path'] })
        #stats.sort(key=distance) 
    myfile.close()
    return newstats



def search_image_pertinance_up(image_src):
    newstats = []
    try:
        image = np.array(Image.open(""+image_src))  
    except Exception:
        print(Exception) 
    gfd = GFD(image, 4, 9)

    print("GFD")
    print(gfd)
    print("GFD TEMP")
    print(gfd_temp)

    myfile = open("stats.txt", "r")
    oldstats = json.load(myfile)
    dic = next(x for x in oldstats if x["path"] == image_src)
    old_distance = dic["distance"]

    new_distance = euclidean_distance(gfd_temp, gfd)
    print("NEW DISTANCE")
    print(new_distance)


    if old_distance > new_distance :
        old_distance = new_distance
        print(old_distance)
        dic["distance"] = old_distance

        print(dic)

        target_index = find_index(image_src, oldstats)

        oldstats[target_index]["distance"] = new_distance

    newstats = oldstats
    newstats.sort(key=distance)  

    outstats = open('stats.txt', 'w')
    json.dump(newstats, outstats)
    print("DONE!")
        #traitement new image

        #stats.append({'name':db_image['name'],'distance': manhattan_distance(gfd, db_image['descriptor']), 'path': db_image['path'] })
        #stats.sort(key=distance) 
    myfile.close()
    return newstats



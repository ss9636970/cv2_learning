import numpy as np
import cv2
import matplotlib.pyplot as plt # plt 用於顯示圖片
import matplotlib.image as mpimg # mpimg 用於讀取圖片
import numpy as np
import os
import PIL

def showpic(pic):
    plt.imshow(pic)
    plt.axis('off')
    plt.show

def readpic(p):
    return mpimg.imread(p)
    
def savepic(img, p):
    plt.imshow(img) # 顯示圖片
    plt.axis('off')
    plt.savefig(p)


if __name__ == '__main__':
    p = './C2_TrainDev/Train'
    dir_train_file = os.listdir(p)
    pic = readpic(p + '/' + dir_train_file[0])
    #取出 RGB
    B,G,R = cv2.split(pic)
    cv2.imshow("RED",R)

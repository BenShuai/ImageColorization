from PIL import Image,ImageDraw
import time,multiprocessing,os
import mains.RtoImg
import mains.GtoImg
import mains.BtoImg
import mains.LtoImg


### 调用多进程进行图片训练
def main(thisImgSrc):
    # thisImgSrc='/Users/sunshuai/Desktop/SunShuai/pg.jpg'
    im=Image.open(thisImgSrc) #打开的图像对象

    w=im.width # 原图的宽
    h=im.height # 原图的高

    w1=int(w/2)
    h1=int(h/2)

    moduleFilePath="./module/" # 训练的数据存储的位置

    # 判断文件夹是否存在
    if os.path.exists(moduleFilePath):
        pass
    else:
        os.makedirs(moduleFilePath) # 不存在就创建

    mains.RtoImg.main(im,w,h,w1,h1,moduleFilePath) # 调用转R通道的方法，将训练数据存储到对应的module
    mains.GtoImg.main(im,w,h,w1,h1,moduleFilePath) # 调用转G通道的方法，将训练数据存储到对应的module
    mains.BtoImg.main(im,w,h,w1,h1,moduleFilePath) # 调用转B通道的方法，将训练数据存储到对应的module
    mains.LtoImg.main(im,w,h,w1,h1,moduleFilePath) # 调用转L通道的方法，将训练数据存储到对应的module




if __name__=='__main__':
    filesPath='/Users/sunshuai/Documents/硬盘文件夹/手机壁纸/'
    for (dirpath,dirnames,filenames) in os.walk(filesPath):#访问文件夹下的所有文件
        for filename in filenames:
            print(filename)

            ticks = time.time() #运行开始之前，获得当前时间(用来结束的时候获取解析总用时)

            main(filesPath+filename)

            ticks2 = time.time() #运行结束之后，获得当前时间
            print("单张图用时：",ticks2-ticks,"秒")

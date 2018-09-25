## 将图片转成G通道

from PIL import Image,ImageDraw
import time,multiprocessing,os

def gToImg1(im,w,h,w1,h1,moduleFilePath):
    moduleFileName="G1.module"  # module的文件名字

    # imR=Image.new('RGB', (w, h), (255, 255, 255))
    # drawR = ImageDraw.Draw(imR)

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）
    for x in range(w1):
        for y in range(h1):
            cur_pixel = im.getpixel((x, y)) # 获得图像的rgb值
            # print(cur_pixel)
            # drawR.ellipse((x,y,x+1,y+1), fill = (0,cur_pixel[1],0)) # 画像素点
            if(up!=(cur_pixel[1],cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel[1],cur_pixel))# 写入文件
                up=(cur_pixel[1],cur_pixel)
    f.close()
    # imR.show()



def gToImg2(im,w,h,w1,h1,moduleFilePath):
    moduleFileName="G2.module"  # module的文件名字

    # imR=Image.new('RGB', (w, h), (255, 255, 255))
    # drawR = ImageDraw.Draw(imR)

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）
    for x in range(w-w1):
        for y in range(h1):
            cur_pixel = im.getpixel((w1+x, y)) # 获得图像的rgb值
            # print(cur_pixel)
            # drawR.ellipse((w1+x,y,w1+x+1,y+1), fill = (0,cur_pixel[1],0)) # 画像素点
            if(up!=(cur_pixel[1],cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel[1],cur_pixel))# 写入文件
                up=(cur_pixel[1],cur_pixel)
    f.close()
    # imR.show()



def gToImg3(im,w,h,w1,h1,moduleFilePath):
    moduleFileName="G3.module"  # module的文件名字

    # imR=Image.new('RGB', (w, h), (255, 255, 255))
    # drawR = ImageDraw.Draw(imR)

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）

    for x in range(w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((x, h1+y)) # 获得图像的rgb值
            # print(cur_pixel)
            # drawR.ellipse((x,h1+y,x+1,h1+y+1), fill = (0,cur_pixel[1],0)) # 画像素点
            if(up!=(cur_pixel[1],cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel[1],cur_pixel))# 写入文件
                up=(cur_pixel[1],cur_pixel)
    f.close()
    # imR.show()


def gToImg4(im,w,h,w1,h1,moduleFilePath):
    moduleFileName="G4.module"  # module的文件名字

    # imR=Image.new('RGB', (w, h), (255, 255, 255))
    # drawR = ImageDraw.Draw(imR)

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）

    for x in range(w-w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((w1+x, h1+y)) # 获得图像的rgb值
            # print(cur_pixel)
            # drawR.ellipse((w1+x,h1+y,w1+x+1,h1+y+1), fill = (0,cur_pixel[1],0)) # 画像素点
            if(up!=(cur_pixel[1],cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel[1],cur_pixel))# 写入文件
                up=(cur_pixel[1],cur_pixel)
    f.close()
    # imR.show()


def main(im,w,h,w1,h1,moduleFilePath):
    #### 用多进程的方式将图像转成G通道图
    pr1 = multiprocessing.Process(target=gToImg1, args=(im,w,h,w1,h1,moduleFilePath,))
    pr2 = multiprocessing.Process(target=gToImg2, args=(im,w,h,w1,h1,moduleFilePath,))
    pr3 = multiprocessing.Process(target=gToImg3, args=(im,w,h,w1,h1,moduleFilePath,))
    pr4 = multiprocessing.Process(target=gToImg4, args=(im,w,h,w1,h1,moduleFilePath,))

    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()

    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()
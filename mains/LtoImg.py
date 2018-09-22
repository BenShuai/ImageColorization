## 将图片转成L通道

from PIL import Image
import time,multiprocessing,os

def lToImg1(im,w,h,w1,h1,moduleFilePath,imL):
    moduleFileName="L1.module"  # module的文件名字

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）
    for x in range(w1):
        for y in range(h1):
            cur_pixel = im.getpixel((x, y)) # 获得图像的rgb值
            cur_pixel2 = imL.getpixel((x, y)) # 获得图像L通道的rgb值
            if(up!=(cur_pixel2,cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel2,cur_pixel))# 写入文件
                up=(cur_pixel2,cur_pixel)
    f.close()


def lToImg2(im,w,h,w1,h1,moduleFilePath,imL):
    moduleFileName="L2.module"  # module的文件名字

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）
    for x in range(w-w1):
        for y in range(h1):
            cur_pixel = im.getpixel((w1+x, y)) # 获得图像的rgb值
            cur_pixel2 = imL.getpixel((w1+x, y)) # 获得图像L通道的rgb值
            if(up!=(cur_pixel2,cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel2,cur_pixel))# 写入文件
                up=(cur_pixel2,cur_pixel)
    f.close()



def lToImg3(im,w,h,w1,h1,moduleFilePath,imL):
    moduleFileName="L3.module"  # module的文件名字

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）

    for x in range(w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((x, h1+y)) # 获得图像的rgb值
            cur_pixel2 = imL.getpixel((x, h1+y)) # 获得图像L通道的rgb值
            if(up!=(cur_pixel2,cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel2,cur_pixel))# 写入文件
                up=(cur_pixel2,cur_pixel)
    f.close()


def lToImg4(im,w,h,w1,h1,moduleFilePath,imL):
    moduleFileName="L4.module"  # module的文件名字

    up=() # 上一个像素的值以及替换色【做一个简单的去重过滤，跟上一个一样的就不存到文件，后面还会有专业的全文件去重，这里只是略微减少重复】

    f = open(moduleFilePath+moduleFileName, 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）

    for x in range(w-w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((w1+x, h1+y)) # 获得图像的rgb值
            cur_pixel2 = imL.getpixel((w1+x, h1+y)) # 获得图像L通道的rgb值
            if(up!=(cur_pixel2,cur_pixel)):
                f.write("%s=%s\n" % (cur_pixel2,cur_pixel))# 写入文件
                up=(cur_pixel2,cur_pixel)
    f.close()


def main(im,w,h,w1,h1,moduleFilePath):

    imL=im.convert('L') # 灰度图
    # imL.show()

    #### 用多进程的方式将图像转成L通道图
    pr1 = multiprocessing.Process(target=lToImg1, args=(im,w,h,w1,h1,moduleFilePath,imL,))
    pr2 = multiprocessing.Process(target=lToImg2, args=(im,w,h,w1,h1,moduleFilePath,imL,))
    pr3 = multiprocessing.Process(target=lToImg3, args=(im,w,h,w1,h1,moduleFilePath,imL,))
    pr4 = multiprocessing.Process(target=lToImg4, args=(im,w,h,w1,h1,moduleFilePath,imL,))

    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()

    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()

# author:SunShuai
# 单进程的方式进行处理【测试本机性能用】
from PIL import Image,ImageDraw
import time,multiprocessing,os


def main():
    imgPath='/Users/sunshuai/Desktop/SunShuai/01-01.jpg'
    im=Image.open(imgPath) #打开的图像对象

    w=im.width # 原图的宽
    h=im.height # 原图的高


    imR=Image.new('RGB', (w, h), (255, 255, 255))
    drawR = ImageDraw.Draw(imR)

    for x in range(w):
        for y in range(h):
            cur_pixel = im.getpixel((x, y)) # 获得图像的rgba值
            # print(cur_pixel)
            drawR.ellipse((x,y,x+1,y+1), fill = (cur_pixel[0],0,0)) # 画一个红色的圆圈，覆盖掉顶部圆球
    imR.show()



if __name__=='__main__':
    ticks = time.time() #运行开始之前，获得当前时间(用来结束的时候获取解析总用时)

    main()

    ticks2 = time.time() #运行结束之后，获得当前时间
    print("用时：",ticks2-ticks,"秒")
# author:SunShuai
### 测试将灰色图片转换成彩色图片

from PIL import Image,ImageDraw
import time,os,multiprocessing

moduleFilePath='./module/'
vlaues=[0 for i in range(256)]

##############################################################################################################################

def loadModule(): # 注：这里是把模型数据存在本地文件，后面可以考虑把数据存储到MongoDB等地方，这样查询就会快很多，不需要遍历本地模型数据了
    print("加载module数据开始")

    ticks = time.time() #运行开始之前，获得当前时间(用来结束的时候获取解析总用时)

    f = open(moduleFilePath+'L1.module', 'r')
    try:
        while True:
            line = f.readline()
            if not line:
                break
            # print(line)
            lineNum=line.split('=')
            # print(lineNum)
            lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
            # print(lineNumRgb)
            vlaues[int(lineNum[0])]=lineNumRgb
    finally:
        f.close()

    f2 = open(moduleFilePath+'L2.module', 'r')
    try:
        while True:
            line = f2.readline()
            if not line:
                break
            # print(line)
            lineNum=line.split('=')
            # print(lineNum)
            lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
            # print(lineNumRgb)
            vlaues[int(lineNum[0])]=lineNumRgb
    finally:
        f2.close()

    f3 = open(moduleFilePath+'L3.module', 'r')
    try:
        while True:
            line = f3.readline()
            if not line:
                break
            # print(line)
            lineNum=line.split('=')
            # print(lineNum)
            lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
            # print(lineNumRgb)
            vlaues[int(lineNum[0])]=lineNumRgb
    finally:
        f3.close()

    f4 = open(moduleFilePath+'L4.module', 'r')
    try:
        while True:
            line = f4.readline()
            if not line:
                break
            # print(line)
            lineNum=line.split('=')
            # print(lineNum)
            lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
            # print(lineNumRgb)
            vlaues[int(lineNum[0])]=lineNumRgb
    finally:
        f4.close()

    ticks2 = time.time() #运行结束之后，获得当前时间
    print(vlaues)
    print("加载module数据结束用时：",ticks2-ticks,"秒")


##############################################################################################################################


def ToImg1(im,w,h,w1,h1,vlaues,imgPath):
    imResult=Image.new('RGB', (w1, h1), (255, 255, 255))
    drawR = ImageDraw.Draw(imResult)

    for x in range(w1):
        for y in range(h1):
            cur_pixel = im.getpixel((x, y)) # 获得图像的rgb值
            # print(cur_pixel)
            RGBnum=[]
            try:
                RGBnum=vlaues[int(cur_pixel[0])]
            except:
                RGBnum=vlaues[int(cur_pixel)]
            # print(RGBnum)
            if len(RGBnum)==3:
                drawR.ellipse((x,y,x+1,y+1), fill = (int(RGBnum[0]),int(RGBnum[1]),int(RGBnum[2]))) # 画像素点
    # imResult.show()
    path=imgPath.lower().replace('.jpg','-1.jpg').replace('.png','-1.png').replace('.jpeg','-1.jpeg').replace('.gif','-1.gif')
    imResult.save(path)

##############################################################################################################################

def ToImg2(im,w,h,w1,h1,vlaues,imgPath):
    imResult=Image.new('RGB', (w-w1, h1), (255, 255, 255))
    drawR = ImageDraw.Draw(imResult)

    for x in range(w-w1):
        for y in range(h1):
            cur_pixel = im.getpixel((w1+x, y)) # 获得图像的rgb值
            RGBnum=[]
            try:
                RGBnum=vlaues[int(cur_pixel[0])]
            except:
                RGBnum=vlaues[int(cur_pixel)]
            if len(RGBnum)==3:
                drawR.ellipse((x,y,x+1,y+1), fill = (int(RGBnum[0]),int(RGBnum[1]),int(RGBnum[2]))) # 画像素点
    # imResult.show()
    path=imgPath.lower().replace('.jpg','-2.jpg').replace('.png','-2.png').replace('.jpeg','-2.jpeg').replace('.gif','-2.gif')
    imResult.save(path)

##############################################################################################################################

def ToImg3(im,w,h,w1,h1,vlaues,imgPath):
    imResult=Image.new('RGB', (w1, h-h1), (255, 255, 255))
    drawR = ImageDraw.Draw(imResult)

    for x in range(w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((x, h1+y)) # 获得图像的rgb值
            RGBnum=[]
            try:
                RGBnum=vlaues[int(cur_pixel[0])]
            except:
                RGBnum=vlaues[int(cur_pixel)]
            if len(RGBnum)==3:
                drawR.ellipse((x,y,x+1,y+1), fill = (int(RGBnum[0]),int(RGBnum[1]),int(RGBnum[2]))) # 画像素点
    # imResult.show()
    path=imgPath.lower().replace('.jpg','-3.jpg').replace('.png','-3.png').replace('.jpeg','-3.jpeg').replace('.gif','-3.gif')
    imResult.save(path)

##############################################################################################################################

def ToImg4(im,w,h,w1,h1,vlaues,imgPath):
    imResult=Image.new('RGB', (w-w1, h-h1), (255, 255, 255))
    drawR = ImageDraw.Draw(imResult)

    for x in range(w-w1):
        for y in range(h-h1):
            cur_pixel = im.getpixel((w1+x, h1+y)) # 获得图像的rgb值
            RGBnum=[]
            try:
                RGBnum=vlaues[int(cur_pixel[0])]
            except:
                RGBnum=vlaues[int(cur_pixel)]
            if len(RGBnum)==3:
                drawR.ellipse((x,y,x+1,y+1), fill = (int(RGBnum[0]),int(RGBnum[1]),int(RGBnum[2]))) # 画像素点
    # imResult.show()
    path=imgPath.lower().replace('.jpg','-4.jpg').replace('.png','-4.png').replace('.jpeg','-4.jpeg').replace('.gif','-4.gif')
    imResult.save(path)

##############################################################################################################################

def main(imgPath,vlaues):
    im=Image.open(imgPath)
    w=im.width # 原图的宽
    h=im.height # 原图的高
    w1=int(w/2)
    h1=int(h/2)

    #### 用多进程的方式将图像转成彩色图像
    pr1 = multiprocessing.Process(target=ToImg1, args=(im,w,h,w1,h1,vlaues,imgPath,))
    pr2 = multiprocessing.Process(target=ToImg2, args=(im,w,h,w1,h1,vlaues,imgPath,))
    pr3 = multiprocessing.Process(target=ToImg3, args=(im,w,h,w1,h1,vlaues,imgPath,))
    pr4 = multiprocessing.Process(target=ToImg4, args=(im,w,h,w1,h1,vlaues,imgPath,))

    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()

    pr1.join()
    pr2.join()
    pr3.join()
    pr4.join()

    # 开始合并四个进程生成的图
    path1=imgPath.lower().replace('.jpg','-1.jpg').replace('.png','-1.png').replace('.jpeg','-1.jpeg').replace('.gif','-1.gif')
    path2=imgPath.lower().replace('.jpg','-2.jpg').replace('.png','-2.png').replace('.jpeg','-2.jpeg').replace('.gif','-2.gif')
    path3=imgPath.lower().replace('.jpg','-3.jpg').replace('.png','-3.png').replace('.jpeg','-3.jpeg').replace('.gif','-3.gif')
    path4=imgPath.lower().replace('.jpg','-4.jpg').replace('.png','-4.png').replace('.jpeg','-4.jpeg').replace('.gif','-4.gif')
    im1=Image.open(path1)
    im2=Image.open(path2)
    im3=Image.open(path3)
    im4=Image.open(path4)

    target = Image.new('RGB', (w, h), (255, 255, 255)) # 合并的图像

    temp = im1.resize((w1, h1), Image.ANTIALIAS)
    target.paste(temp, (0, 0, w1, h1))

    temp2 = im2.resize((w-w1, h1), Image.ANTIALIAS)
    target.paste(temp2, (w1, 0, w, h1))

    temp3 = im3.resize((w-w1, h1), Image.ANTIALIAS)
    target.paste(temp3, (0, h-h1, w1, h))

    temp4 = im4.resize((w-w1, h-h1), Image.ANTIALIAS)
    target.paste(temp4, (w-w1, h-h1, w, h))

    target.show()
    path5=imgPath.lower().replace('.jpg','-rgb.jpg').replace('.png','-rgb.png').replace('.jpeg','-rgb.jpeg').replace('.gif','-rgb.gif')
    target.save(path5)

    if os.path.exists(path1):
        os.remove(path1)
    if os.path.exists(path2):
        os.remove(path2)
    if os.path.exists(path3):
        os.remove(path3)
    if os.path.exists(path4):
        os.remove(path4)

    print("结束")

##############################################################################################################################

if __name__=='__main__':
    loadModule() # 加载模型数据

    ticks = time.time() #运行开始之前，获得当前时间(用来结束的时候获取解析总用时)

    main('D:/218861.jpg',vlaues)

    ticks2 = time.time() #运行结束之后，获得当前时间
    print("单张图用时：",ticks2-ticks,"秒")
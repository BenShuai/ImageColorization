from PIL import Image,ImageDraw
import time,threading


thisImgSrc='D:/homeSec1-2.jpg'

im=Image.open(thisImgSrc) #打开的图像对象
w=im.width # 原图的宽
h=im.height # 原图的高

w1=int(w/2)
h1=int(h/2)

imR=Image.new('RGB', (w, h), (255, 255, 255))
drawR = ImageDraw.Draw(imR)



def rToImg1():
    for x in range(w1):
        for y in range(h1):
            cur_pixel = im.getpixel((x, y)) # 获得图像的rgba值
            # print(cur_pixel)
            drawR.ellipse((x,y,x+1,y+1), fill = (cur_pixel[0],0,0)) # 画一个红色的圆圈，覆盖掉顶部圆球

def rToImg2():
    for x in range(w-w1):
        for y in range(h1):
            cur_pixel = im.getpixel((w1+x, y)) # 获得图像的rgba值
            # print(cur_pixel)
            drawR.ellipse((w1+x,y,w1+x+1,y+1), fill = (cur_pixel[0],0,0)) # 画一个红色的圆圈，覆盖掉顶部圆球





def main():
    # imL=im.convert('L') # 灰度图
    # imL.show()
    # for x in range(w):
    #     for y in range(h):


    # imI=im.convert('I') # 单通道图   I = R * 299/1000+ G * 587/1000 + B * 114/1000
    # imI.show()


    t1 = threading.Thread(target=rToImg1, args=())
    t2 = threading.Thread(target=rToImg2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    imR.show()

    while(1):
        pass



if __name__=='__main__':
    ticks = time.time() #运行开始之前，获得当前时间(用来结束的时候获取解析总用时)

    main()

    ticks2 = time.time() #运行结束之后，获得当前时间
    print("用时：",ticks2-ticks,"秒")

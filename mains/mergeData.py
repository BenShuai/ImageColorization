# author:SunShuai
### module模型数据清洗

import time

moduleFilePath='./module/'
vlaues=[[] for i in range(256)]

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
            vlaues[int(lineNum[0])].append(lineNumRgb)
    finally:
        f.close()

    # f2 = open(moduleFilePath+'L2.module', 'r')
    # try:
    #     while True:
    #         line = f2.readline()
    #         if not line:
    #             break
    #         # print(line)
    #         lineNum=line.split('=')
    #         # print(lineNum)
    #         lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
    #         # print(lineNumRgb)
    #         vlaues[int(lineNum[0])].append(lineNumRgb)
    # finally:
    #     f2.close()
    #
    # f3 = open(moduleFilePath+'L3.module', 'r')
    # try:
    #     while True:
    #         line = f3.readline()
    #         if not line:
    #             break
    #         # print(line)
    #         lineNum=line.split('=')
    #         # print(lineNum)
    #         lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
    #         # print(lineNumRgb)
    #         vlaues[int(lineNum[0])].append(lineNumRgb)
    # finally:
    #     f3.close()
    #
    # f4 = open(moduleFilePath+'L4.module', 'r')
    # try:
    #     while True:
    #         line = f4.readline()
    #         if not line:
    #             break
    #         # print(line)
    #         lineNum=line.split('=')
    #         # print(lineNum)
    #         lineNumRgb=(lineNum[1].replace('(','').replace(')','').replace(' ','').replace('\n','')).split(',')
    #         # print(lineNumRgb)
    #         vlaues[int(lineNum[0])].append(lineNumRgb)
    # finally:
    #     f4.close()

    ticks2 = time.time() #运行结束之后，获得当前时间
    print(vlaues)
    print("加载module数据结束用时：",ticks2-ticks,"秒")

    print("开始数据清洗")
    ticks3 = time.time() #获得当前时间
    for i in range(len(vlaues)):
        # print(vlaues[i])
        dValues=vlaues[i];
        dValues2=[]
        for j in range(len(dValues)):
            flag=0
            for k in range(len(dValues2)):
                if dValues[j][0]==dValues2[k][0] and dValues[j][1]==dValues2[k][1] and dValues[j][2]==dValues2[k][2]:
                    flag=1
                    break
            if flag==0:
                dValues2.append(dValues[j])
        # print(dValues2)
        vlaues[i]=dValues2

    ticks4 = time.time() #获得当前时间
    print("数据清洗结束用时：",ticks4-ticks3,"秒")


    print("清洗数据结果存储开始")
    ticks5 = time.time() #获得当前时间
    # print(vlaues)
    f = open(moduleFilePath+'all.module', 'a') # 以追加的方式进行文件写入（文件不存在的时候会创建新的文件）
    for g in range(len(vlaues)):
        dValues=vlaues[i];
        for j in range(len(dValues)):
            f.write("%s=%s\n" % (g,dValues[j]))# 写入文件
    f.close()
    ticks6 = time.time() #获得当前时间
    print("清洗数据结果存储结束用时：",ticks6-ticks5,"秒")
##############################################################################################################################


loadModule()

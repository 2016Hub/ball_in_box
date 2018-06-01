import math
import random

pointlist = []
R = []
Result = []
def pointgetter():
    i = 0
    j = 0
    for i in range (1,1000):
        for j in range (1,1000):
            pointlist.append((-1+i*0.002,-1+j*0.002))

def distance(x, y, a, b):

    return math.sqrt((x - a) * (x - a) + (y - b) * (y - b))

def check_and_del(x,y,R_index):
    i = 0
    L = len(R)
    for i in range(0,L):
        if i == R_index:
            continue
        a = pointlist[i][0]
        b = pointlist[i][1]
        #print (distance(x, y, a, b),(R[i] + R[R_index]))
        if distance(x, y, a, b) < (R[i] + R[R_index]):
            R[i] = 0
    R[R_index]=0            
        
        
def ball_in_box(ballnum,blocks):
    #先将圆心定好
    pointgetter()
    #先不考虑圆之间的距离,将可能的最大圆全部找出
    for (x,y) in pointlist:
        dis = []
        for (a,b) in blocks:
            dis.append(distance(x, y, a, b))
        dis = dis + [min(abs(1-x),abs(1-y),abs(x+1),abs(y+1))]
        R.append(min(dis))
    #根据圆的个数，将圆选中加入结果并除去被此圆覆盖的圆
    j = ballnum
    ri = 0
    while j > 0:
        ri = R.index(max(R))
        x = pointlist[ri][0]
        y = pointlist[ri][1]
        r = R[ri]
        Result.append((x,y,r))
        check_and_del(x,y,ri)
        j = j - 1
    return Result

    


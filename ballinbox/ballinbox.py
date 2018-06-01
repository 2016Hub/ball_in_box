# -- coding: utf-8 --
import math
import random

"""
算法分析：将矩形方框分成n*n份，得到（n-1）*（n-1）个坐标点；
找到每个点满足在圆内和不覆盖障碍点的条件的最大半径，即找到每个点到障碍点和边界距离的最小值；
然后找到具有最大半径的坐标点作为圆心坐标点并加入到结果；
每找到一个圆的同时删去覆盖到的坐标点（将半径置零），即删去到圆点的距离小于两点半径之和的坐标点。
"""

d=1000
eps=(1-(-1))/d
pointlist = []
R = []
Result = []
def pointgetter():
    i = 0
    j = 0
    for i in range (1,d):
        for j in range (1,d):
            pointlist.append((-1+i*eps,-1+j*eps))

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

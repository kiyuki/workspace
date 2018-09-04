import math
def getCirPoint(a,b,c, x1,y1,r):
    distance = math.fabs(a*x1 + b*y1+ c)/math.sqrt(a**2+ b**2)
    d = math.fabs(a*x1+ b*y1+c)
    lineVer = math.sqrt(a**2 + b**2)
    hx = x1-a*d/(a**2 + b**2)
    hy = y1-b*d/(a**2 + b**2)
    hq = math.sqrt(r**2 - (d**2/(a**2+b**2)))
    x = (hx + hq*b/lineVer, hx - hq*b/lineVer)
    y = (hy - hq*a/lineVer, hy + hq*a/lineVer)
    print(x)
    print(y)

temp = input().strip().split()
c = [float(i) for i in temp]
getCirPoint(c[0], c[1], c[2], c[3], c[4], c[5])

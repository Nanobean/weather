# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:10:24 2018

@author: 73902
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean,ptp,var,std
import seaborn as sns
os.chdir('D:\python')

we = pd.read_csv("mergedData.csv")
year=we['Year']
bridcode=we['AOU']
bridnum=we['SpeciesTotal']
date = pd.DataFrame({
        'year':year,
        'num':bridnum,
        'code':bridcode
        })



cyn= pd.DataFrame(date['num'].groupby([date['code'],date['year']]).sum())
#不同地区求和，按照物种先编号后年进行分类

ycn= pd.DataFrame(date['num'].groupby([date['year'],date['code']]).sum())
#不同地区求和，按照先年后物种编号分类

cynfile= pd.ExcelWriter('c-year-numfile.xlsx')
cyn.to_excel(cynfile,'page_1',float_format='%.5f')
cynfile.save()
ycnfile= pd.ExcelWriter('y-code-numfile.xlsx')
ycn.to_excel(ycnfile,'page_1',float_format='%.5f')
ycnfile.save()
#把分类好的数据存储成excel出来




#正式处理
#列表生成

def listgroup(ind,x,y):
     xlist=[]
     ylist=[]
     i=0
     newxlist=[]
     newylist=[]
     o=len(x)
     for i in range(0,o):
        if i==o-1:         
            xlist.append(x[i])
            ylist.append(y[i])
            newxlist.append(xlist)
            newylist.append(ylist)
        else:
            if i==0:
                 xlist.append(x[i])
                 ylist.append(y[i])
            elif pd.notnull(ind[i+1]):
               xlist.append(x[i])
               ylist.append(y[i])
               newxlist.append(xlist)
               newylist.append(ylist)
               xlist=[]
               ylist=[]
            else:
               xlist.append(x[i])
               ylist.append(y[i]) 
            
            
     return(newxlist,newylist)
yn= pd.read_excel('c-year-numfile.xlsx')


ynyear=[]
ynnum=[]

ynyear,ynnum=listgroup(yn['code'],yn['year'],yn['num'])     
i=0
fig=plt.figure()
ax1=fig.add_subplot(111)

for i in range(0,len(ynyear)):
    
    ax1.plot(ynyear[i],ynnum[i],color='0.5')


#第二y轴
cn= pd.read_excel('y-code-numfile.xlsx')
x=[]
y=[]
x,y=listgroup(cn['year'],cn['code'],cn['num'])

ax2=ax1.twinx()
ax2.plot(range(1966,2018),list(map(meann,y)),color='r')
plt.show
plt.xticks(range(1966,2018))
#x轴的刻度
plt.rcParams['figure.figsize'] = (32.0, 16.0)
#尺寸
list(map(varr,y))

plt.plot(range(1966,2017),list(map(cvv,y)))

def summ(Data):
    sumdata=0
    for i in range(len(Data)):
        sumdata=Data[i]+sumdata
    return sumdata

def varr(Data):  
    sumdata=0
    n=len(set(bridnum))-1
    m=meann(Data)
    for i in range(len(Data)):
        sumdata=np.square(Data[i]-m)+sumdata
    return sumdata/n

def stdd(Data):
    return np.sqrt(varr(Data))


def meann(Data):
    n=(len(set(bridnum)))
    return sum(Data)/n


def cvv(Data):
    return stdd(Data)/meann(Data)


cvv([1,2,3,4,5,6,7,8,9,10])

 
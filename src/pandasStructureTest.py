import numpy as np
import pandas as pd
#pandas的基础是两个数据结构Series和DataFrame。前者是一维数据，后者是多维数据。

#Series的创建方法
print("###############################################################")
print("#########            创建Series，操作Series           ########################")
print("###############################################################")
print("=============1.直接创建，采用默认index(从0开始的数字)======================")
s1 = pd.Series([100,-20,300,0.9])
print(s1)

print("=============2.指定index======================")
s2 = pd.Series([100,-20,300,0.9], index=['a','b','c','d'])  #注意，若index比元素少，则会报错。若index多，则也会报错。
#除非是用字典方式创建Series，此时index多，那没有对应元素的index会被关联上NaN元素
print(s2)

print("=============3.打印index和value======================")
print("index is \n{}".format(s2.index))
print("values is \n{}".format(s2.values))

print("=============4.通过np.array创建Series======================")
a = np.array([100,-20,300,0.9])
s3 = pd.Series(a)
print(s3)
s4 = pd.Series(a,index=['a','b','c','d'])
print(s4)

print("=============5.通过字典创建Series======================")
mydict = {'a':11, 'b':22, 'c':33, 'd':44}
s5 = pd.Series(mydict)
print(s5)

print("=============6.Series的index不能变更，除非通过np.array，字典再重新构建一个Series（但是由于字典已经有了index，所以会有下面的情况）=====================")
print("变更前")
print(s5)
print("在Series上直接变更，会发现，凡是原Series中没有的index都是NaN,而有的index则会是Series的原值")
print(pd.Series(s5,index=['aa','bb','cc','dd','a'])) 
print("用mydict再次生成，会发现，凡是原mydict中没有的index都是NaN,而有的index则会是mydict的原值。与Series上的操作结论一致") 
print(pd.Series(mydict,index=['aa','bb','cc','dd','a']))
print("用较少的index生成一个Series，只具有较少index对应的部分视图（非完整视图）") 
print(pd.Series(mydict,index=['aa','a']))
print("再次打印变更前的Series，会发现没有任何变化，这说明用新的index创建的Series是一个视图而已，在原来的Series中有值的部分，就是原值，没有原值对应的index，就是NaN值")
print(s5)

print("=============6.操作Series中的元素======================")
b = np.array([100,-20,300,0.9])
s6 = pd.Series(b,index=['x1','x2','x3','x4'])
print(s6)
print("==用index定位元素===")
s6['x2'] = 8000
print(s6)
print("==用默认从0开始的下标定位元素===")
s6[1] = 1000
print(s6)
print("==范围选取===")
print(s6[::])
print(s6[1:3])
print(s6[['x3','x1']])  #注意多加了一个括号[]


print("=============7.实验s.copy()创建一个数据副本（非视图）======================")
c = np.array([100,-20,300,0.9])
s7 = pd.Series(c.copy(),index=['xx1','xx2','xx3','xx4'])
s8 = pd.Series(c,index=['xx1','xx2','xx3','xx4'])
print("==c.copy副本方式创建的s7===")
print(s7)
print("==非副本方式创建的s8===")
print(s8)
c[0] = 55555
print("==将np里的array改变后，副本方式创建的s7不受影响===")
print(s7)
print("==将np里的array改变后，非副本方式创建的s8受影响===")
print(s8)

print("=============8.用条件表达式筛选元素======================")
d = np.array([100,-20,300,0.9])
s8 = pd.Series(d,index=['y1','y2','y3','y4'])
print(s8)
print("选择大于0的元素")
print(s8[s8>0])

print("###############################################################")
print("#########            Series上的计算           ########################")
print("###############################################################")
print("=============9.逐元素计算======================")
e = np.array([100,-20,300,0.9])
s9 = pd.Series(e,index=['y1','y2','y3','y4'])
print(s9)
print("=====")
print(s9+1)

print("=============10.np中函数的计算======================")
print(s9)
print("===np.min===")
print(np.min(s9))

print("=============11. 对value的count计算======================")
f = np.array([100,-20,300,0.9,100,300])
s10 = pd.Series(f,index=['y1','y2','y3','y4','y5','y6'])
print(s10)
print("===unique统计不同的value值===")
print(s10.unique())
print("===value_counts()统计每个value值出现的次数===")
print(s10.value_counts())

print("=============12. 两个Series对应元素的计算，对应index的部分一起计算，各自独有的index在结果中都对应NaN======================")
print("s9 is")
print(s9)
print("s10 is")
print(s10)
print("s9+s10 is")
print(s9+s10)


print("###############################################################")
print("#########            Series中NaN的使用           ########################")
print("###############################################################")
print("=============13.直接赋值np.NaN======================")
g = np.array([100,-20,np.NaN,0.9,100,300])
s11 = pd.Series(g,index=['y1','y2','y3','y4','y5','y6'])
print(s11)

print("=============14.isnull()和notnull()判断NaN======================")
print("=====isnull()作为条件来选择元素=====")
print(s11[s11.isnull()])
print("=====notnull()作为条件来选择元素=====")
print(s11[s11.notnull()])








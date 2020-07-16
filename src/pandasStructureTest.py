import numpy as np
from numpy.lib.shape_base import column_stack
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

print("=============9.用isin()判断和选择元素======================")
lll = np.array([100,-20,30,0.9,100,300])
lllSeries = pd.Series(lll,index=['y1','y2','y3','y4','y5','y6'])
print(lllSeries)
print("[100,0.9]是否在Series中")
print(lllSeries.isin([100,0.9]))
print("筛选出来")
print(lllSeries[lllSeries.isin([100,0.9])])

print("###############################################################")
print("#########            Series上的计算           ########################")
print("###############################################################")
print("=============10.逐元素计算======================")
e = np.array([100,-20,300,0.9])
s9 = pd.Series(e,index=['y1','y2','y3','y4'])
print(s9)
print("=====")
print(s9+1)

print("=============11.np中函数的计算======================")
print(s9)
print("===np.min===")
print(np.min(s9))

print("=============12. 对value的count计算======================")
f = np.array([100,-20,300,0.9,100,300])
s10 = pd.Series(f,index=['y1','y2','y3','y4','y5','y6'])
print(s10)
print("===unique统计不同的value值===")
print(s10.unique())
print("===value_counts()统计每个value值出现的次数===")
print(s10.value_counts())

print("=============13. 两个Series对应元素的计算，对应index的部分一起计算，各自独有的index在结果中都对应NaN======================")
print("s9 is")
print(s9)
print("s10 is")
print(s10)
print("s9+s10 is")
print(s9+s10)


print("###############################################################")
print("#########            Series中NaN的使用           ########################")
print("###############################################################")
print("=============14.直接赋值np.NaN======================")
g = np.array([100,-20,np.NaN,0.9,100,300])
s11 = pd.Series(g,index=['y1','y2','y3','y4','y5','y6'])
print(s11)

print("=============15.isnull()和notnull()判断NaN======================")
print("=====isnull()作为条件来选择元素=====")
print(s11[s11.isnull()])
print("=====notnull()作为条件来选择元素=====")
print(s11[s11.notnull()])



#DataFrame的创建方法
print("###############################################################")
print("#########            创建DataFrame           ########################")
print("###############################################################")
print("=============1.用字典创建======================")
data1 = {'color':['blue','green','yellow','red','white'], 'object': ['ball','pen','pencil', 'paper', 'mug'], 'price':[30, 90, 1.5, 300, 8]} 
df1 = pd.DataFrame(data1)
print(df1)

print("=============2.用嵌套字典创建,即可以为每一个元素指定一个键值，这个键值将作为index,出现index没有对应元素的，将自动填充NaN======================")
data2 =  {'color':{'first':'blue', 'second':'green', 'third':'yellow'}, 'object':{'first':'ball', 'second':'pen','fifth':'mug'}, 'price':{'fourth':'300'}}
 #注意index的顺序，会按照第一次遇到的排在前面的方式
df2 = pd.DataFrame(data2)
print(df2)

print("=============3.用np.array.reshape()，然后指定index和columns======================")
data3 = np.arange(15).reshape(5,3)
df3 = pd.DataFrame(data3, index = ['first', 'second', 'third', 'fourth', 'fifth'], columns = ['color','object','price'])
#若不指定index或columns，则默认为是从0开始的数字作为index或columns。
print(df3)

print("###############################################################")
print("#########            选择DF的元素           ########################")
print("###############################################################")
print("=============4.查看index，colums，values======================")
print(df3)
print(df3.index)
print(df3.columns)
print(df3.values)

print("=============5.用['columns_name'][行标范围]的组合选择元素，或['columns_name']['index_name']======================")
print(df3)
print("="*8)
print(df3['color'])

print("="*8)
print(df3['color'][0:2])

print("="*8)
print(df3['color'][4]) #第5行   如果查询结果是一个元素，那么结果就不是Series或DF了。

print("="*8)
print(df3['color']['first']) #first指定的行

print("="*8)
print(df3[1:4]) #要整行就不指定columns即可。取第2行和第4行

print("=============6.用.loc和.iloc进行内部元素的选取，注意下标是要加1，因为把index和columns的内容也算在里面了======================")
#.loc[]：是location，以index（行名）和columns（列名）作为参数,以逗号隔开。行在前，列在后。
#.iloc[]：是index location，以二维矩阵的位置指标（即0,1,2……）作为参数，以逗号隔开。行在前，列在后。
#[]里面可以有个逗号，然后再套两个[]分别表示行列，如果用了冒号表示范围，就不要[]了。
print(df3)
print("=========iloc[]=======")
print("取了第一行，第2到3列。")
print(df3.iloc[[0],1:3]) #取了第一行，第2到3列。注意取某一个行，而不是范围，就要加上一个[]。
print("取第3和5行，第2列到3列")
print(df3.iloc[2:5,1:3])#取第3和5行，第2列到3列，从0开头的下标。
print("取第2列，在行的位置用冒号")
print(df3.iloc[:,[1]])#取第2列，用冒号表示所有。

print("===========================================================")
print(df3)
print("=========loc[]=======")
print("取third那一行，不写列了")
print(df3.loc['third']) #要整行就不指定columns即可
print("取third那一行，用:放在列的位置，表示取所有列。但是跟上面那种取法似乎是转置了，所以尽量不要用上面那种省略行或列不写的方式，会和原DF矩阵转置的。")
print(df3.loc[['third'],:]) #用:放在列的位置，表示取所有列
print("取first和third行，price列")
print(df3.loc[['first','third'],['price']]) 



print("###############################################################")
print("#########            赋值操作           ########################")
print("###############################################################")
print("=============7.赋值单个元素======================")
data6 = {'color':['blue','green','yellow','red','white'], 'object': ['ball','pen','pencil', 'paper', 'mug'], 'price':[30, 90, 1.5, 300, 8]} 
df6 = pd.DataFrame(data6)
print(df6)
print("赋值后,将1行2列的元素改为pingpang")
df6.iloc[[0],[1]] = 'pingpang'
print(df6)

print("=============8.赋值一行元素======================")
print(df6)
print("赋值后,将1行元素修改了")
df6.iloc[[0],:] = ['pink','basketball','1']
print(df6)

print("=============9.赋值一列元素======================")
print(df6)
print("赋值后,将3列元素修改了")
df6.iloc[:,[2]] = np.random.random(5).reshape(5,1)*100
print(df6)

print("=============10.赋值给条件筛选出的元素，在赋值时，尽量用loc或iloc======================")
print(df6)
print("将价格小于70的选出来")
print(df6.loc[df6['price'] <70])   #df6.loc[df6['price']定位的是整行元素，即行标有了。
print("选出来的改为70")
df6.loc[df6['price']<70,['price']] = 70  #要对修改的列的范围进行指定，否则修改的就是整个行里所有的列了。
print(df6)


print("=============11.增加一列，用Series修改一列，删除一列元素======================")
print(df6)
print("增加一列number")
df6['number'] = 100
print(df6)
print("用Series修改一列number")
n = pd.Series(np.linspace(10,100,5))
df6['number'] = n
print(df6)
print("删除一列number")
del df6['number']   #在df6本视图上删除。
print(df6)
print("再增加一列number")
df6['number'] = 100
print(df6)
print("删除一列number，方法2")
ddddd = df6.drop(columns=['number'])   #产生了一个新的视图ddddd。
print(ddddd)


print("=============12.增加一行，用DataFrame修改一行，删除一行元素======================")
print(df6)
print("增加一行")
insertData = np.array(['brown','car',22]).reshape(1,3)
print(insertData)
insertRow = pd.DataFrame(insertData,index = [5], columns = ['color','object','price'])
print(insertRow)
df7 = pd.concat([df6,insertRow],ignore_index = True)   #增加一行必须要组装成DF，然后用concat才行。
print(df7)

print("用DataFrame修改一行,只能删除再添加了，所以这里只测试删除即可")
print("删除一行")
df8 = df7.drop(index = [5]) #仅仅是视图中删除了而已。
print(df8)




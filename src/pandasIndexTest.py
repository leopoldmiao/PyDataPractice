import numpy as np
import pandas as pd

#pandas的index提供了pandas数据结构Series和DataFrame的许多优势。
#index的创建方法
print("###############################################################")
print("#########            创建Index，操作Index           ########################")
print("###############################################################")
print("=============1.创建Index,并取值======================")
s1 = pd.Series(np.arange(6),index = ['white','white','blue','green','green','yellow'])
print(s1)
print("用索引取一个元素或一组元素（Series）")
print(s1['blue'])
print("===============")
print(s1['white'])
print("=============2.获取index的最小和最大值（字母序）======================")
print(s1.idxmin())
print(s1.idxmax())
print("=============3.判断索引是否为唯一性索引======================")
print(s1.index.is_unique)


print("###############################################################")
print("#########            更换索引和删除索引           ########################")
print("###############################################################")
print("=============1.reindex更换索引，从原来的索引取对应元素附加给新索引。若新索引中的索引值是新的，则默认填NaN，也可用method来指定填充方法======================")
s2 = pd.Series(np.arange(6),index = ['pink','white','blue','green','black','yellow'])
print(s2)
print("======注意1：必须为reindex的结果赋予一个新的句柄，因为是产生了一份新的Series对象=========")
print("======注意2：原Series对象的索引必须是unique，否则reindex报错=========")
s3 = s2.reindex(['blue','white','white','green','green','yellow'])
print(s3)

print("==========2.用method参数实现自动索引，前提是索引必须是数字============================")
s4 = pd.Series(np.arange(3),index = [1,2,5])
print(s4)
print("======用method='ffill'填充缺失的索引，索引对应的元素值从前一个索引对应的元素复制过来=========")
s5 = s4.reindex(range(8),method='ffill')  #第一个参数是新的index的范围，先对齐新index与原来index共同的索引值，然后开始从前一个索引对应的元素复制到缺失的位置，如果前面没有已知的元素值，就用NaN。
print(s5)
print("======用method='bfill'填充缺失的索引，索引对应的元素值从后一个索引对应的元素复制过来=========")
s6 = s4.reindex(range(8),method='bfill')
print(s6)

print("==========3.用reindex实现对DataFrame的index和columns进行修改============================")
data1 = {'color':['blue','green','yellow','red','white'], 'object': ['ball','pen','pencil', 'paper', 'mug'], 'price':[30, 90, 1.5, 300, 8]} 
df1 = pd.DataFrame(data1)
print(df1)
print("============================")
#可以看到第4个以后的都是按照method=ffill复制的，而colums的指定，发现可以调整列的顺序，但是新列名不知道是按照什么复制的之前的列值。
df2 = df1.reindex(range(8),method='ffill',columns= ['price','color','object','new1','sup']) 
print(df2)


print("==========4.用drop删除行============================")
print(s1)
print("============================")
print("==========注意，drop返回一个新句柄指向一个新视图，必须用新变量接收句柄和视图，否则原的变量还是没有drop的==================")
s7 = s1.drop(['white']) #重复的index值，是可以一次性删除的。
print(s7)
print("========一次删除两行===============")
s8 = s1.drop(['blue','yellow'])
print(s8)


print("===========5.用drop删除列========================")
print(df1)
print("=======================")
df3 = df1.drop(['price'],axis = 1)
print(df3)


print("###############################################################")
print("#########            算术和数据对齐           ########################")
print("###############################################################")
print("=============1.在Series的算术运算中，要先按照index执行对齐，将index相同的元素进行元素运算，不同的部分置为NaN保留下来======================")
s9 = pd.Series([3,2,5,1],index = ['white','yellow','green','blue'])
s10 = pd.Series([1,4,7,2,1],index = ['white','yellow','black','blue','brown'])
print(s9)
print(s10)
print("=========s9+s10========结果还按照index的字母序进行了排序==")
print(s9+s10)

print("=============2.在DataFrame的算术运算中，要先按照index和column都执行对齐，将index和column都相同的元素进行元素运算，不同的部分置为NaN保留下来======================")
df4 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'], columns=['ball','pen','pencil','paper'])
df5 = pd.DataFrame(np.arange(12).reshape((4,3)), index=['blue','green','white','yellow'], columns=['mug','pen','ball'])
print(df4)
print(df5)
print("===")
print(df4+df5)

print("=============3.采用函数add(),sub(),mul(),div()元素级运算======================")
print("===add()====")
print(df4.add(df5))
print("===sub()====")
print(df4.sub(df5))
print("===mul()===哈达玛积，不是矩阵乘法=")
print(df4.mul(df5))
print("===div()====")
print(df4.div(df5))

print("=============4.DataFrame与Series的运算，加或减======================")
print(df4)
s11 = pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
print(s11)
print("===将DataFrame每一行都减去s11====")
print(df4-s11)
print("=============若Series的index与DataFrame的columns不完全匹配，则不匹配的部分各自保留，置为NaN======================")
s12 = pd.Series(np.arange(4),index=['ball','pen','pencil','paperXXXX'])
print(s12)
print("===将DataFrame每一行都减去s12====")
print(df4-s12)
print("=============再测试一下乘法,还是元素级的相乘======================")
print(df4*s12)



print("###############################################################")
print("#########            各种计算函数           ########################")
print("###############################################################")
print("=============1.np.sqrt(A),sin(),log()等Numpy中的元素级运算函数可以被用于Series和DataFrame结构======================")
print(df5)
print("========np.sqrt(df5)===========")
print(np.sqrt(df5))
print("========np.sin(df5)===========")
print(np.sin(df5))

print("=============2.聚合函数，即对矩阵运算后，结果为一个数值，例如sum(),max(),mean()均值，std()标准差,var()均方差等Numpy中的聚合函数可以被用于Series和DataFrame结构======================")
print(df5)
print("========df5.sum()，默认是axis=0，即在不同行上进行统计===========")
print(df5.sum())
print("========df5.sum(axis=1)，axis=1表示列，即在不同列上进行统计===========")
print(df5.sum(axis=1))

print("=============3.自定义一些函数，然后按照行或列在DataFrame或Series上执行======================")
print(df5)
#定义一个归一化函数
def f(x): #x是一个向量，return的也是一个向量
    return (x-x.mean())/x.std()
print("========df5.apply(f)，默认是axis=0，即在不同行上进行计算，即同一列内部归一化了===========")
print(df5.apply(f))  #可以看到每一列经过标准化后，都是均值为0，标准差为1的分布了。

print("=======df5.apply(f,axis=1)，axis=1，即在不同列上进行计算，即同一行内部归一化了===========")
print(df5.apply(f,axis=1))  #可以看到每一行经过标准化后，都是均值为0，标准差为1的分布了。

print("=============4.DataFrame或Series上的大威力统计函数describe()======================")
print(df5)
print("=====df5.describe()按照每个属性列的数据进行各种特征的统计，例如最大最小值，均值，标准差，分位数等======")
print(df5.describe())


print("###############################################################")
print("#########            排序、排位次           ########################")
print("###############################################################")
print("=============1.sort_index()按照index或columns名称的字母顺序排序，跟元素的值没关系======================")
df6 = pd.DataFrame(np.arange(12).reshape((4,3)), index=['white','blue','green','yellow'], columns=['mug','pen','ball'])
print(df6)
print("===========按照index升序排列================")
print(df6.sort_index())
print("===========按照index降序排列================")
print(df6.sort_index(ascending=False))
print("===========按照columns升序排列================")
print(df6.sort_index(axis=1))
print("===========先按照index，再按照columns升序排列================")
print(df6.sort_index().sort_index(axis=1))

print("=============2.sort_values()按照元素的值排序======================")
print(df6)
print("===========按照pen那一列的值降序排列================")
print(df6.sort_values(by='pen',ascending=False))
print("===========按照blue那一行的值降序排列================")
print(df6.sort_values(by='blue',axis=1, ascending=False))


print("=============3.rank()排位次，即不挪动顺序，而是分配一个名次的值，每个元素都有一个位次值，这个值可以是行角度，也可以是列角度的======================")
print(df6)
print("==========rank(axis=0),行，在不同行之间排序，所以是每一列内部都有一个位次=================")
print(df6.rank(axis=0))
print("==========rank(axis=1),列，在不同列之间排序，所以是每一行内部都有一个位次=================")
print(df6.rank(axis=1))


print("==========rank(axis=1),method的意思是指定位次的计算方法，尤其是在有重复值的时候。=================")
#method若默认，则是用average方式，即重复值的位次要相加除以重复个数，例如元素x有两个，本来一个位次是6，一个位次是7，则average方式认为x的位次是6.5
#method='first'，则是在处理相同元素时，以出现的先后次序分出个先后位次，例如元素x有两个，本来一个位次是6，一个位次是7，则first方式认为第一次出现的x的位次是6，第二次出现的x的位次是7
#method='max'，则是在处理相同元素时，认为相同元素的位次都是选大的值，例如元素x有两个，本来一个位次是6，一个位次是7，则max方式认为第一次出现的x的位次是7，第二次出现的x的位次还是7
#method='min'，则是在处理相同元素时，认为相同元素的位次都是选小的值，例如元素x有两个，本来一个位次是6，一个位次是7，则min方式认为第一次出现的x的位次是6，第二次出现的x的位次还是6
df6.loc[['blue'],['pen']]=3
print(df6)
print("==method='max'==")
print(df6.rank(axis=1,method='max'))

print("###############################################################")
print("#########            相关系数和协方差           ########################")
print("###############################################################")
print("=============1.相关系数corr(),标准化后的协方差，即去除了量纲的影响，只考虑不同变量之间变化的方向是否相关======================")
print(df6)
print("=====df6.corr()=======")
print(df6.corr())

print("=============2.协方差cov()======================")
print(df6)
print("=====df6.cov()=======")
print(df6.cov())


print("###############################################################")
print("#########            NaN值处理           ########################")
print("###############################################################")
print("=============1.赋值np.NaN======================")
df6.loc[['green'],:] = np.NaN  #把green那一行都置为了NaN
df6.loc[:,['pen']] = np.NaN  #把pen那一列都置为了NaN
print(df6)

print("=============2.过滤NaN，删除NaN======================")
print(df6.notna())
print("===dropna()会将所有包含NaN值的行与列都整体删除===")
df7 = df6.dropna() #注意要有一个句柄接收新返回的视图
print(df7)
print("===dropna(how='all')会将全是NaN值的行或列删除，一行或一列中有几个NaN的这种会保留下来===")
print(df6.dropna(how='all'))

print("=============3.为NaN填充其他值======================")
print(df6)
print("=========fillna()==============")
print(df6.fillna(100)) #用100填充所有NaN
print("=========fillna()用字典{'a': 1, 'b': 2, 'b': '3'}指定每个属性列各用什么值替换NaN==============")
print(df6.fillna({'mug':20, 'pen':np.random.random(1)[0], 'ball':666})) #np.random.random(1)[0]产生了只有一个随机数的数组，然后用[0]取出来，但是发现赋值的时候，都是相同的随机数。。。。

print("###############################################################")
print("#########            分层索引           ########################")
print("###############################################################")
print("=============1.在创建时，用index=[[],[]]，可以建立两层索引。注意重复的索引会自动被合并单元格形式的合并显示======================")
cs1 = pd.Series(np.random.rand(8),index=[['white','white','white','blue','blue','red','red','red'],['up','down','right','up','down','up','down','left']])
print(cs1)

print("=============2.利用两层索引选取元素======================")
print(cs1['blue'])
print("========")
print(cs1['blue','up'])
print("========")
print(cs1[:,'up'])

print("=============3.unstack()可以将双层索引的Series变为单层的DataFrame======================")
print(cs1)
print("========")
tmp = cs1.unstack()
print(tmp)

print("=============4.stack()可以将单层的DataFrame变为双层索引的Series======================")
print(tmp)
print("========")
cs2 = tmp.stack()
print(cs2)

print("=============5.创建双层index和双层columns的DataFrame======================")
cs3 = pd.DataFrame(np.random.randn(16).reshape(4,4),index=[['white','white','red','red'],['up','down','up','down']], columns=[['pen','pen','paper','paper'],[1,2,1,2]])
print(cs3)

print("=============6.交换index和columns多层之间的次序======================")
print("先给各个index和columns层起名字，注意用的是xxx.index.names=...., 如果是xxx.index=则对应的是具体的索引值，而不是那一层的名字了")
cs3.index.names= ['colors','status'] #相当于左上角多了一个描述索引和属性列含义的元数据方格
cs3.columns.names = ['objects','id']
print(cs3)
print("交换index的两层")
cs4 = cs3.swaplevel('colors','status')#交换columns和这个用法一样
print(cs4)

print("=============7.按照某个层级进行排序，是指对索引本身按照字母序排序，与元素的大小无关======================")
print(cs3)
print("========")
print(cs3.sort_index(level=0,axis=0))
print("===level=1=====")
print(cs3.sort_index(level=1,axis=0)) #axis=0表示行，不同行之间要排序，因此是对index进行排序，而level=1表示按照第二层status为主进行排序（第一层也会在第二层排序好以后，内部调整一下顺序）。
print("====level='status'====")
print(cs3.sort_index(level='status',axis=0)) #axis=0表示行，不同行之间要排序，因此是对index进行排序，而level='status'与level=1效果一样


print("=============8.按照某个层级进行统计======================")
print(cs3)
print("====cs3.sum(level='colors')====")
print(cs3.sum(level='colors'))
print("====cs3.sum(level='objects',axis=1)=========注意一定要加axis=1,否则报错==========")
print(cs3.sum(level='objects',axis=1))

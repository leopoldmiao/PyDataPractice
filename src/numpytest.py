import numpy as np
#Numpy的基础就是ndarray，一个n维数组对象。对象类型由dtype指定，每个ndarray只有一个dtype，所以ndarray存储都是同质元素。

#利用array函数创建ndarray对象。
a = np.array([1,2,3])
print(a)
print(type(a))#判断a是否一个ndarray对象
print(a.dtype)#a中元素的类型
print(a.ndim)#a的维度，即有几个坐标轴
print(a.shape)#a的形状，输出(3,)第一个参数是轴1的维数，第二个参数是轴2的维数，省略则表示只有一个维数，省略不写了，其实就是(3,1)，3行1列，即创建的a是一个列向量，有3行1列。


print("===========================================")
b = np.array([[1.3, 2.4, 3],[4, 5, 6]])
print(b.dtype)
print(b.ndim)
print(b.shape)  #b是一个2行3列的（2，3），第一个参数是轴1的维数，第一层[]里的元素个数就是轴1的维数，是2。所以第几个轴是按照[]的层数从外到内排序的。
print(b.size)   #所有元素个数
print(b.itemsize) #b中每个元素的大小
print(b.data) #b的缓冲区位置

print("=============dtype选项==============================")
c = np.array([['a','b'],['c','d']])
print(c.dtype)
print(c.dtype.name)

d = np.array([[1.3, 2.4, 3],[4, 5, 6]],dtype=complex)#如果不加dtype=complex，则就默认创建了一个float64的类型ndarray。而加了dtype=complex，就创建的是一个复数的ndarray了。
print(d.dtype)
print(d) #显示[[1.3+0.j 2.4+0.j 3. +0.j][4. +0.j 5. +0.j 6. +0.j]]


print("==================其他创建ndarray的方法 zeros  ones  arange=================================")
e = np.zeros((2,3)) #创建一个2行3列的全0数组
print(e)

f = np.ones((5,1))  #创建一个5行1列的全1数组
print(f)

g = np.arange(4,10) #创建一个[4,10)左闭右开区间范围的数列
print(g)

h = np.arange(0,12,3)   #arange(start=None, stop, step=None, , dtype=None, /)
print(h)

i = np.arange(0, 5,0.5) #步长可以为小数
print(i)

print("=================用arange和reshape创建多维度数组==============================================")
j = np.arange(0, 5, 0.5).reshape(2,5) #reshape成2行5列的数组。
print(j)

print("=================用linspace创建一维序列=====================================")
k = np.linspace(0,10,100) #等距离从0到10中采样100个数据，注意这里的范围包括了10自身。
print(k)

print("==================用random产生random的一维数组，可以再reshape为其他shape===============")
l = np.random.random(10).reshape(2,5)   #random是从0-1中随机
print(l)

print("###############################################################")
print("#########            矩阵运算           ########################")
print("###############################################################")
print("元素级运算")
m = np.arange(0,5)
print("m is {}".format(m))
print("m+5 is {}".format(m+5))   
print("m*5 is {}".format(m*5))

print("=============")
n = np.arange(6,11)
print("m is {}".format(m))
print("n is {}".format(n))
print("m+n is {}".format(m+n))
print("m*n is {}".format(m*n))

print("============sin(),sqrt(),log()等其他元素级运算函数========================")
o = np.linspace(0,100,8).reshape(2,4)
print("o is {}".format(o))
print("np.sin(o) is {}".format(np.sin(o)))
print("np.sqrt(o) is {}".format(np.sqrt(o)))
print("np.log(o) is {}".format(np.log(o)))   #inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷。nan表示缺失值

print("=================矩阵乘积，哈达玛积是a*b，而矩阵乘积是np.dot(a,b)或a.dot(b)================================")
print("m is {}".format(m)) #1行5列
print("n is {}".format(n)) #1行5列
print("n.transpose is {}".format(n.transpose())) #5行1列，但是打印出来还是一位数组，也就是在numpy中，一位数组转置还是一位数组，而且np.dot(m,n.transpose())与np.dot(m,n)结果一样。
#自己在开发的时候就按照正常的矩阵转置理解，结果不会出错，不用管numpy这个对一位数组的特殊对待，反正结果一样。
print("np.dot(m,n) is")
print(np.dot(m,n))
print("np.dot(m,n.transpose()) is")
print(np.dot(m,n.transpose()))
print("m*n is")
print(m*n)

print("================聚合函数，即对矩阵运算后，结果为一个数值，例如sum(),max(),mean()均值，std()标准差,var()均方差等==============")
p = np.random.random(20).reshape(2,10)
print("p is {}".format(p))
print(p.min())
print(p.max())
print(p.sum())
print(p.mean())
print(p.std())
print(p.var())

print("###############################################################")
print("#########            索引，切片，迭代           ########################")
print("###############################################################")
q = np.arange(3,9)
print(q)
print("q[0] is {}".format(q[0]))  #下标从0开始
print("q[2] is {}".format(q[2]))



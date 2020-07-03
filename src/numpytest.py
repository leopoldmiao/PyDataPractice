import numpy as np
from numpy.core.arrayprint import dtype_is_implied
from numpy.lib.npyio import load
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
print("#########            索引，切片           ########################")
print("###############################################################")
q = np.arange(3,9)
print(q)
print("q[0] is {}".format(q[0]))  #下标从0开始
print("q[2] is {}".format(q[2]))
print("q[-2] is {}".format(q[-2])) #负数下标也可以

print("用索引一次获取多个元素，组成一个新的数组,索引列表用中括号（共两层,相当于额外多了一层）括起来即可")
r = q[[0,2,4]]
print(r)

print("用索引获取多维数组，就是用[行下标，列下标]即可")
s = q.reshape(2,3)
print(s)
print("s[1,2] is {},即第二行，第三个元素（下标从0开始）".format(s[1,2]))
print("s[[0,1],[1,2]] is {},即一次取两个元素，分别是[0,1]和[1,2]位置的元素".format(s[[0,1],[1,2]]))

print("==================切片操作，就是用a[n1:n2:x]从数组中抽取一部分构建新数组，n1可以从0开始，n2需要注意是开区间，即a[n2]这个元素不取，x为步长，默认为1========================")
print("再说一遍n2位置的元素不取！！！！！")
print(q)
print("q[1:4] is {},即第2至第4个元素（下标从0开始,q[4]这第五个元素不取，是开区间）".format(q[1:4]))
print("q[1:4:2] is {},即第2至第4个元素,步长为2（下标从0开始，q[4]这第五个元素不取，是开区间）".format(q[1:4:2]))

print("==================二维切片操作，就是用a[n1:n2:x, n3:n4:x]从二维数组中抽取一部分构建新数组，即用逗号隔开分别写行（第一个维度）和列的索引范围========================")
t = np.arange(50).reshape(5,10)
print(t)
print("第2至第4行,第4到第6列，t[1:4, 3:6] is ")
print(t[1:4, 3:6])
print("第2至第4行,第4到第6列,步长为2，t[1:4:2, 3:6:2] is ")
print(t[1:4:2, 3:6:2])

print("###############################################################")
print("#########            迭代           ########################")
print("###############################################################")
print("for循环的迭代")
for ii in t:    #只能以行为单位打印，for只能深入一层。如果要两层，就得用两个for循环。
    print(ii)

for ii in t:   #两层，就得用两个for循环。
    for jj in ii:
        print(jj)

print("flat方式，用一个for循环遍历多维矩阵")
for ii in t.flat:
    print(ii)

print("=============np.apply_along_axis(np.min,axis=0,arr=t)方式遍历执行函数==================")
print(t)
tmp = np.apply_along_axis(np.min,axis=0,arr=t) #axis=0表示按照行进行聚合，即行与行之间进行聚合，即同一个列下标的不同行之间进行聚合。
print("axis=0表示按照行进行聚合，即行与行之间进行聚合，即同一个列下标的不同行之间进行聚合。")
print("result is {}".format(tmp))

print("=============np.apply_along_axis应用自定义函数==========================================")
print(t)
def foo(x):
    return x+1  #元素级运算
tmp = np.apply_along_axis(foo,axis=1,arr=t) #因为是元素级运算，所以axis=0或1,结果都是一样的
print("变化后：")
print(tmp)

print("###############################################################")
print("#########            条件选择构成数组           ########################")
print("###############################################################")
print(t)
print("选出元素是偶数的，构成新数组。即在t[]的中括号内写入选择条件即可，t%2为元素级运算取余数")
tnew = t[t%2==0]
print(tnew)


print("###############################################################")
print("#########            连接和切分数组           ########################")
print("###############################################################")
print("=============连接数组vstack纵向拼接, hstack A|B水平拼接==========================================")
u = np.ones([3,3])
v = np.zeros([3,3])
print(u)
print(v)
print("vstack纵向拼接")
print(np.vstack((u,v)))  #注意括号(u,v)
print("hstack横向拼接")
print(np.hstack((u,v)))
print("注意，如果合并的对象都是一维数组，那么请用column_stack和row_stack，否则用vstack和hstack可能会合并的结果为一个大数组，而不是多维矩阵。")
print("注意，不论用vstack, hstack还是column_stack和row_stack，合并后的数组的元素类型就变为同质的了，就是dtype都是一个，如果有string类型，那么合并后所有元素都是string了")

print("============数组切分vsplit和hsplit是纵向与横向 等分 为几份，split是任意切分（参数更多）==========================================")
w = np.arange(16).reshape(4,4)
print(w)
print("hsplit横向切分")
[w1,w2] = np.hsplit(w,2)
print(w1)
print("////////")
print(w2)

print("vsplit纵向切分")
[w1,w2] = np.vsplit(w,2)
print(w1)
print("////////")
print(w2)


print("split任意切分，np.split(w,[1,3],axis=1), [1,3]表示下刀的位置，刀所在的这一行或一列归后面的部分。axis = 1表示在维度1上进行切分，即按照维度1的不同值进行切开，维度1是列，所以按照不同列切分。")
print(w)
[w1,w2,w3]=np.split(w,[1,3],axis=1)
print(w1)
print("////////")
print(w2)
print("////////")
print(w3)

print("###############################################################")
print("#########            handle视图与副本          ########################")
print("###############################################################")
print("=============注意！！！！Numpy中的任何赋值=运算符(包括切片后得到的每个切片的视图，仅仅是原数据上的视图而已)，都是句柄复制，只是有了一个新视图，而不会产生一个新的数据副本==========================================")
x = np.arange(0,6)
print("x is {}".format(x))
y = x
print("y=x, y is {}".format(y))
x[1]=0
print("x[1]=0后, y 也会变化，y is {}".format(y))

print("==============测试切片，验证不创建新数组==============")
z = np.arange(16).reshape(4,4)
print("z is ")
print(z)
[z1,z2] = np.vsplit(z,2)
print("z1 is")
print(z1)
z[0,0] = 100
print("z[0,0] = 100后, z1也会变化，z1 is")
print(z1)

print("==============测试reshape，验证不创建新数组===============")
print("再次执行z = np.arange(16).reshape(4,4)，就能创造一个新的数组，而不是原来的视图")
z = np.arange(16).reshape(4,4)
print(z)
z3 = z.reshape(2,8)
print("执行z3 = z.reshape(2,8)，同样z3是一个句柄，一个视图而已，数据哪怕shape变了，但是使用的仍然是原来的一份原始数据")
z[0,0] = 20
print("执行z[0,0] = 20，发现z3还是跟着变了，验证了视图的说法。所以Shape仅仅是数据ndarray的一个属性而已，reshape改变了属性，但是并不会创建一个新数组")
print(z3)

print("###############################################################")
print("==============只有copy()显示调用，才能创建一个新的副本数组，而不会再与原数组有关联===============")
arr_a = np.linspace(0,15,16).reshape(4,4) #linspace()等距离采样
print(arr_a)
arr_b = arr_a.copy()
arr_a[0,0] = 101
print("执行arr_a[0,0] = 101，发现arr_b不变")
print(arr_b)


print("###############################################################")
print("#########            结构化数组          ########################")
print("###############################################################")
s1 = np.array(["Tom","Jim","Lucy","Lily","Mary"])
s2 = np.random.random(5)
s3 = np.linspace(80,100,5)
structure_s = np.column_stack((s1,s2,s3))
print(structure_s)
print(structure_s.dtype)

print("从上面可以看到，用vstack之类的合并出来的数组，都是同质的，所以要创建结构化数组，必须重新用np.array()创建")
print("[]列表是结构体的列表，里面的每个元素是一个元组用()表示，每个元组就是一个结构体。")
structure_s = np.array([("123456Tom",80),("Mary",90),("Lucy",90)],dtype=[("name","S6"),("score","int")])
print(structure_s)
print(structure_s.dtype)
print("int表示整型，S6表示长度为6的字符串")
print(structure_s['score']) #可以用dtype指定的列名选取元素。


print("###############################################################")
print("#########            二进制文件读写          ########################")
print("###############################################################")
np.save('saved_data', structure_s)   #自动保存为.npy文件了。
load_data = np.load('saved_data.npy')  
print(load_data)

print("###############################################################")
print("#########            csv文件读写          ########################")
print("###############################################################")
print("建议用pandas")














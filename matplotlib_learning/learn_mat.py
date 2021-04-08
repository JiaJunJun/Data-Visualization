import numpy as np
import matplotlib.pyplot as plt

'''------------------------绘制散点图-------------------------'''
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.random.rand(100) #加random为了让曲线不是一条线，有一定程度的浮动

plt.rcParams['font.sans-serif'] = 'SimHei' # 正常显示中文字体，黑体
plt.rcParams['axes.unicode_minus'] = False # 正常显示纵轴的负号

plt.figure(figsize=(10,5))#画布尺寸
plt.title('sin散点')
plt.scatter(x,y) #绘制散点图
plt.show()

'''------------------------绘制折线图-------------------------'''
x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.random.rand(100)

plt.figure(dpi=120) #根据画布像素调整尺寸
plt.plot(x,y,'r--') #根据坐标点绘制折线图
plt.plot(x,np.sin(x),'g') #根据函数绘制，显示一条曲线
plt.legend(['折线','sin曲线']) #标注
plt.show()

'''------------------------绘制柱状图-------------------------'''
x = range(10)
y1 = np.random.random(10)
y2 = np.random.random(10)

plt.bar(x,y1,facecolor='r') #绘制柱状图
plt.bar(x,-y2,facecolor='g') #绘制x轴下方的柱状图，有时若同时比较两个公司的销售额可能会用到

for i,j in zip(x,y1):  #柱状图字体的显示
    plt.text(i, j, '%.2f'%j, ha='center', va='bottom') #水平居中，垂直方向字体的bottom紧挨图
for i,j in zip(x,y2):
    plt.text(i, -j, '%.2f'%j, ha='center', va='top') #水平居中，垂直方向字体的top紧挨图

plt.title('$\sigma_i=15$') #用$$可写TeX表达式
plt.show()

'''---------------plt.show()---------绘制饼图-------------------------'''
z = np.ones(10)
plt.figure(figsize=(5,5))#正方形
plt.pie(z, autopct='%.2f%%', explode=[0.1]+[0]*9, labels=list('ABCDEFGHIJ'), labeldistance=1.4) #绘制饼图，autopct显示占比,explode突出显示某一份,labels设置标签，labeldistance设置标签距离
plt.show()
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt

con = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8') #读取数据库中的test数据库
tmp1 = pd.read_sql('meal_order_detail1', con=con) #读取meal_order_detail1数据表
#pd.read_sql('select * form meal_order_detail1',con=con) #和上述作用一致，可直接读取表，也可使用select语句
tmp2 = pd.read_sql('meal_order_detail2', con=con)
tmp3 = pd.read_sql('meal_order_detail3', con=con)
data = pd.concat([tmp1,tmp2,tmp3],axis=0) #纵向拼接，数据合并

data['price'] = data['counts'] * data['amounts']#计算收入
ind = pd.DatetimeIndex(data['place_order_time']) #转换为时间格式
data['weekday_name'] = ind.weekday #查看当天是周几
data['day'] = pd.DatetimeIndex(data['place_order_time']).day #转换为第几天
data_gb = data[['day','price']].groupby(by='day') #根据每天分组，筛选价格
number = data_gb.agg(np.sum) #统计每天的销售额

plt.rcParams['font.sans-serif'] = 'SimHei'

plt.scatter(range(1,32),number, marker='D') #绘制销售额的散点图，横轴是1-31日，marker=D表示散点为方形
plt.plot(range(1,32),number) #绘制销售额的折线图，横轴是1-31日
plt.title('2016年8月餐饮销售额趋势示意图')
plt.xticks(range(1,32)[::7],range(1,32)[::7])#设置x轴的刻度和标签，每7天显示一个刻度
plt.xlabel('日期')
plt.ylabel('销售额')
plt.text(number['price'].argmin(), number['price'].min(), '最小值为'+str(number['price'].min())) #显示最小值
plt.show()

data_gb = data[['weekday_name','price']].groupby(by='weekday_name')# 按星期几分组
number = data_gb.agg(np.sum)
ind = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']#按这个顺序排序
#number2 = number.loc[ind, 'price']
plt.bar(number.index, number['price'],width=0.5,alpha=0.5)
plt.xticks(number.index,ind)
plt.title('星期与销售额的数量情况')
for i,j in zip(number.index, number['price']):
    plt.text(i,j,'%i'%j,ha='center',va='bottom')
plt.show()

plt.figure(figsize=(5,5))
plt.style.use('ggplot') #style更好看
plt.pie(number['price'], labels=ind, autopct='%.2f %%',wedgeprops=dict(width=0.6,edgecolor='w'))#wedgeprops可设置环图
plt.title('星期销售额占比情况')
plt.show()

data_gb = data[['order_id','price','day']].groupby(by='day')
def myfun(data):         # 统计每天的销售订单数
    return len(np.unique(data))

number = data_gb.agg({'price':np.sum,'order_id':myfun})
plt.scatter(range(1,32),number['price'],s=number['order_id'])#s表示用order_id的大小控制点的大小
plt.title('订单量、销售额与时间的关系') #通常有三个变量的话用该方法显示，即气泡图
plt.xlabel('时间')
plt.ylabel('销售额')
plt.show()
'''
该程序实现的功能： 每个enrollment_id 开始时间，结束时间，每天活动的数量，平均每天活动的数量
'''
import pandas as pd
import math
#导入数据
df=pd.read_csv('log_train.csv',dtype={'time': str},usecols=[0,3],nrows=1000)
#将1000行的记录保存为csv格式文件
#df.to_csv('dataslice.csv')
group1 = df.groupby('enrollment_id')
#按照enrollment_id来统计分组数量
d = group1.size()
#d的索引长度,4
length = d.size
#循环索引，获得d的对应enrollment-id的元素
s = []
indexs = 0
for i in range(length):
    indexs += d.at[d.index[i]]
    if i!=0:
        s.append(':')
    
    s.append(d.index[i])
    
    if i == 0:
        startTime = df.at[0,'time']
        endTime = df.at[indexs-1,'time']
        s.append(startTime)
        s.append(endTime) 
             
        dayStart = df.at[i,'time'][0:10]
        countEveryday = 0 
        countDays = 0
        countActivity = 0
        for k in range(indexs):  #i->0-313            
             if df.at[k,'time'][0:10] == dayStart[0:10]:
                 countEveryday += 1              
             else:
                 countActivity += countEveryday
#                 print(d.index[i],dayStart,countEveryday)
                 s.append(dayStart)
                 s.append(countEveryday)
                 countDays += 1
                 dayStart = df.at[k,'time'][0:10]
                 countEveryday = 1
                 
#        print('用户',d.index[i],'活动的天数:',countDays) 
        s.append(math.ceil(countActivity/countDays))
#        print('用户',d.index[i],'平均每天的活动量:',math.ceil(countActivity/countDays))
    else:
        startTime = df.at[indexs-d.at[d.index[i]],'time']
        endTime = df.at[indexs-1,'time']
        s.append(startTime)
        s.append(endTime)  
        
        dayStart = startTime[0:10]
        countEveryday = 0
        countDays = 0
        countActivity = 0
        for k in range(indexs-d.at[d.index[i]],indexs):  #i->314-288+314           
             if df.at[k,'time'][0:10] == dayStart[0:10]:
                 countEveryday += 1              
             else:
                 countActivity += countEveryday
#                 print(d.index[i],dayStart,countEveryday)
                 s.append(dayStart)
                 s.append(countEveryday)
                 countDays += 1
                 dayStart = df.at[k,'time'][0:10]
                 countEveryday = 1
#        print('用户',d.index[i],'活动的天数:',countDays)
        s.append(math.ceil(countActivity/countDays))
#        print('用户',d.index[i],'平均每天的活动量:',math.ceil(countActivity/countDays)) 

# print(s)
position = 0
for m in range(len(s)):
    if s[m] == ':':
        print(s[position:m])
        position = m+1
print(s[position:])

#    print(i)#0,1,2,3
#    print(d.index[i])#1,3,4,5
#    print(d.at[d.index[i]])#314,288,99,299
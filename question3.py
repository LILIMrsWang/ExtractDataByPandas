'''
该程序实现的功能：
3.每个enrollment_id problem事件的个数，以及与总事件个数的比值；
4. 每个enrollment_id video事件的个数，以及与总事件个数的比值；
5. 每个enrollment_id access事件的个数，以及与总事件个数的比值；
6. 每个enrollment_id wiki事件的个数，以及与总事件个数的比值；
7. 每个enrollment_id discussion事件的个数，以及与总事件个数的比值；
8. 每个enrollment_id navigate事件的个数，以及与总事件个数的比值；
9. 每个enrollment_id page_close事件的个数，以及与总事件个数的比值；
'''
import pandas as pd
import math
#导入数据,并只用第一行
df=pd.read_csv('log_train.csv',dtype={'time': str},nrows=1000)
#按照enrollment_id来分组
group1 = df.groupby('enrollment_id').size()
#按照event，enrollment_id来统计分组数量
group2 = df.groupby(['enrollment_id','event']).size()
#按照enrollment_id来统计分组数量
print(group2)
print(group2/(group1*2))
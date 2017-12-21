这组数据是一个服务器日志数据，一共有8157277条数据（已经超过了excel的最大行数）。

enrollment_id 由username 和course_id构成，指每个学生上课的学号；
username 指的是学生的姓名；
course_id 指的是课程号；
time 指的是这条日志数据发生的时间；
source 指的是发生日志数据产生源（server或者browser）
event 指的是发生日志事件(有7种)
object 指其他事件

现在需要使用pandas http://pandas.pydata.org  提取特征值
数据源：log_train.csv 网盘文件下载地址：https://pan.baidu.com/s/1hsCMU6S

1. 每个enrollment_id 事件总数；
2. 每个enrollment_id 开始时间，结束时间，每天活动的数量，平均每天活动的数量（question2.py）
3. 每个enrollment_id problem事件的个数，以及与总事件个数的比值；
4. 每个enrollment_id video事件的个数，以及与总事件个数的比值；
5. 每个enrollment_id access事件的个数，以及与总事件个数的比值；
6. 每个enrollment_id wiki事件的个数，以及与总事件个数的比值；
7. 每个enrollment_id discussion事件的个数，以及与总事件个数的比值；
8. 每个enrollment_id navigate事件的个数，以及与总事件个数的比值；
9. 每个enrollment_id page_close事件的个数，以及与总事件个数的比值；

最后，按照提取的特征做成特征矩阵（用numpy）
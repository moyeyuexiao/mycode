import pymysql
import time
db=pymysql.connect(host="127.0.0.1", user="shisi@666", password="7egtzdvXM7qsLckD", database="cmq", charset='utf8')
cursor=db.cursor()
sql="INSERT INTO cmq_main (id, get_time, visibilityTimeout, maxMsgHeapNum, maxMsgSize, msgRetentionSeconds, pollingWaitSeconds, activeMsgNum, inactiveMsgNum, createTime, lastModifyTime, QueueName, rewindSeconds, rewindmsgNum, minMsgTime, delayMsgNum) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),'hh2','hh3','hh4','hh5','hh6','hh7','hh8','hh9','hh10','hh11','hh12','hh13','hh14','hh15')
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
db.close()

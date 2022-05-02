# 创建队列 eg.

from cmq.cmq_api import CmqApi
import re
import pymysql
import time

queue_name = "saomiaoqi_migrate_queue"
cmq_api = CmqApi()
#res = cmq_api.createQueue(queue_name)

queue_list = cmq_api.get_queue_list()                
print(queue_list)
#[{'queueId': 'queue-gm8ro4vu', 'queueName': 'saomiaoqi_migrate_queue'}, {'queueId': 'queue-83imf35c', 'queueName': 'zxwk_queue'}, {'queueId': 'queue-l0us9rxa', 'queueName': 'knsq_queue'}, {'queueId': 'queue-2pbjnbo6', 'queueName': 'jiema_life'}, {'queueId': 'queue-c1l0h9so', 'queueName': 'jiema_projs'}, {'queueId': 'queue-1yos3etu', 'queueName': 'biz_official_website_result'}, {'queueId': 'queue-50qawezc', 'queueName': 'biz_mobilephone_result'}, {'queueId': 'queue-51g00p8e', 'queueName': 'biz_mobilephone'}, {'queueId': 'queue-c48cwyze', 'queueName': 'biz_official_website'}, {'queueId': 'queue-0tzsytuk', 'queueName': 'online_education_queue'}, {'queueId': 'queue-5gi3yq1c', 'queueName': 'maochi_phones_data'}, {'queueId': 'queue-ihvpxvbk', 'queueName': 'lz_data'}, {'queueId': 'queue-lbxa20zg', 'queueName': 'lz_software'}, {'queueId': 'queue-ii1r4840', 'queueName': 'laoge_luntan_queue'}, {'queueId': 'queue-fk3p7ltk', 'queueName': 'tousu_heimao_queue'}, {'queueId': 'queue-kx52hqpm', 'queueName': 'tousu_ju_queue'}, {'queueId': 'queue-m8yy3d5g', 'queueName': 'test'}, {'queueId': 'queue-0ixx4r8w', 'queueName': 'xianbao_migrate_queue'}, {'queueId': 'queue-hqs62vg8', 'queueName': 'order_id'}, {'queueId': 'queue-7g8o9kus', 'queueName': 'oschina_queue'}]
gettime=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
for i in queue_list:

    #res = cmq_api.get_queue_attributes(queue_name)
    res = cmq_api.get_queue_attributes(i["queueName"])
    temp=str(res)
    hh=re.split('\n|:',temp)
    visibilityTimeout=hh[1]
    maxMsgHeapNum=hh[3]
    maxMsgSize=hh[5]
    msgRetentionSeconds=hh[7]
    pollingWaitSeconds=hh[9]
    activeMsgNum=hh[11]
    inactiveMsgNum=hh[13]
    createTime=hh[15]+":"+hh[16]+":"+hh[17]
    lastModifyTime=hh[19]+":"+hh[20]+":"+hh[21]
    QueueName=hh[23]
    rewindSeconds=hh[25]
    rewindmsgNum=hh[27]
    minMsgTime=hh[29]
    delayMsgNum=hh[31]
    db=pymysql.connect(host="127.0.0.1", user="shisi@666", password="7egtzdvXM7qsLckD", database="cmq", charset='utf8')
    cursor=db.cursor()
    sql="INSERT INTO cmq_main (id, get_time, visibilityTimeout, maxMsgHeapNum, maxMsgSize, msgRetentionSeconds, pollingWaitSeconds, activeMsgNum, inactiveMsgNum, createTime, lastModifyTime, QueueName, rewindSeconds, rewindmsgNum, minMsgTime, delayMsgNum) VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (gettime,visibilityTimeout, maxMsgHeapNum, maxMsgSize, msgRetentionSeconds, pollingWaitSeconds, activeMsgNum, inactiveMsgNum, createTime, lastModifyTime, QueueName, rewindSeconds, rewindmsgNum, minMsgTime, delayMsgNum)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.close()
    


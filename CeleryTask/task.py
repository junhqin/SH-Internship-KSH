from __future__ import absolute_import
import json
from keshihua.celery import app
from datetime import datetime
from demo.pachong import  new_job
from demo.graph import avg_salary,lan_fre,bar_job,job_cate,jieba_count

# 数据更新
@app.task
def start_get_data():
    print('正在获取并更新数据...')
    count=new_job()
    print('处理专业薪资图中...')
    avg_salary()
    print('处理语言使用情况图中...')
    lan_fre()
    print('处理技术块状图中...')
    bar_job()
    print('处理岗位饼图..')
    job_cate()
    jc = jieba_count()



    nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('demo/data/UpdateTime.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps({
            'code': 200,
            '数据获取时间': nowtime,
            '数据量':count,
            '词云数据量':jc
        }, ensure_ascii=False, indent=4))
    print('获取完毕数据已更新!')
    print('更新时间:' + nowtime)
    with app.connection() as conn:
        conn.default_channel.queue_purge(queue='celery')


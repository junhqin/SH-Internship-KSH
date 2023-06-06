import pandas as pd  # 读取csv
import jieba  # 用于分词
import jieba.analyse
import re  # 匹配词频，清洗数据
import json
import sqlite3
import numpy as np
import os
from PIL import Image  # 导入图片
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, wordcloud
import matplotlib.pyplot as plt  # 展示图片
import collections  # 词频统计库
import seaborn as sns
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey
from pyecharts.charts import Sankey
from pyecharts import options as opts
########################################################################################
#薪资与学位关系
def avg_salary():
    # 连接数据库文件
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM job")
    rawData = cur.fetchall()

    # print("Total rows:", cur.rowcount)
    degrees = ['大专', '本科', '硕士', '不限']
    dict = {'大专': [], '本科': [], '硕士': [], '不限': []}
    first_regexs = ["([0-9]*)"]

    salary = []

    for i in range(len(rawData)):
        sentence = rawData[i][3]
        if(len(sentence)<=2):
            continue
        for pat in first_regexs:
            result = re.findall(pat, sentence)

            search_degree = None
            for degree in degrees:
                tmp = re.search(degree,rawData[i][5])
                if tmp:
                    search_degree = degree
                    break
            if search_degree == None :
                search_degree = '不限'
            for res in result:
                if (len(res) >= 2):
                    salary.append(float(res))
                    dict[search_degree].append(float(res))


    salary = [float(i) for i in salary]
    avg = {}
    for key, value in dict.items():
         avg[key] = len(value), sum(value) / len(value)
    #  总体

    avg['total'] = len(salary), sum(salary) / len(salary)
    #
    with open("./demo/data/avg_salary.json", "w", encoding='utf-8') as f:
        # json.dump(dict, f)  # 写为一行
        json.dump(avg, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行


#语言使用率,漏斗图
def lan_fre():
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM job")
    rawData = cur.fetchall()
    first_regexs = [r'(.*)工程师', r'(.*)实习生', r'(.*)开发']
    language_sentence = []
    for position in rawData:
        language_sentence.append(position[1] + position[8])

    reg = r'[a-zA-Z\+\#]*'

    arr = []

    for require in language_sentence:
        result = re.findall(reg, require)
        if(result):
            for i in result:
                tmp = i.upper()#全部转化为大写
                if len(tmp) >= 1:
                    arr.append(tmp)

    word_counts = collections.Counter(arr)




    application = ['JAVA', 'PYTHON', 'C++', 'HTML', 'JAVASCRIPT', 'CSS', 'MYSQL', 'UNITY', 'C#', 'IOS',
                           'GOLANG', 'SHELL', 'PHP']
    jsonData = {}
    for i in application:
        jsonData[i] = word_counts[i]
    jsonData['JAVASCRIPT'] += word_counts['JS']
    jsonData['GOLANG'] += word_counts['GO']
    array = []
    for a, b in jsonData.items():
        array.append({'value': b, 'name': a})


    with open("./demo/data/language.json", "w", encoding='utf-8') as f:
        # json.dump(dict_, f)  # 写为一行
        json.dump(array, f, indent=2, sort_keys=False, ensure_ascii=False)  # 写为多行

def bar_job():
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM job")
    rawData = cur.fetchall()
    first_regexs = [".*熟悉(.*)", ".*精通(.*)", ".*了解(.*)", "掌握(.*)"]
    match_sentence = []
    for i in range(len(rawData)):
        sentence = rawData[i][8]
        word_list = [i for i in sentence.split('\n')]  # 以换行符进行分割
        for sen in word_list:  # 匹配含有“熟悉，精通，了解的关键词”
            sen = sen.upper()
            if (len(sen) <= 1):
                continue
            for pat in first_regexs:

                result = re.search(pat, sen)
                if result:
                    match_sentence.append(result.group(1))
    # 除去无用信息
    second_regexs = [
        "[优化|优先|应用|一种|具有|能够|不限|数种|对|常见|使用|设计|编写|参与|理解|有|掌握|如|设计|包括|了解](.*)(，|。|；)",
        "(，|。|；)(.*)[相关|等|一定|基础|工具|习惯|优先|相关| \
                     经验|语言|框架|能力|流程|产品|数据库|应用|基础|优先考虑|模型|基本|\
                     服务器|原理|基础知识|项目|操作|模式|规范|方法|平台|更佳]",
        ]
    match_sentence_sec = []
    for i in range(len(second_regexs)):
        pat = second_regexs[i]
        for sen in match_sentence:
            result = re.finditer(pat, sen)
            if (result and i == 0):
                for j in result:
                    match_sentence_sec.append(j.group(1))
            elif (result and i == 1):
                for j in result:
                    match_sentence_sec.append(j.group(2))
                continue
    match_sentence_thi = []
    third_regexs = ["优先", "框架", "编程", "语言", "常用", '常见', '一种', '流程', '使用', "主流", '分项', '快速',
                    '意识', ' 岗位', '提供',
                    '经验', '熟练', '熟悉', '应用', '学习', '设计', '基础知识', '能力', '优化', '逻辑思维', '行业',
                    '办公', '工程', '自我', '版本',
                    '了解', '基本', '知识', '基础', '至少', '基本操作', '更佳', '一门', '抗压', '解决', '公司',
                    '优秀者', '表现', '驱动', '兼容性', '钻研', '本科生',
                    '组件', '扎实', '限于', '理解', '平台', '具备', '深度', '良好', '习惯', '调试', '管理', '兴趣',
                    '或者', '时间', '例如', '半年', '弹性', '目标', '勤奋',
                    '方法', '理论', '数种', '工具', '原理', '相关', '一定', '能够', '深入', '10', '客户', '体验',
                    '承受', '提升', '协调', '有者', '交付', '日常', '数字化', '敏捷', '业界',
                    '具有', '最好', '有过', '相关', '经有', '硬性规定', '习有', '系统', '产品', '包括', '专业', '协作',
                    '精神', '服务', '质量', '远程', '流式', '营销', '科学', '地址', '社区',
                    '工业', '模块', '上线', '任务', '1999', '72', '28', '研一', '全日制', '过程', '内容', '关系',
                    '主动性', '生产', '流利', '注重', '激情', '定位', '功能', '细节',
                    '社交', '后端', '设备', '课程', '撰 写', '丰富', '商业', '收获', '备注', '深刻', '期间', '简单',
                    '得到',
                    '人力资源', '概念', '加班', '后台', '人员', '监理', '康桥', '证书', '视频', '最新', '无人机',
                    '一个', '星球',
                    '及其', '经有', '类库', '认证', '模型', '底层', '焊接', '模式', '处理', '问题', '互联网', '强烈',
                    '需求', '协助', '一周',
                    '项目', '手工', '架构', '掌握', '软件', '结构', '性能', '交互', '编写', '企业', '机会', '技能',
                    '参与', '用户', '优异者', '以及',
                    '编码', '经有', '实现', '习有', '清晰', '各种', '完成', '结合', '进行', '等备', '以及', '业务',
                    '逻辑', '乐于', '可以', '任职',
                    '硬性', "技术", "代码", '机器', '开源', '个人', '有着', '机械加工', '发现', '出勤', '研究生',
                    '认真负责', '分析', '岗位',
                    '等用', '自主', '定义', '数量', '制式', '方案', '经有', '等备', '习有', '优秀', '本科', '文档',
                    'CODE', '细致', '在读', '实践', '创新', '耐心', '拥有',
                    '实习', '沟通', '团队', '开发', '工作', '每周', '较强', '责任心', '合作', '环境', '热情', '认真',
                    '领域', '有者', '负责', '其他', '好奇心', '责 任感', '获得',
                    '要求', '以上学历', '独立', '考虑', '善 于', '优化', '逻辑思维', '计算机', '积极主动', '踏实',
                    '热爱', '表达', '特克', '连续',
                    '天及', '薪资', '积极', '千寻', '免费', '信息', '协议', '毕业', '持续', '实时', '做事', '人及',
                    '充满', '转正', '同学', '程序', '高度', '员工',
                    '上海', '维护', '思维', '学历', '游戏', '待遇', '落地', '根据', '职位', '培训', '保证', '接受',
                    '研发', '精通', '规范', '以上', '场景', '压力', '交流', '搭建', '留用',
                    '责任感', '背景', '午餐', '健康', '加分', '有限', ' 智能', '挑战', '适应', '硕士', '方向', '思考',
                    '执行力', '浓厚', '发展', '小伙伴', '阅读',
                    '00', '严谨', '氛围', '经历', '211', '30', '思考', '执行力', '浓厚', '发展', '小伙伴', '阅读',
                    '等者', '善于', '福利', '态度', '事业部', '编码',
                    '体系', '愿意', '我们', '智能', '严谨', '氛围', '执行力', '浓厚', '发展', '小伙伴', '阅读', '全勤',
                    ' 写作', '帮助', '理工科', '成长', '通过', '总结', '补贴', '长期',
                    '2023', '180', '晚餐', '页面', '构建', '时长', '集成', '文化', '部署', '在校生', ' 金融', '对于',
                    '各类', '人际交往', '模块化', '全职', '勇于', '小时',
                    '接触', '性格开朗', '电子', '移动', '电路', '大三', '下午茶', '实际', '协同', '学生', '大四',
                    '技巧', '职业', '活动', '细心', ' 配合', '追求',
                    '硬件', '组织', '进取', '接口', '简历', '通信', '研二', '2024', '咨询', '志同道合', '关注', '安排',
                    '前沿', '并发', '指导', '英语口语', '埃森哲',
                    '全球', '院校', '多种', '尝试', '区块', '分享', '自己', '支持', '人工', '品牌', '图像', '部门',
                    '听说读写', '探索', '风格', '导师',
                    '微信', '标准', '功底', '不断', '文字', '事物', '高质量', '视觉', '布局', '需要', '在校', '三天',
                    '运用', '控制', '有者',
                    '咖啡', '基于', '位于', '会 员', '吃苦耐劳', '人才', '乐观', '合格者', '饮料', '好学', '一起',
                    '联调', '如果', '认知', '研究', '任意', '打造',
                    '仪器仪表', '缓存', '学校', '比如', '富有', '命令', '剪辑', '大专', '从事', '2021', '适配', '资格',
                    ' 欢迎', '相应', '故障', '语义', '核心', '中国', '本地', '文案', '查询',
                    '热衷于', '晋升', '乒乓球', '顺畅', '分离', '打卡', '主动', '并且', '导向', '获奖者', '出色',
                    '监控', '有化',
                    '写作', '应届生', '20', '985', '调优', 'POWER', '24'
                    ]

    for sen in match_sentence_sec:
        for i in range(len(third_regexs)):
            pat = third_regexs[i]
            sen = re.sub(pattern=pat, repl="", string=sen, count=0)
        match_sentence_thi.append(sen)
    link_sentence = "".join(match_sentence_thi)
    keywords_textrank = jieba.analyse.textrank(link_sentence, topK=100)
    # print(keywords_textrank)
    # print("\n\n")
    keywords_textrank = jieba.analyse.tfidf(link_sentence, topK=100)
    # print(keywords_textrank)
    top_words = ['PYTHON', '前端', '数据库', 'JAVA', 'C++', 'VUE', '算法', 'LINUX', 'REACT', 'JS', 'SEMI', 'MYSQL',
                  'SQL', '测试', 'WEB', 'JAVASCRIPT', 'GIT', 'GO', 'ANDROID', '自动化', '操作', '网络',
                 '英语', '英文', 'EXCEL', 'CSS', 'HTML', 'HTTP', 'REDIS', '读写', 'TCP', 'SPRING', '多线程', 'API',
                 '存储', 'GOLANG', 'UI', 'IP', '嵌入式', '运营', '浏览器', '安全', 'ORACLE', 'OFFICE', 'DOCKER',
                 'JQUERY', 'NODE', 'WORD', '分布式', 'WEBPACK', '面向对象', 'ANGULAR', 'SHELL', 'PPT',
                 '日语', 'NODEJS', 'PHP', 'ROS', 'APP', 'SIEMENS', 'LOW', 'MYBATIS', 'C#', 'IOS',
                 'ELASTICSEARCH', '脚本', '建模', '可视化', '数学', 'TYPESCRIPT', '竞赛', 'KUBERNETES', 'HTML5',
                 'DJANGO', 'AI', 'MQ', 'HIVE', 'SPARK', 'OPENCV', '金融', 'CSS3', 'HBASE', 'BI', 'ARM',
                 'HTTPS', 'MVC', 'AJAX', 'SOCKET', 'SVN', '内存', '中间件', 'NET', 'SPRINGBOOT']

    top_words_fre = {}
    for i in range(len(top_words)):
        word = top_words[i]
        all_match = re.findall(re.escape(word), link_sentence)
        # 转义C++ C#这种由特殊意义的符号
        num = len(all_match)
        top_words_fre[word] = num

    top_words_fre['英语'] += top_words_fre['英文']
    top_words_fre['英文'] = 0
    top_words_fre.pop('英文')

    # print(top_words_fre)

    jsonData = {}
    cnt = 0
    for key in top_words_fre:
        jsonData[key] = top_words_fre[key]
    with open("./demo/data/job_fre.json", "w", encoding='utf-8') as f:
        json.dump(jsonData, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行

def jieba_count():
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM job")
    rawData = cur.fetchall()
    sentences = ""
    for i in range(len(rawData)):
        sentences += rawData[i][8]

    seq_list = list(jieba.cut(sentences))
    result_list = []
    for word in seq_list:
        if (len(word) > 1):
            result_list.append((word))
    return len(result_list)


def job_cate():
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM job")
    rawData = cur.fetchall()
    first_regexs = [r'(.*)工程师', r'(.*)实习生', ]
    rawCategory = {}
    for i, x in enumerate(rawData):
        tmp = rawData[i][1]
        for reg in first_regexs:
            result = re.search(reg, tmp)
            if result:
                key = result.group(1).upper()
                if key not in rawCategory.keys():
                    rawCategory[key] = 1
                else:
                    rawCategory[key] += 1
                break
    clean = ['后端', '测试', '前端', '游戏', '移动端', '客户端',
             '服务端', '软件', 'C'
                               '量化', '数据', '硬件', '嵌入式', '运维', '算法', '网络'
        , '机器人', 'IOS', 'C++', 'JAVA', 'PYTHON', 'C#', 'UNITY',
             '产品', '安全', '云', 'AI', '电器', 'WEB', '网站',
             'IT', '开发', '研发'
             ]

    category = {}

    for key in rawCategory.keys():
        for reg in clean:
            tmp = re.escape(reg)
            result = re.search(tmp, key)
            if result:
                if reg in category.keys():
                    category[reg] += rawCategory[key]
                else:
                    category[reg] = rawCategory[key]
                rawCategory[key] = 0
                break
    keys = list(rawCategory.keys())
    for k in keys:  # 对字典a中的keys，相当于形成列表list
        if rawCategory[k] == 0:
            del rawCategory[k]
    category['开发'] += category['研发'] + category['服务端'] + category['云']
    category['研发'] = category['服务端'] = category['云'] = 0
    category['后端'] += category['JAVA'] + category['C++'] + category['C#']
    category['JAVA'] = category['C++'] = category['C#'] = 0
    category['数据'] += category['IT'] + category['PYTHON']
    category['IT'] = category['PYTHON'] = 0
    category['前端'] += category['WEB'] + category['客户端'] + category['移动端']
    category['WEB'] = category['网站'] = category['客户端'] = category['移动端'] = 0
    category['前端'] += category['WEB']
    category['WEB'] = 0
    category['硬件'] += category['嵌入式'] + category['机器人']
    category['嵌入式'] = category['机器人'] = 0
    category['游戏'] += category['UNITY']
    category['UNITY'] = 0
    keys = list(category.keys())
    for k in keys:  # 对字典a中的keys，相当于形成列表list
        if category[k] == 0:
            del category[k]

    # for i, j in category.items():
    #     print(i, j)
    jsonData = {}
    a = sorted(category.items(), key=lambda kv: (kv[1], kv[0]))
    # print(a)
    for i in sorted(category.items(), key=lambda kv: (kv[1], kv[0])):
        jsonData[i[0]] = i[1]
        # print ((i, category[i]), end =" ")

    array = []
    for i in sorted(category.items(), key=lambda kv: (kv[1], kv[0])):
        array.append({'name': i[0], 'value': i[1]})

    with open("./demo/data/job_category.json", "w", encoding='utf-8') as f:
        # json.dump(dict_, f)  # 写为一行
        json.dump(array, f, indent=2, sort_keys=False, ensure_ascii=False)  # 写为多行





if __name__=='__main__':
    pass
    # avg_salary()
    # lan_fre()
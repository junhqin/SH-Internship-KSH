import copy
import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Line, Map, Timeline, Pie, Bar
from pyecharts import options as opts
from pyecharts.charts import Sankey
from pyecharts.globals import ThemeType
import sqlite3
import re


def sangshen():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # conn = sqlite3.connect("../data.db")
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM job")
    # rawData = cur.fetchall()
    #
    # first_regexs = [r'(.*)工程师', r'(.*)实习生', ]
    # rawCategory = {}
    # for i, x in enumerate(rawData):
    #     tmp = rawData[i][1]
    #     for reg in first_regexs:
    #         result = re.search(reg, tmp)
    #         if result:

    data = pd.read_excel('数据源.xls')
    data['薪资'] = data['薪资'].str.replace('元', '')
    data['薪资'] = data['薪资'].str.replace('/天', '')
    data['薪资'] = data['薪资'].apply(lambda x: (int(x.split('-')[0]) + int(x.split('-')[1])) / 2 if '-' in x else x)
    data = data.rename(columns={'工作地点': '地区', '岗位名称': '岗位'})
    # 将闸北区更换成静安区
    data['地区'].replace('闸北区', '静安区', inplace=True)
    # 将不在指定地区列表中的地区替换成其他
    other_regions = ['浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区', '虹口区', '杨浦区', '普陀区', '闵行区',
                     '宝山区', '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区']
    data['地区'].mask(~data['地区'].isin(other_regions), '其他', inplace=True)


    #将不在指定岗位的工作去除
    specified_positions = ['开发', '运维','游戏','硬件','网络', '算法', '数据', '软件', '前端', '后端','管理','产品','测试', '安全'] # 指定的岗位列表
    data = data[data['岗位'].str.contains('|'.join(specified_positions))]


    count = data.groupby(["岗位", "地区"]).size()
    result = count.to_frame(name="数量").reset_index()
    cross = pd.MultiIndex.from_product([result["岗位"].unique(), result["地区"].unique()], names=["岗位", "地区"])
    result = result.set_index(["岗位", "地区"]).reindex(cross, fill_value=0).reset_index()
    result = result.sort_values(["岗位", "地区"])
    result.insert(loc=0, column='地区', value=result.pop('地区'))
    result = result[result['数量'] != 0]
    result = result.reset_index(drop=True)
    customer_level = result
    # 创建nodes
    node_contents = sorted(list(set(customer_level['地区'].tolist() + customer_level['岗位'].tolist())))
    nodes = [{'name': x} for x in node_contents]
    # 创建links
    links = [{'source': x, 'target': y, 'value': z} for x, y, z in
             zip(customer_level['地区'], customer_level['岗位'], customer_level['数量'])]
    # 创建桑基图
    sankey = (
        Sankey(init_opts=opts.InitOpts(width="100%", height="6000px"))
        .add(
            series_name='',
            nodes=nodes,
            links=links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.4, color="source"),
            label_opts=opts.LabelOpts(position="up"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="上海市地区与岗位关系展示"),
        )
    )
    return sankey.dump_options_with_quotes()




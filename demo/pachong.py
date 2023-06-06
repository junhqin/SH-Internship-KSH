import datetime
import json
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from lxml import etree
import sqlite3



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# con = create_engine("mysql+mysqlconnector://root@localhost:3306/ksh")
def pj(m):
    n = ''
    for i in m:
        a = i.strip()
        if a:
            n+=a
    return n


def new_job():
    with open('实习僧2.csv', 'w', newline='', encoding='utf-8') as f:
        # 保存第一行数据-字段
        f.write('岗位名称,公司名称,薪资,岗位描述,工作地点,学历,工作时长,实习时长\n')
        # 遍历翻页
        for p in range(1, 2):
            # 打印页数，方便观察
            print(f'===============================================!这是第{p}页!============================================')
            # 传值
            # 请求头
            url1 = "https://www.shixiseng.com/interns"
            # 参数
            params1 = {
                "page": f"{p}", # 页数
                "type": "intern",
                "keyword": "互联网，开发，算法", # 关键字，可以改
                "area": "",
                "months": "",
                "days": "",
                "degree": "",
                "official": "",
                "enterprise": "",
                "salary": "-0",
                "publishTime": "",
                "sortType": "zj",
                "city": "上海", # 地址，可以改
                "internExtend": ""
            }
            headers = {
                'authority': 'www.shixiseng.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': 'utm_source_first=PC; adCloseOpen=true; SXS_VISIT_XSESSION_ID_V3.0_EXP=2|1:0|10:1683702332|30:SXS_VISIT_XSESSION_ID_V3.0_EXP|16:MTY4Mzc4ODczMg==|7aa6b17473eea79cd87fbb61b3025ef8ecddbf736418dc214bd51943bccb96f3; SXS_VISIT_XSESSION_ID_V3.0=2|1:0|10:1683702332|26:SXS_VISIT_XSESSION_ID_V3.0|48:Y2M3ZGJjMWQtZmZjYS00NGY3LWI0ODctZDQwYTUyNThiNDQ5|73447b875827d43933e09e99ed5fb5e5db5f54689466d941a621736fb8f9ba2b; adClose=true; bottom_banner=true; utm_source=PC; utm_campaign=PC; Hm_lvt_03465902f492a43ee3eb3543d81eba55=1683701934,1683714237,1683716735; position=pc_search_flss; SXS_XSESSION_ID=2|1:0|10:1683716979|15:SXS_XSESSION_ID|88:MjU5YTY5MzFkMDI1YWRlY2RkZWE2M2JkMmM1ZmFjNDM2ZmY1ZTI0MjViZjQ0YzAwNDUzZmE5NjExOWNjZTBkYg==|44ef89f5107d90b1a0b4ef3fa91419ead1e07494135025d209803681df6580be; SXS_XSESSION_ID_EXP=2|1:0|10:1683716979|19:SXS_XSESSION_ID_EXP|16:MTY4NjMwODk3OQ==|4564243f2c96f0e439cf2719de58ee8f6ef4f4cc243319b0c5391cd85a4d1073; affefdgx=usr_k0z4zgwdmkyy; sxs_usr=2|1:0|10:1683716979|7:sxs_usr|24:dXNyX2swejR6Z3dkbWt5eQ==|445c63c2ee85025b9db2c70bc949c94acadb779689ed570753b4dba418cb6930; xyz_usr=2|1:0|10:1683716979|7:xyz_usr|40:bzhSbncwR2Q5VGM1NUtCMFZ2V1hiZWdCZVVnVQ==|307b731a2cc38179c9cc5f2ae0371c7db986a6f5769667d108ab6dc33d9e9991; userflag=user; RANGERS_WEB_ID=usr_k0z4zgwdmkyy; RANGERS_SAMPLE=0.12283785723221863; Hm_lpvt_03465902f492a43ee3eb3543d81eba55=1683716985',
                'if-none-match': '"906a7-a9aOHQkaK+brAigYcR8lK6FDzco"',
                'referer': 'https://www.shixiseng.com/',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.5'
            }
            # 发送请求，获取HTML页面
            response1 = requests.request("GET", url1, headers=headers,params=params1).text
            # print(response1)
            data1 = etree.HTML(response1)
            # xpath解析数据
            div = data1.xpath('//div[@style="display:;"]/div[1]/div')
            # 要放入数据库的数据
            y=[]
            conn = sqlite3.connect("./data.db")

            for i in div:
                # 获取详情页链接
                url2 = i.xpath('.//p/a[@class="title ellipsis font"]/@href')[0]
                # print(url2)
                # 获取详情页HTML
                while True:
                    try:#防止页面超时
                        response2 = requests.request("GET", url2, headers=headers,timeout=10).text
                        break
                    except:
                        print("=====================================超时！！=====================================")
                        continue
                # xpath解析数据
                data2 = etree.HTML(response2)
                gwmc = data2.xpath('//div[@class="new_job_name"]/span/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                gsmc = data2.xpath('//div[@class="com_intro"]/a[2]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                xz = data2.xpath('//span[@class="job_money cutom_font"]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                zwms = data2.xpath('//div[@class="job_detail"]//text()')
                zwms = pj(zwms).replace('  ','').replace('\t','').replace('\r','').replace('\n','').replace(',','，')
                tdyq = data2.xpath('//div[@class="content_left"]/div[@class="con-job"][2]//text()')
                tdyq = pj(tdyq).replace('  ','').replace('\t','').replace('\r','').replace('\n','').replace(',','，')
                gzdd = data2.xpath('//span[@class="com_position"]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                xl = data2.xpath('//span[@class="job_academic"]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                gzsc = data2.xpath('//span[@class="job_week cutom_font"]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                sxsc = data2.xpath('//div[@class="job_msg"]/span[@class="job_time cutom_font"][1]/text()')[0].replace(' ','').replace('\n','').replace(',','，')
                if sxsc.startswith('实习'):
                    sxsc = sxsc[2:]  # 删除开头的两个字符
                j=[url2,gwmc,gsmc,xz,gzdd,xl,gzsc,sxsc,zwms]
                y.append(j)
                # 打印数据，便于观察
                print(url2)
                print(gwmc)
                print(gsmc)
                print(xz)
                print(zwms)
                print(tdyq)
                print(gzdd)
                print(xl)
                print(gzsc)
                print(sxsc)
                print("================================================================================================")
            x = ['url','job_name', 'company_name', 'salary', 'address', 'xl','gzsc', 'sxsc','miaoshu']
            new_data = pd.DataFrame(y,columns=x)
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM job")
            count1 = cur.fetchone()[0]

            print(f"更新前表中数据量共{count1}")

            existing_data = pd.read_sql_query('select * from job', conn)
            # 合并数据并去重
            combined_data = pd.concat([existing_data, new_data]).reset_index(drop=True)
            combined_data = combined_data.drop_duplicates(subset='url')#只根据url去重

            # combined_data = pd.concat([existing_data, new_data]).reset_index(drop=True)
            # combined_data = combined_data.drop_duplicates()
            #只去处理缺省经纬值的行
            count2 = len(combined_data)
            print(count2)

            # for index, row in combined_data.iterrows():
            #     if pd.isnull(row['jw']):
            #         combined_data.loc[index, 'jw'] = location2jw(combined_data.loc[index, 'address'])

            if(count2>count1):
                last = combined_data.iloc[count1-count2:]
                for index, row in last.iterrows():
                    combined_data.at[index, 'jw'] = location2jw(combined_data.at[index, 'address'])

            combined_data.to_sql('job', conn, if_exists='replace', index=False )
            cur.execute("SELECT COUNT(*) FROM job")
            count = cur.fetchone()[0]
            print(f"更新后表中数据量共：{count}")



            # conn.execute('ALTER TABLE job ADD COLUMN id INTEGER NOT NULL AUTOINCREMENT')  # 添加自增字段id
            conn.close()
        return count

#将地址转换为经纬度
def location2jw(address):
    url = f"http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak=mWIQP1AiGugtUa9YUGB37bZBokfSGZgT"
    # 发送请求，获取响应
    response = requests.get(url)
    # print(response.text)
    # print(address)
    if "上海" not in address:
        return None
    if len(address)<=3:
        return None
    result = response.json()
    if result['status'] ==0:
        lng = result["result"]["location"]["lng"]
        lat = result["result"]["location"]["lat"]
        return str(lng) + ',' + str(lat)

    else:
        return None


if __name__ == '__main__':
    pass


import sqlite3
import csv
# conn = sqlite3.connect("data.db")  #打开或创建
# print ("opened database")
# cur = conn.cursor()
# sql = '''
#     create table job
#         (
#         url text,
#         job_name text not null,
#         company_name text not null,
#         salary text not null,
#         address text not null,
#         xl text not null,
#         gzsc text not null,
#         sxsc text not null,
#         miaoshu text not null,
#         jw text);
# '''
#
# # # 插入语句
# # sql = '''
# #     insert into boss (id,jname,cname,salary,address,miaoshu,others)
# #     values (1,'张三',"1","1","1","1","1")
# # '''
#
# # conn.execute('ALTER TABLE job DROP COLUMN id')
# #
# cur.execute(sql)
# conn.commit()
# conn.close()




#
def saveData2DB(datalist, dbpath):
    # conn = sqlite3.connect("data.db")  # 打开或创建
    # print("opened database")
    # cur = conn.cursor()
    # # sql = '''
    # #     create table boss
    # #         (id INTEGER PRIMARY KEY autoincrement,
    # #         jname text not null,
    # #         cname text not null,
    # #         salary text not null,
    # #         address text not null,
    # #         miaoshu text not null,
    # #         others text not null);
    # # '''
    # # cur.execute(sql)
    # conn.commit()
    # conn.close()
    # print("saving...")
    conn = sqlite3.connect(dbpath)
    cur=conn.cursor()
    i=0
    for data in datalist:
        # print(data)
        # print('\n')
        i +=1
        cur.execute("SELECT COUNT(*) FROM job")
        result = cur.fetchone()
        record_count = result[0]
        next_id = record_count + 1
        url = data[0]
        job_name = data[1]
        company_name = data[4]
        salary = data[5]
        address = data[6]
        miaoshu = data[7]
        xl = data[9]
        re = data[8].split(' ')
        print(re)
        gzsc = re[0]
        sxsc = re[1]

        sql='''
            insert into job(url,job_name,company_name,salary,address,xl,gzsc,sxsc,miaoshu)
            values (?,?,?,?,?,?,?,?,?)
        '''
        # print(sql)
        cur.execute(sql, (url, job_name, company_name,salary, address,xl,gzsc,sxsc, miaoshu))
        conn.commit()
    cur.close()
    conn.close()



def read_csv(file_path):
    datalist=[]
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i,row in enumerate(reader):
            if i==0:
                continue
            datalist.append(row)
    return datalist


if __name__ == "__main__" :
    dbpath = "data.db"
    file_path = "boss.csv"
    datalist = read_csv(file_path)
    saveData2DB(datalist, dbpath)



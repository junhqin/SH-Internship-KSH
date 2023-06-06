html+ python +django +爬虫 +pyecharts+celery
##实现了上海实习数据实时可视化，项目已经部署到了网站###
可通过域名：data.junhqin.com 访问来进行浏览 
管理员账户：admin
密码：ksh2023
（用于更新数据权限）

下面是运行环境的步骤：（请一步步运行）
请使用python3.6版本（务必，不然有版本冲突）

安装requirements.txt依赖：pip install -r requirements.txt

生成迁移文件 python manage.py makemigrations

执行迁移 python manage.py migrate

启动项目
python manage.py runserver
执行分布式任务队列
python manage.py celery worker --loglevel=info 启动worker
python manage.py celery beat --loglevel=info 启动定时任务
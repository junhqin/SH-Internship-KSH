import redis

# 创建Redis客户端实例
r = redis.Redis(host='127.0.0.1', port=6379, db=2)

# 执行Redis命令
r.set('key', 'value')
result = r.get('key')
print(result)

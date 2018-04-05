# coding: utf8
import time
from DelayQueue import*

redis_conf = {'host': '127.0.0.1', 'port': 6379, 'db': 0}
# 构造延迟队列对象
queue = DelayQueue(redis_conf)
# push 20条数据
for i in range(20):
    item = {'user': 'user-{}'.format(i)}
    queue.push(item)
    
# 从延迟队列中马上获取10条数据
data = queue.pop(num=10)
# 刚添加的马上获取是获取不到的
assert len(data) == 0
# 休眠10秒
time.sleep(10)
# 从延迟队列中获取10条数据
data = queue.pop(num=10)
assert len(data) == 10
# 从延迟队列中获取截止到5秒之前添加的10条数据
data = queue.pop(num=10, previous=5)
assert len(data) == 10

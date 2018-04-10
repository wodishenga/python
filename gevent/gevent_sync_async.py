#coding=utf-8
import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task', pid, 'done')

def synchronous():  #同步
    for i in range(1,10):
        task(i)

def asynchronous(): #异步
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
# Synchronous: #没有协程则不会控制其它进程睡眠,所以挨个执行
# (‘Task’, 1, ‘done’)
# (‘Task’, 2, ‘done’)
# (‘Task’, 3, ‘done’)
# (‘Task’, 4, ‘done’)
# (‘Task’, 5, ‘done’)
# (‘Task’, 6, ‘done’)
# (‘Task’, 7, ‘done’)
# (‘Task’, 8, ‘done’)
# (‘Task’, 9, ‘done’)
# Asynchronous: #他们放在grennlet里面,sleep的时间是随机的,完成顺序也就不同了
# (‘Task’, 2, ‘done’)
# (‘Task’, 3, ‘done’)
# (‘Task’, 5, ‘done’)
# (‘Task’, 7, ‘done’)
# (‘Task’, 9, ‘done’)
# (‘Task’, 6, ‘done’)
# (‘Task’, 1, ‘done’)
# (‘Task’, 0, ‘done’)
# (‘Task’, 8, ‘done’)
# (‘Task’, 4, ‘done’)

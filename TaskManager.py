import queue

# 需要的改进：增加多线程支持
# 初始化一个队列：放入速度 > 取出速度 可以缓冲
# 放入速度 < 取出速度 执行取出行为线程阻塞

# 为生产者-消费者模型而设计的队列
# 可选参数1为block=True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。即消费者线程阻塞
# 如果队列为空且block为False，队列将引发Empty异常。
# 可选参数2为timeout=None，如果timeout为非负数，那么线程阻塞最长时间为该值，超时后产生empty exception
class TaskManager():
    def __init__(self):
        self.taskQueue = queue.Queue()

    def add(self, item):
        self.taskQueue.put(item)

    # 取不出元素返回None
    def get(self):
        if self.taskQueue.qsize() != 0:
            return self.taskQueue.get(block = False)
        else:
            return None

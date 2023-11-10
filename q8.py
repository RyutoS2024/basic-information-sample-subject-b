import queue

class PrioQueue:
    def __init__(self):
        self.queue = queue.PriorityQueue()
        
    # 優先度を指定して要素を追加する
    def enqueue(self, item: str, priority: int):
        self.queue.put((priority, item))
        
    # 優先度付きキューからキュー内で最も優先度の高い要素を取り出して返す
    # 最も優先度の高い要素が複数あるときは，そのうち最初に追加された要素を1つ取り出して返す
    def dequeue(self):
        if self != None:
            return self.queue.get()[1]
    
    # 優先度付きキューに格納されている要素の個数を返す
    def size(self):
        return self.queue.qsize()

# インスタンスを作成する
prioQueue = PrioQueue()

prioQueue.enqueue("A", 1)
prioQueue.enqueue("B", 2)
prioQueue.enqueue("C", 2)
prioQueue.enqueue("D", 3)
prioQueue.dequeue() # A（1）
prioQueue.dequeue() # B（2）
prioQueue.enqueue("D", 3)
prioQueue.enqueue("B", 2)
prioQueue.dequeue() # B（2）
prioQueue.dequeue() # C（2）
prioQueue.enqueue("C", 2)
prioQueue.enqueue("A", 1)

while (prioQueue.size() != 0):
    print(prioQueue.dequeue()) 
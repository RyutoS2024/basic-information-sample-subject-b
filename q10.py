# 単方向リストの1つの要素を表すクラス 
class ListElement:
    
    def __init__(self, qVal: str):
        self.val = qVal # val=データ
        self.next = None # next=次の要素への参照

# 単方向リスト全体を表すクラス
class SinglyLinkedList:
    def __init__(self):
        self.listHead = None # リストの先頭
        
        # 引数で与えられた文字を単方向リストに追加する
    # 新しい要素はリストの末尾に追加される
    def append(self, qVal: str):
        
        curr = ListElement(qVal) # 要素を1つ作成する
        
        if (self.listHead == None): # もしリストの先頭が何も参照していない場合
            self.listHead = curr # さきほど作成した要素をリストの1つ目とする
        else: # すでに先頭がある要素を参照していた場合，追加する要素の1つ前の参照を付け替える
            prev = self.listHead # リストの先頭を取得する
            while (prev.next != None): # 要素が別の要素を参照していたとき以下の処理を繰り返す
                prev = prev.next # 次の要素を取得する
                
            prev.next = curr # 要素が何も参照していなければ新しい要素を追加する
    
    
    def delNode(self, pos: int):
        
        if (pos == 0):
            self.listHead = self.listHead.next
        else:
            prev = self.listHead
            
            for i in range (1, pos-1):
                if (i == 1):
                    continue
                prev = prev.next
            
            prev.next = prev.next.next
    
    # 単方向リストの中身を表示する
    def display(self):
        current = self.listHead
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
            
# 単方向リストのインスタンスを作成する
my_list = SinglyLinkedList()

# 単方向リストに要素を追加する
my_list.append(1)
my_list.append(2)
my_list.append(3) 
my_list.delNode(0)

# リストの中身を表示する
my_list.display()
# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : 大小根堆.py
# @Time       ：2024/3/6 14:34
# @version    ：python 3.9
# @Software   : PyCharm
# @Description：
"""
# ================【功能：】====================
import heapq

# 小根堆
a = []  # 创建一个空堆
heapq.heappush(a, 18)
heapq.heappush(a, 1)
heapq.heappush(a, 20)
heapq.heappush(a, 10)
heapq.heappush(a, 5)
heapq.heappush(a, 200)
print(a)
heapq.heappop(a)
print(a)
print('------------')
#
a = []
for i in [1, 5, 20, 18, 10, 200]:
    heapq.heappush(a, -i)
print(list(map(lambda x: -x, a)))

print('-----')
# heapify(heap) 建立大、小根堆
# heapq.heapfy()是以线性时间将一个列表转化为小根堆
a = [1, 5, 20, 18, 20, 200]
heapq.heapify(a)
print(a)

# 用同样相同的方法建立大根堆
a = [1, 5, 20, 18, 10, 200]
a = list(map(lambda x: -x, a))
heapq.heapify(a)
print([-x for x in a])
# 与第一节所得大根堆相比， 虽然二叉树的第三层元素顺序不同， 但都符合大根堆的定义

# heappop(heap)
# heapq.heappop()是从堆中弹出并返回最小的值
# 利用heappop进行堆排序
# 堆排序当然也要利用到heappush或者heapify， 可参考排序算法总结中的堆排序， 这里只贴代码
print('---------')
import heapq


def heap_sort(arr):
    if not arr:
        return []
    h = []  # 建立空堆
    for i in arr:
        heapq.heappush(h, i)  # heappush自动建立小根堆
    return [heapq.heappop(h) for i in range(len(h))]  # heappop每次删除并返回列表中最小的值


# 若是从大到小排列， 有两种方法
# 1）先建立小根堆， 然后每次heappop(), 此时得到从小到大的排列， 再reverse
# 2) 利用相反数建立大根堆， 然后heappop(-元素), 即push(-元素), pop(-元素)
print('-----')
a = [10, 2, 1, 29, 30, 16, 90, 3]
res = heap_sort(a)
print(res)

# 3.2 普通list的heapop()
# 普通list(即并没有进行heapify等操作的list)， 对它进行heappop操作并不会弹出list中最小的值， 而是弹出第一个值
print('------3.2 普通list的heappop()-----')
a = [3, 6, 1]
heapq.heapify(a)  # a变成堆之后， 可以对其操作
print(heapq.heappop(a))

b = [4, 2, 5]  # b不是堆， 如果对其进行操作， 显示结果如下
print(heapq.heappop(b))  # 按照排序， 删除第一个数值并返回， 不会从中挑选出最小的

heapq.heapify(b)  # 变成堆之后， 再操作
print(heapq.heappop(b))

# 5 heapreplace(heap.item)弹出并返回heap中最小的一项， 同时推入新的item
# heapq.heapreplace()与heapq.heappushpop()相反， 先进行heappop()， 再进行heappush()
# 堆的大小不变。如果堆为空则引发IndexError。这个单步骤操作比依次执行heappop() + heappush()更高效，
# 并且在使用固定大小的堆时更为适宜。pop/push组合总是会从堆中返回一个元素并将其替换为item。
# 返回的值可能会比添加的item更大， 如果不希望如此， 可以考虑改用heappushpop()。
# 它的push/pop组合会返回两个值中较小的一个， 将较大的值留在堆中。
print('----5-----')
a = []
# heapq.heapreplace(a, 3)  # 如果list为空， 则报错
heapq.heappush(a, 3)
print(a)  # [3]
print(heapq.heapreplace(a, 6))  # 先从堆a中找出最小值并返回， 然后加入6  3
print(a)  # [6]

heapq.heappush(a, 5)
heapq.heappush(a, 9)
heapq.heappush(a, 4)
print(a)  # [4, 5, 9, 6]
heapq.heapreplace(a, 1)  # 1是后来加入的， 在1加入之前， a中最小值是4
print(a)  # [1, 5, 9, 6]

# 6 merge(*iterables)
# heapq.merge()合并多个堆然后输出
# 输入的list无序，
## 6 merge(*iterables)
# heapq.merge()合并多个堆然后输出， 输入的list无序， merge后无序。若输入的list有序， merge后也有序
print('-------6、merge-----')
# 无序
print(list(heapq.merge([1578, 2, 5, 3], [1564, 554, 25458], [])))

print(list(heapq.merge([1, 3, 5, 7], [0, 2, 4, 8], [5, 10, 15, 20], [], [25])))  # 有序

# heapq.merge()迭代性质意味着它对所有提供的序列都不会做一次性读取，
# 这意味着可以利用它处理非常长的序列， 而开销却非常小。

# 7 nlargest(n, iterbale, key=None)和nsmallest(n, iterbale, key=None)
# 获取列表中最大、最小的几个值， key的作用和sorted()方法里面的key类似
print('-----7、nlarge----')
a = [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 20, 25]
print(heapq.nlargest(5, a))  # [25, 20, 10, 8, 7]

b = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(heapq.nlargest(1, b, key=lambda x: x[1]))  # [('e', 5)]

# 复杂度分析
# 各个方法的复杂度
'''
1) heapq.heapify(x): O(n)
2) heapq.heappush(heap, item) : O(logn)
3) heapq.heappop(heap): O(logn)
插入或删除元素时， 所有节点自动调整， 保证堆的结构的复杂度为O(log n)
4) heapq.nlargest(k, iterable)和nsmallest(k, iterable): O(n * log(t))

# 关于排序和取TopN时各方法的快慢比较
在关于排序和取TopN值时， 到底使用什么方法最快， 
1） 当要查找的元素个数相对比较小的时候， 函数nlargest()和nsmallest()
2) 仅仅想查找唯一的最小或最大(N=1)元素的话， 那么使用min()和max()函数
3） 如果N的大小和集合大小接近的时候， 通常先排序这个集合然后再使用切片操作会更快点(sorted(items)[:N])
'''

print('-----9、heapq实现优先队列----')
# 9、使用heapq实现优先队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # push方法， 实现将列表转化为堆数据。
        # 插入的是元祖， 元组大小比较式从第一个元素开始， 第一个相同， 再对比第二个元素。
        # 我们这里采用的方案是如果优先级相同， 那么就根据第二个元素， 谁先插入堆中， 谁的index就小， 那么它的值就小

        # heapq.heappop()方法得到， 该方法会先将第一个元素弹出，然后用下一个最小的元素来去代被弹出元素
        # heappush在队列_queue上插入第一个元素
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop在队列_queue上删除第一个元素
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
# 输出
'''
Item('bar')
Item('spam')
Item('foo')
'''




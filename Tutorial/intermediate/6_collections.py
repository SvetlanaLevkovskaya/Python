# collections: Counter, namedtuple, OrderDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = 'aaabbbbccc'
print('a', '                                           ', a)
my_counter = Counter(a)
print('my_counter = Counter(a)', '                     ', my_counter)
print('my_counter.items()', '                          ', my_counter.items())
print('Counter(a).items())', '                         ', Counter(a).items())
print('my_counter.keys', '                             ', my_counter.keys())
print('my_counter.values()', '                         ', my_counter.values())
print('my_counter.most_common(1)', '                   ', my_counter.most_common(1))
print('my_counter.most_common(2)', '                   ', my_counter.most_common(2))
print('my_counter.most_common(1)[0][0]', '             ', my_counter.most_common(1)[0][0])
print('list(my_counter.elements())', '                 ', list(my_counter.elements()))
print('type(my_counter)', '                            ', type(my_counter))

print('*'*80)
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print('pt', '                                          ', pt)
print('pt.x, pt.y', '                                  ', pt.x, pt.y)
print('type(pt)', '                                    ', type(pt))

print('*'*80)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['e'] = 4
print('ordered_dict', '                               ', ordered_dict)
print('type(ordered_dict)', '                         ', type(ordered_dict))

print('*'*80)
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print('d', '                                          ', d)
print('d["a"]', '                                     ', d['a'])
print('d["b"]', '                                     ', d['b'])
print('d["c"]', '                                     ', d['c'])
print('type(d)', '                                    ', type(d))


print('*'*80)
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print('d', '                                          ', d)
print('d["a"]', '                                     ', d['a'])
print('d["b"]', '                                     ', d['b'])
print('d["c"]', '                                     ', d['c'])
print('type(d)', '                                    ', type(d))

print('*'*80)
d = defaultdict(list)

d['a'] = 1
d['b'] = 2
print('d', '                                          ', d)
print('d["a"]', '                                     ', d['a'])
print('d["b"]', '                                     ', d['b'])
print('d["c"]', '                                     ', d['c'])
print('type(d)', '                                    ', type(d))


print('*'*80)
d = deque()
d.append(1)
d.append(2)
print('d = deque()', '                                ', d)
d.appendleft(3)
print('d.appendleft(3)', '                            ', d)
d.pop()
print('d.pop()', '                                    ', d)
d.popleft()
print('d.popleft()', '                                ', d)
d.extend([4, 5, 6])
print('d.extend(4, 5, 6])', '                         ', d)
d.extendleft([4, 5, 6])
print('d.extendleft(4, 5, 6])', '                     ', d)
d.rotate(1)
print('d.rotate(1)', '                                ', d)
d.rotate(-1)
print('d.rotate(-1)', '                               ', d)
d.clear()
print('d.clear()', '                                  ', d)
print('type(d)', '                                    ', type(d))

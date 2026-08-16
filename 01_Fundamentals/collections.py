from collections import Counter
a = "aaaabbbbccc"
#operations
# count = Counter(a)
# count = Counter(a).items()
# count = Counter(a).most_common(1)[0][0]
# count = list(Counter(a).elements())
# print(count)


# from collections import namedtuple
# point = namedtuple('points', 'x,y')
# pt = point(1, -4)
# print(pt)

from collections import OrderedDict
from collections import defaultdict

# ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['a'] = 1
# print(ordered_dict)

# d = defaultdict(int) 
# d['b'] = 2
# d['c'] = 3
# d['a'] = 4
# print(d['z'])


# from collections import deque

# d = deque()

# d.append(1)
# d.append(2)

# d.appendleft(4)
# print(d)

# d.popleft()
# print(d)

# d.extend([4, 5, 6])
# print(d)

# from itertools import product
# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2)
# print(list(prod))

# from itertools import permutations
# a = [4, 5, 6]
# perm = permutations(a, 2)
# print(list(perm)) 

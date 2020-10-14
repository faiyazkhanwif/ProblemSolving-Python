#Code for finding all possible subsets of a particular length
from itertools import combinations
a_set = ["a", "b", 1, 2]

data = combinations(a_set,2)

subsets = set(data)

print(subsets)

#Convert subset to list
my_set = {'Geeks', 'for', 'geeks'}

s = list(my_set)
print(s)


#Code for finding all possible subsets
from itertools import chain, combinations

def powerset(a_set):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(a_set)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerset(a_set)))
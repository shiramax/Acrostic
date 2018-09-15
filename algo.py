from itertools import combinations, chain
import operator

priority = {12: 8503, 11: 12967, 10: 17986, 9: 22132, 8: 23830, 7: 23661, 6: 21592, 5: 17301, 4: 13542, 3: 3962, 2: 287, 1: 42}
sotred_priority = sorted(priority.items(), key=operator.itemgetter(1))
input  = ["e", "a", "c", "h", "v", "m", "f", "s", "d", "r"]



def sum_to_n(n):
    'Generate the series of +ve integer lists which sum to a +ve integer, n.'
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i))
    return (list(map(operator.sub, chain(s, e), chain(b, s))) for s in splits)


def find_combo_by_priority():
    combo_by_priority = {}
    sum=0
    for p in sum_to_n(len(input)-1):
        for i in p:
            import ipdb; ipdb.set_trace()
            sum +=priority[i]
        combo_by_priority[p]=sum
        sum=0
    return combo_by_priority

find_combo_by_priority()
# count = 0
# for combs in (combinations(input, r) for r in range(len(input)+1)):
#     for comb in combs:
#         diff = list(set(input[:]) - set(comb))
#         print diff, list(comb)
#         count += 1
#
# print "count: ", count

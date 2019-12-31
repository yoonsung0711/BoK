from algo_2019_winter._03_.cache_simple_impl2 import SimpleCache

cacheSize = [3, 3, 2, 5, 2, 0]
citiesArrs = [ ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
            ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
            ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
            ["Jeju", " Pangyo", " Seoul", " NewYork", " LA", " SanFrancisco", " Seoul", " Rome", " Paris", " Jeju", " NewYork", " Rome"],
            ["Jeju", " Pangyo", " NewYork", " newyork"],
            ["Jeju", " Pangyo", " Seoul", " NewYork", " LA"] ]
execTime = [50, 21, 60, 52, 16, 25]

def gen(arr):
    cur = 0
    while cur < len(arr) - 1:
        cur = cur + 1
        yield a[cur]

c = cacheSize[1]
a = citiesArrs[1]
t = 0 
__cache = []


# check cache hit
# success:

# def refer(s):
#     print("new: {}".format(s))
#     global __cache
#     global t
#     if s in __cache:
#         print("cache hit: +1 -> {}".format(t))
#         t = t + 1
#         idx = __cache.index(s); __cache[idx]
#         s = [s] + __cache[0:idx] + __cache[idx + 1:]
#     # fail:
#     if s not in __cache:
#         t = t + 5
#         # full
#         if not len(__cache) < c:
#             print("cache miss +5 -> {}".format(t))
#             print("cache is full : {}".format(__cache))
#             __cache = __cache[1:]
#             print("removed the oldest : {}".format(__cache))
#             __cache.append(s)
#             print("new one appended : {}".format(__cache))
#         # not full
#         if len(__cache) < c:
#             print("cache miss +5 -> {}".format(t))
#             print("cache is not full: {}".format(__cache))
#             __cache.append(s)
#             print("new one appended : {}".format(__cache))

g = gen(a)

try:
    s = next(g)
    "new: {}".format(s)
except StopIteration:
    "finish"


if s in __cache:
    "cache hit: +1 -> {}".format(t)
    t = t + 1
    idx = __cache.index(s); __cache[idx]
    __cache = (__cache[0:idx] + __cache[idx + 1:]) if idx == 0 else __cache
if s not in __cache:
    t = t + 5
    # full
    if not len(__cache) < c:
        "cache miss +5 -> {}".format(t)
        "cache is full : {}".format(__cache)
        __cache = __cache[1:]
        "removed the oldest : {}".format(__cache)
        __cache.append(s)
        "new one appended : {}".format(__cache)
    # not full
    if len(__cache) < c:
        "cache miss +5 -> {}".format(t)
        "cache is not full: {}".format(__cache)
        __cache.append(s)
        "new one appended : {}".format(__cache)


g = gen(a);t=0;__cache=[]

# g = gen(a)
# while True:
#     try:
#         s = next(g)
#         refer(s)
#     except StopIteration:
#         break
# t = 0 
# __cache = []

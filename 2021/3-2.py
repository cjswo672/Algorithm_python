import re
import random
import time

class Lang:
    def __init__(self):
        self.lang = {'java': Field(), 'python': Field(), 'cpp': Field(), '-': Field()}
    def get(self):
        return self.lang

class Field:
    def __init__(self):
        self.field = {'backend': Career(), 'frontend': Career(), '-': Career()}
    def get(self):
        return self.field

class Career:
    def __init__(self):
        self.career = {'junior': Soul(), 'senior': Soul(), '-': Soul()}
    def get(self):
        return self.career

class Soul:
    def __init__(self):
        self.soul = {'pizza': [], 'chicken': [], '-': []}
    def get(self):
        return self.soul

def insert(root, depth, key):
    if depth == 4:
        root.append(int(key[depth]))
        return
    insert(root.get()[key[depth]], depth + 1, key)
    insert(root.get()['-'], depth + 1, key)

def sort(root, depth):
    if depth == 4:
        root.sort()
        return
    d = root.get()
    for k in d: sort(d[k], depth + 1)

def find_idx(arr, value):
    l, r, res = 0, len(arr) - 1, len(arr)
    while l <= r:
        m = (l + r) // 2
        if arr[m] >= value: 
            r = m - 1
            res = min(res, m)
        else: l = m + 1
    return res

def solution(info, query):
    answer = []
    root = Lang()
    for idx, i in enumerate(info):
        insert(root, 0, i.split(" "))
    sort(root, 0)
    
    for idx, q in enumerate(query):
        q = q.split(" and ")
        soul_q, score_q = q[3].split(" ")

        field = root.get()[q[0]]
        career = field.get()[q[1]]
        soul = career.get()[q[2]]
        score = soul.get()[soul_q]
        answer.append(len(score) - find_idx(score, int(score_q)))
    return answer

lang = ['java', 'python', 'cpp', '-']
field = ['backend', 'frontend', '-']
carrer = ['junior', 'senior', '-']
food = ['pizza', 'chicken', '-']

applicants = []
queries = []

for i in range(50000):
    s = f'{lang[random.randint(0, 2)]} {field[random.randint(0, 1)]} {carrer[random.randint(0, 1)]} {food[random.randint(0, 1)]} {random.randint(0, 100000)}'
    applicants.append(s)

for i in range(100000):
    s = f'{lang[random.randint(0, 3)]} and {field[random.randint(0, 2)]} and {carrer[random.randint(0, 2)]} and {food[random.randint(0, 2)]} {random.randint(0, 100000)}'
    queries.append(s)

tic = time.time()
solution(applicants, queries)
print("\n", time.time() - tic)
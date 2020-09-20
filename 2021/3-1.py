from collections import defaultdict
import re

class Applicant:
    def __init__(self, info):
        self.lang = info[0]
        self.field = info[1]
        self.carrier = info[2]
        self.soul = info[3]
        self.score = int(info[4])

def solution(info, query):
    answer = []
    applicants, scores = [], []
    lang, field, carrier, soul, score = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    # 지원자의 info를 분리한다.
    for i in info:
        a = Applicant(i.split(" "))
        applicants.append(a)
        lang[a.lang].append(a)
        field[a.field].append(a)
        carrier[a.carrier].append(a)
        soul[a.soul].append(a)
        scores.append(a.score)

    scores.sort()
    # query를 분리한다.
    for q in query:
        q = q.split(" and ")
        f, sc = q[3].split(" ")
        s = set(applicants)
        if q[0] is not '-': s &= set(lang[q[0]])
        if q[1] is not '-': s &= set(field[q[1]])
        if q[2] is not '-': s &= set(carrier[q[2]])
        if f is not '-': s &= set(soul[f])
        s &= set([a for a in applicants if a.score >= int(sc)])
        answer.append(len(s))
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

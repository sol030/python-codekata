# [PCCE 기출문제] 6번 / 물 부족
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340202
# 작성자: 조은솔
# 작성일: 2026. 01. 26. 20:02:20

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage + (usage * change[i]/100)
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1
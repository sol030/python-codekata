# 카운트 업
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181920
# 알고리즘: 반복문
# 작성자: 조은솔
# 작성일: 2026. 01. 22. 11:26:12

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer
# 콜라츠 추측
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 알고리즘: 시뮬레이션, 반복문
# 작성자: 조은솔
# 작성일: 2026. 01. 16. 14:43:29

def solution(num):
    answer = 0
    if num == 1:
        return 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        answer += 1
        if answer >= 500:
            return -1
    return answer
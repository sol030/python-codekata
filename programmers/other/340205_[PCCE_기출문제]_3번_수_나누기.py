# [PCCE 기출문제] 3번 / 수 나누기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340205
# 작성자: 조은솔
# 작성일: 2026. 01. 29. 09:28:41

number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(answer)
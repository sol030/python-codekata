# [PCCE 기출문제] 2번 / 각도 합치기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340206
# 작성자: 조은솔
# 작성일: 2026. 02. 03. 14:14:05

angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2) % 360
print(sum_angle)
# 이상한 문자 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 알고리즘: 문자열
# 작성자: 조은솔
# 작성일: 2026. 01. 20. 18:05:11

def solution(s):
    answer = s.split(" ")
    result = []

    for word in answer:
        words = ""
        for i, ch in enumerate(word):
            if i % 2 == 0:
                words += ch.upper()
            else:
                words += ch.lower()
        result.append(words)

    return " ".join(result)
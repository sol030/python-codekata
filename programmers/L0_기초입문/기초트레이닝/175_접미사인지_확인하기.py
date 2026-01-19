# 접미사인지 확인하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 알고리즘: 문자열
# 작성자: 조은솔
# 작성일: 2026. 01. 19. 14:50:44

def solution(my_string, is_suffix):
    n = len(is_suffix) 
    answer = my_string[-n:]
    return 1 if answer == is_suffix else 0 
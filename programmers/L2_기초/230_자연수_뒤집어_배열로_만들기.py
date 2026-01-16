# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 조은솔
# 작성일: 2026. 01. 16. 14:43:35

##내가 쓴 거 (ORDER BY 어쩌구 DESC같은)
def solution(n):
    result = []
    while n > 0:	#더이상 안 쪼개질 때까지 반복
        result.append(n % 10)   # 10으로 나눈 나머지(맨 뒷자리)를 리스트에 추가
        n //= 10                # n을 10으로 나눈 몫으로 갱신하여 맨 뒷자리를 제거
        			#전체 숫자가 오른쪽으로 한 칸 이동하며 마지막 숫자가 칸 밖으로 밀려 나감
    return result               # 이미 뒤집힌 상태라서 그냥 반환
# 오랜 기간 보호한 동물(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59411
# 작성자: 조은솔
# 작성일: 2026. 01. 20. 18:27:06

-- 코드를 입력하세요
SELECT
    i.animal_id,
    i.name
FROM animal_ins i
INNER JOIN animal_outs o
    ON i.animal_id = o.animal_id
ORDER BY o.datetime - i.datetime DESC
LIMIT 2;
select e.ID, 
    (   
        select count(*)
        from ecoli_data c
        where c.parent_id = e.id
    ) as CHILD_COUNT
from ecoli_data e
order by e.id 

-- 바깥쪽 값을 참조하기 때문에 ,바깥쪽 행 수만큼 반복 실행됨!
"""
새롭게 깨닳은것 : 
1. 상관 서브쿼리 : 서브쿼리가 바깥 쿼리의 칼럼을 참조!
2. self join관계 : 같은 테이블 안에서 계층구도를 표현하는 방식 - 트리
3. 상관 서브쿼리는 행 수만큼 반복 실행, 느림 -> Left join 은 한번의 집계로 더 빠름
4. colesce 활용 : 매칭 안되는 행은 null이 됨 (left join 할 떄), 이때 coalesce로 null을 0으로 바꾸기
""" 
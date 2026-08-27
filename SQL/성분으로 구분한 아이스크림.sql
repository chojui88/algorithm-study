select b.INGREDIENT_TYPE	, sum(TOTAL_ORDER) as TOTAL_ORDER
from first_half a 
join icecream_info b
on a.flavor = b.flavor
group by INGREDIENT_TYPE
order by TOTAL_ORDER 

-- group by는 1단계 : 값이 같은 행들을 그룹화한뒤, 2단계: 그 그룹 안에서 합계를 계산한다
-- 그래서 group by와 sum이 같이 쓰이면, 그룹 안에서 sum이 되는거라고 문법이 달라짐!


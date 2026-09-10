select base.ID, base.FISH_NAME, base.LENGTH
from fish_info base
join fish_name_info name
on base.fish_type = name.fish_type
where (base.FISH_TYPE, base.LENGTH) IN (
    select base.fish_type, max(LENGTH)
    from fish_info as base
    group by base.fish_type
)
order by base.ID

-- 집계 연산과, 행의통계값 구하기를 동시에 할 수 없다!!
--sql는 group by를 수행하고 나면, 통계를 낼 수 없다, 그래서 max를 먼저 계산해줘야함!
-- select 절의 서브쿼리는 하나의 값만 반환해야 한다!!!!
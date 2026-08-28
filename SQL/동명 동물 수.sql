select NAME, count(*) as count
from animal_ins
group by name
having count(*) >= 2
order by name

-- where절에는  개별 행을 필터링 하는 단계여서, 그룹된 count 쓸 수 없다
-- 
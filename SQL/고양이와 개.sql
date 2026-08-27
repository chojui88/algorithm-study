select animal_type, count(*) as count
from animal_ins
where animal_type regexp 'Cat|Dog'
group by animal_type
order by animal_type

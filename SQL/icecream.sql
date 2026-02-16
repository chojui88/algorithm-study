SELECT f.flavor #상위 3개
from FIRST_HALF f
INNER JOIN JULY j on f.flavor = j.flavor
GROUP BY f.flavor
ORDER BY SUM(f.total_order) + SUM(j.total_order) DESC
LIMIT 3;

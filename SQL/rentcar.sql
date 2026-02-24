SELECT c.CAR_ID,	c.CAR_TYPE, ROUND(c.daily_fee  *30* (100-REPLACE(p.discount_rate,'%',''))/ 100) as FEE
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
ON c.CAR_TYPE = p.CAR_TYPE
WHERE  p.duration_type IN ('30일 이상')
and c.daily_fee * 30 between 200000 and 500000 
and c.CAR_TYPE IN('세단','SUV')
and not exists (SELECT 1
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    WHERE h.CAR_ID = c.CAR_ID
    AND h.START_DATE <= '2022-11-30'
      AND h.END_DATE >= '2022-11-01') 
ORDER BY FEE desc, c.CAR_TYPE asc, c.CAR_ID desc
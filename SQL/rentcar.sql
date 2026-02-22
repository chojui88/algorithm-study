SELECT CAR_ID,	CAR_TYPE,	FEE
FROM CAR_RENTAL_COMPANY_CAR c
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h
ON c.CAR_ID = h.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
ON c.CAR_TYPE = p.CAR_TYPE
WHERE  h.duration_type IN ('30일 이상')
and c.daily_fee * 30 between 200000 and 500000 
and c.CAR_TYPE IN('세단','SUV')
not exist (h.start_date <= '2022-11-1'
and h.end_date >= '2022-11-30') 
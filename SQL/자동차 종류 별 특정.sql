select CAR_TYPE, count(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS regexp '통풍시트|열선시트|가죽시트'
GROUP BY CAR_TYPE
order by CAR_TYPE

-- option은 하나하나의 값이 아니라, ,로 결합되어있어서 1차정규화가 되어있지 않음
select FLOOR(price/10000)*10000 as PRICE_GROUP , count(*) as PRODUCTS
from product
group by PRICE_GROUP--만원 단위로 카운트하고싶어
order by PRICE_GROUP

--새로배운것: 구간 나누기 Floor(값/단위) * 단위
SELECT ROUND(AVG(daily_fee),0) as AVERAGE_FEE
FROM car_rental_company_car
where car_type = 'SUV'

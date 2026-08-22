select a.category, sum(b.sales) as TOTAL_SALES
from book a
jOIN book_sales b ON a.book_id = b.book_id
where sales_date like '2022-01%'
group by a.category
order by a.category asc;
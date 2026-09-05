select u.USER_ID, u.NICKNAME, sum(price) as TOTAL_SALES
from used_goods_board b
join used_goods_user u 
on b.writer_id = u.user_id
where b.status = 'DONE'
group by b.writer_id -- 오라클은, select의 모든 칼럼도 적어줘야 함 
having sum(price) >= 700000
order by TOTAL_SALES


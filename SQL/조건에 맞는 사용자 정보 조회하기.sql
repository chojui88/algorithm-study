select u.USER_ID, u.NICKNAME, 
CONCAT(
    u.city, ' ',
    u.street_address1, ' ',
    u.street_address2
 ) as '전체주소', 
regexp_replace(
    u.TLNO, '([0-9]{3})([0-9]{4})([0-9]{4})$', '$1-$2-$3')
    as '전화번호'
from used_goods_board b 
join used_goods_user u
on b.writer_id = u.user_id
group by u.USER_ID, u.NICKNAME, u.CITY, u.STREET_ADDRESS1, u.STREET_ADDRESS2, u.TLNO
having count(board_id) >=3
order by u.USER_ID desc



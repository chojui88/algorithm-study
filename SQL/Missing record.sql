SELECT o.animal_id, o.name
FROM animal_ins i -- 동물의 정보
RIGHT JOIN animal_outs o -- 입양보낸 동물의 정보
ON i.animal_id = o.animal_id
WHERE i.animal_id is NULL
ORDER BY o.animal_id

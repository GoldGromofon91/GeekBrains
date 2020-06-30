/* 1. Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался 
 * с выбранным пользователем.
 * users.id = 1
 * */ 


SELECT from_user_id, count(*) as total
FROM messages
WHERE to_user_id = 1
GROUP BY from_user_id
ORDER BY total DESC;

+--------------+-------+
| from_user_id | total |
+--------------+-------+
|            8 |     9 |
|            4 |     3 |
|            2 |     2 |
|            3 |     1 |
|           13 |     1 |
|           18 |     1 |
|           19 |     1 |
+--------------+-------+


/*
 * Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..
 * */

-- пользователи кто младше 10 лет
select *
from likes
where user_id in (SELECT user_id from profiles where TIMESTAMPDIFF(YEAR,birthday,NOW()) <= 10)

+----+---------+----------+---------------------+
| id | user_id | media_id | created_at          |
+----+---------+----------+---------------------+
|  2 |       2 |        1 | 1988-09-04 16:08:30 |
|  7 |       7 |        2 | 2003-02-03 04:56:27 |
+----+---------+----------+---------------------+


select count(*) as total_likis
from likes
where user_id in (SELECT user_id from profiles where TIMESTAMPDIFF(YEAR,birthday,NOW()) <= 10)

+-------------+
| total_likis |
+-------------+
|           2 |
+-------------+

/*
 * Определить кто больше поставил лайков (всего): мужчины или женщины.
 * */

select
 (select count(id) from likes) as total_like,
 (select count(id) from likes where user_id in (SELECT user_id from profiles where gender ='f')) as female_like,
 (select count(id) from likes where user_id in (SELECT user_id from profiles where gender ='m')) as male_like










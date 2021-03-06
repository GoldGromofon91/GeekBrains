-- “Операторы, фильтрация, сортировка и ограничение”

/* 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем. */
SELECT * FROM users;
+----+--------------------+-------------+---------------------+---------------------+
| id | name               | birthday_at | created_at          | updated_at          |
+----+--------------------+-------------+---------------------+---------------------+
|  1 | Геннадий           | 1990-10-05  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
|  2 | Наталья            | 1984-11-12  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
|  3 | Александр          | 1985-05-20  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
|  4 | Сергей             | 1988-02-14  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
|  5 | Иван               | 1998-01-12  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
|  6 | Мария              | 1992-08-29  | 2020-06-23 12:32:05 | 2020-06-23 12:32:05 |
+----+--------------------+-------------+---------------------+---------------------+

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT NULL,
  updated_at DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at, created_at, updated_at) VALUES
  ('Геннадий', '1990-10-05',NOW(),NOW()),
  ('Наталья', '1984-11-12',NOW(),NOW()),
  ('Александр', '1985-05-20',NOW(),NOW()),
  ('Сергей', '1988-02-14',NOW(),NOW()),
  ('Иван', '1998-01-12',NOW(),NOW()),
  ('Мария', '1992-08-29',NOW(),NOW());

 mysql> select * from users;
+----+--------------------+-------------+---------------------+---------------------+
| id | name               | birthday_at | created_at          | updated_at          |
+----+--------------------+-------------+---------------------+---------------------+
|  1 | Геннадий           | 1990-10-05  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
|  2 | Наталья            | 1984-11-12  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
|  3 | Александр          | 1985-05-20  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
|  4 | Сергей             | 1988-02-14  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
|  5 | Иван               | 1998-01-12  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
|  6 | Мария              | 1992-08-29  | 2020-06-23 13:11:07 | 2020-06-23 13:11:07 |
+----+--------------------+-------------+---------------------+---------------------+


ALTER TABLE users 
MODIFY COLUMN created_at VARCHAR(255) default '0', 
MODIFY COLUMN updated_at VARCHAR(255) default '0';

truncate users;

SELECT * FROM users;
Empty set (0,01 sec)

/* 2. Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR
 *  и в них долгое время помещались значения в формате "20.10.2017 8:10". Необходимо преобразовать поля 
 * к типу DATETIME, сохранив введеные ранее значения.*/
INSERT INTO users (name, birthday_at,created_at,updated_at) 
VALUES
  ('Геннадий', '1990-10-05','20.10.2017 8:10','20.10.2017 8:10'),
  ('Наталья', '1984-11-12','20.10.2017 8:10','20.10.2017 8:10'),
  ('Александр', '1985-05-20','20.10.2017 8:10','20.10.2017 8:10'),
  ('Сергей', '1988-02-14','20.10.2017 8:10','20.10.2017 8:10'),
  ('Иван', '1998-01-12','20.10.2017 8:10','20.10.2017 8:10'),
  ('Мария', '1992-08-29','20.10.2017 8:10','20.10.2017 8:10');
 
ALTER TABLE users 
ADD COLUMN created_at_dt DATETIME,
ADD COLUMN updated_at_dt DATETIME;
+----+--------------------+-------------+-----------------+-----------------+---------------+---------------+
| id | name               | birthday_at | created_at      | updated_at      | created_at_dt | updated_at_dt |
+----+--------------------+-------------+-----------------+-----------------+---------------+---------------+
|  1 | Геннадий           | 1990-10-05  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
|  2 | Наталья            | 1984-11-12  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
|  3 | Александр          | 1985-05-20  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
|  4 | Сергей             | 1988-02-14  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
|  5 | Иван               | 1998-01-12  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
|  6 | Мария              | 1992-08-29  | 20.10.2017 8:10 | 20.10.2017 8:10 | NULL          | NULL          |
+----+--------------------+-------------+-----------------+-----------------+---------------+---------------+

UPDATE users 
SET created_at_dt= STR_TO_DATE(created_at, '%d.%m.%Y %h:%i'),
	updated_at_dt= STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');

mysql> SELECT * FROM users;
+----+--------------------+-------------+-----------------+-----------------+---------------------+---------------------+
| id | name               | birthday_at | created_at      | updated_at      | created_at_dt       | updated_at_dt       |
+----+--------------------+-------------+-----------------+-----------------+---------------------+---------------------+
|  1 | Геннадий           | 1990-10-05  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  2 | Наталья            | 1984-11-12  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  3 | Александр          | 1985-05-20  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  4 | Сергей             | 1988-02-14  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  5 | Иван               | 1998-01-12  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  6 | Мария              | 1992-08-29  | 20.10.2017 8:10 | 20.10.2017 8:10 | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
+----+--------------------+-------------+-----------------+-----------------+---------------------+---------------------+

ALTER TABLE users 
DROP created_at, 
DROP updated_at,
RENAME COLUMN created_at_dt TO created_at, 
RENAME COLUMN updated_at_dt TO updated_at;
mysql> SELECT * FROM users;
+----+--------------------+-------------+---------------------+---------------------+
| id | name               | birthday_at | created_at          | updated_at          |
+----+--------------------+-------------+---------------------+---------------------+
|  1 | Геннадий           | 1990-10-05  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  2 | Наталья            | 1984-11-12  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  3 | Александр          | 1985-05-20  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  4 | Сергей             | 1988-02-14  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  5 | Иван               | 1998-01-12  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  6 | Мария              | 1992-08-29  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
+----+--------------------+-------------+---------------------+---------------------+

/* 3. 
 * В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, 
 * если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, 
 * чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
 */

mysql> SELECT value FROM storehouses_products ORDER BY IF(value = 0,1,0), value;
+-------+
| value |
+-------+
|     5 |
|    12 |
|    25 |
|    30 |
|   140 |
|     0 |
|     0 |
+-------+

/* 4.(по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
 * Месяцы заданы в виде списка английских названий ('may', 'august')
 * */

select id, name, (select MONTHNAME(birthday_at)) as MONTH_NAME
from users u 
where MONTH(birthday_at) = 5 OR MONTH(birthday_at) = 8;
+----+--------------------+------------+
| id | name               | MONTH_NAME |
+----+--------------------+------------+
|  3 | Александр          | May        |
|  6 | Мария              | August     |
+----+--------------------+------------+




/* 5.(по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
 * Отсортируйте записи в порядке, заданном в списке IN.
 * */

SELECT *
FROM catalogs WHERE id IN (5, 1, 2) ORDER BY FIELD(id,5,1,2);

+----+-------------------------------------+
| id | name                                |
+----+-------------------------------------+
|  5 | Оперативная память                  |
|  1 | Процессоры                          |
|  2 | Материнские платы                   |
+----+-------------------------------------+

-- "Агрегация данных"

/* 1 Подсчитайте средний возраст пользователей в таблице users*/
mysql> SELECT
    -> name,
    -> TIMESTAMPDIFF(Year,birthday_at,NOW()) AS age
    -> FROM
    -> users;

+--------------------+------+
| name               | age  |
+--------------------+------+
| Геннадий           |   29 |
| Наталья            |   35 |
| Александр          |   35 |
| Сергей             |   32 |
| Иван               |   22 |
| Мария              |   27 |
+--------------------+------+

mysql> SELECT  AVG(TIMESTAMPDIFF(Year,birthday_at,NOW())) as age from  users;
+---------+
| age     |
+---------+
| 30.0000 |
+---------+

/* 2 Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
 *Следует учесть, что необходимы дни недели текущего года, а не года рождения.*/

mysql> SELECT DATE_FORMAT(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(birthday_at), DAY(birthday_at))),'%W') AS day_in_week, 
COUNT(*) AS total
FROM users 
GROUP BY day_in_week DESC ;

+-------------+-------+
| day_in_week | total |
+-------------+-------+
| Monday      |     1 |
| Thursday    |     1 |
| Wednesday   |     1 |
| Friday      |     1 |
| Sunday      |     1 |
| Saturday    |     1 |
+-------------+-------+

/* 3. (по желанию) Подсчитайте произведение чисел в столбце таблицы*/

drop table if exists numbers;
create table numbers(
	value INT
);

insert into numbers (value) values (1),(2),(3),(4);
select * from numbers
+-------+
| value |
+-------+
|     1 |
|     2 |
|     3 |
|     4 |
+-------+

select ROUND(exp(SUM(log(value)))) as _RESULT_ from numbers n 
+----------+
| _RESULT_ |
+----------+
|       24 |
+----------+

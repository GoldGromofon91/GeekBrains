-- “Транзакции, переменные, представления”
/* 1. В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
   Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
*/
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shop               |
| sys                |
| vk                 |
+--------------------+

mysql> DROP DATABASE IF EXISTS sample;
mysql> CREATE DATABASE sample;
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| shop               |
| sys                |
| vk                 |
+--------------------+

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';

START TRANSACTION;
INSERT sample.users SELECT * FROM shop.users WHERE id = 1;
COMMIT;

mysql> SELECT * FROM sample.users;
+----+------------------+-------------+---------------------+---------------------+
| id | name             | birthday_at | created_at          | updated_at          |
+----+------------------+-------------+---------------------+---------------------+
|  1 | Геннадий         | 1990-10-05  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
+----+------------------+-------------+---------------------+---------------------+


/* 2.Создайте представление, которое выводит название name товарной позиции из таблицы 
 * products и соответствующее название каталога name из таблицы catalogs.*/

create or replace view view_1(prod_id, product_name, catalog_name) AS 
select products.id, products.name, catalogs.name 
from products
left join catalogs 
ON products.catalog_id = catalogs.id;

mysql> select * from view_1;
+---------+-------------------------+-----------------------------------+
| prod_id | product_name            | catalog_name                      |
+---------+-------------------------+-----------------------------------+
|       1 | Intel Core i3-8100      | Процессоры                        |
|       2 | Intel Core i5-7400      | Процессоры                        |
|       3 | AMD FX-8320E            | Процессоры                        |
|       4 | AMD FX-8320             | Процессоры                        |
|       5 | ASUS ROG MAXIMUS X HERO | Материнские платы                 |
|       6 | Gigabyte H310M S2H      | Материнские платы                 |
|       7 | MSI B250M GAMING PRO    | Материнские платы                 |
+---------+-------------------------+-----------------------------------+


-- "Хранимые процедуры и функции, триггеры"
/* 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
 * с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
 * */
DELIMITER //
DROP PROCEDURE IF EXISTS hello//

CREATE PROCEDURE hello()
BEGIN
	IF(CURTIME() BETWEEN '06:00:00' AND '12:00:00') THEN
		SELECT 'Доброе утро';
	ELSEIF(CURTIME() BETWEEN '12:00:00' AND '18:00:00') THEN
		SELECT 'Добрый день';
	ELSEIF(CURTIME() BETWEEN '18:00:00' AND '00:00:00') THEN
		SELECT 'Добрый вечер';
	ELSE
		SELECT 'Доброй ночи';
	END IF;
END//
DELIMITER ;
CALL hello();

/* 2. В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того,чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.
 * */

drop trigger if exists no_name_trigger;
delimiter //
create trigger no_name_trigger before insert on products
for each row
BEGIN
	IF(ISNULL(NEW.name) AND ISNULL(NEW.description)) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error! Two row is NULL';
	END IF;
END //
delimiter ;

mysql> INSERT INTO products (name, description, price, catalog_id)
    -> VALUES (NULL, NULL, 5000, 2); 
ERROR 1644 (45000): Error! Two row is NULL

INSERT INTO products (name, description, price, catalog_id)
VALUES ('AVG', NULL, 5000, 2);

mysql> mysql> select * from products where name ='AVG';
+----+------+-------------+---------+------------+---------------------+---------------------+
| id | name | description | price   | catalog_id | created_at          | updated_at          |
+----+------+-------------+---------+------------+---------------------+---------------------+
|  9 | AVG  | NULL        | 5000.00 |          2 | 2020-07-07 16:01:19 | 2020-07-07 16:01:19 |
+----+------+-------------+---------+------------+---------------------+---------------------+



-- Задания по желанию
/*
 * по желанию) Пусть имеется таблица с календарным полем created_at. 
 * В ней размещены разряженые календарные записи за август 2018 года '2018-08-01', '
 * 2016-08-04', '2018-08-16' и 2018-08-17. Составьте запрос, который выводит полный список 
 * дат за август, выставляя в соседнем поле значение 1, если дата присутствует в исходном 
 * таблице и 0, если она отсутствует.*/

drop table if exists calendar;
create table calendar(
	-- id SERIAL,
	created_at DATE
);

call sp_create_day('2020-08-01','2020-08-31'); 



drop table if exists diff_date;
create table diff_date(
	-- id SERIAL,
	created_at DATE
);

insert into diff_date (created_at )
values ('2020-08-01'),
	('2020-08-12'),
	('2020-08-25'),
	('2020-08-13'),
	('2020-08-07'),
	('2020-08-03');

select
  calendar.created_at as cal_day,
  if(diff_date.created_at is null, 0, 1) as day_rand
from calendar
left join diff_date
on calendar.created_at = diff_date.created_at;


+------------+----------+
| cal_day    | day_rand |
+------------+----------+
| 2020-08-01 |        1 |
| 2020-08-12 |        1 |
| 2020-08-25 |        1 |
| 2020-08-13 |        1 |
| 2020-08-07 |        1 |
| 2020-08-03 |        1 |
| 2020-08-02 |        0 |
| 2020-08-04 |        0 |
| 2020-08-05 |        0 |
| 2020-08-06 |        0 |
| 2020-08-08 |        0 |
| 2020-08-09 |        0 |
| 2020-08-10 |        0 |
| 2020-08-11 |        0 |
| 2020-08-14 |        0 |
| 2020-08-15 |        0 |
| 2020-08-16 |        0 |
| 2020-08-17 |        0 |
| 2020-08-18 |        0 |
| 2020-08-19 |        0 |
| 2020-08-20 |        0 |
| 2020-08-21 |        0 |
| 2020-08-22 |        0 |
| 2020-08-23 |        0 |
| 2020-08-24 |        0 |
| 2020-08-26 |        0 |
| 2020-08-27 |        0 |
| 2020-08-28 |        0 |
| 2020-08-29 |        0 |
| 2020-08-30 |        0 |
| 2020-08-31 |        0 |
+------------+----------+











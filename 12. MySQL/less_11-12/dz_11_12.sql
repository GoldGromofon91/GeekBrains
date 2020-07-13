-- Практическое задание по теме “Оптимизация запросов”
/* 1. Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу 
 * logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля name.
*/

DROP TABLE IF EXISTS logs;
CREATE TABLE logs(
	id BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
	id_string BIGINT NOT NULL,
	from_tbl CHAR(15),
	content_from_table VARCHAR(100),
	created_at DATETIME DEFAULT NOW()
) ENGINE Archive;

-- Trigger for users
DROP TRIGGER IF EXISTS `tr_users_to_logs`;

DELIMITER //
DROP TRIGGER IF EXISTS `tr_users_to_logs`//
CREATE TRIGGER `tr_users_to_logs` AFTER INSERT ON `users` FOR EACH ROW 
BEGIN
	INSERT INTO logs (id_string,from_tbl,content_from_table) VALUES (NEW.id,'users',NEW.name);
END //

DELIMITER ;

-- Trigger for catalogs
DROP TRIGGER IF EXISTS `tr_catalogs_to_logs`;

DELIMITER //
DROP TRIGGER IF EXISTS `tr_catalogs_to_logs`//
CREATE TRIGGER `tr_catalogs_to_logs` AFTER INSERT ON `catalogs` FOR EACH ROW 
BEGIN
	INSERT INTO logs (id_string,from_tbl,content_from_table) VALUES (NEW.id,'catalogs',NEW.name);
END //

DELIMITER ;

-- Trigger for products
DROP TRIGGER IF EXISTS `tr_products_to_logs`;

DELIMITER //
DROP TRIGGER IF EXISTS `tr_products_to_logs`//
CREATE TRIGGER `tr_products_to_logs` AFTER INSERT ON `products` FOR EACH ROW 
BEGIN
	INSERT INTO logs (id_string,from_tbl,content_from_table) VALUES (NEW.id,'products',NEW.name);
END //

DELIMITER ;
INSERT INTO users(id , name) VALUES (11,'FDF');
INSERT INTO catalogs (id , name) VALUES (6,'Аксессуары');
INSERT INTO products (id , name,description ,price ,catalog_id) VALUES (10,'Клавиатура Genius RX-750',NULL,3000,6);

SELECT * FROM logs;
+----+-----------+----------+------------------------------------+---------------------+
| id | id_string | from_tbl | content_from_table                 | created_at          |
+----+-----------+----------+------------------------------------+---------------------+
|  1 |        11 | users    | FDF                                | 2020-07-13 12:06:36 |
|  2 |         6 | catalogs | Аксессуары                         | 2020-07-13 12:09:29 |
|  3 |        10 | products | Клавиатура Genius RX-750           | 2020-07-13 12:14:15 |
+----+-----------+----------+------------------------------------+---------------------+

/*(по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион(n-e количество записей) записей.*/

DELETE FROM users WHERE birthday_at IS NULL AND name = 'павл';
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
CREATE PROCEDURE shop.sp_mill_user ()
BEGIN
	DECLARE i INT DEFAULT 10;
	DECLARE j INT DEFAULT 1;
	WHILE i > 0 DO
		INSERT INTO users(name, birthday_at) VALUES (CONCAT('user_', j), NOW());
		SET j = j + 1;
		SET i = i - 1;
	END WHILE;
END

CALL sp_mill_user(); 

SELECT * FROM users
+----+--------------------+-------------+---------------------+---------------------+
| id | name               | birthday_at | created_at          | updated_at          |
+----+--------------------+-------------+---------------------+---------------------+
|  1 | Геннадий           | 1990-10-05  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  2 | Наталья            | 1984-11-12  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  3 | Александр          | 1985-05-20  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  4 | Сергей             | 1988-02-14  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  5 | Иван               | 1998-01-12  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
|  6 | Мария              | 1992-08-29  | 2017-10-20 08:10:00 | 2017-10-20 08:10:00 |
| 13 | user_1             | 2020-07-13  | NULL                | NULL                |
| 14 | user_2             | 2020-07-13  | NULL                | NULL                |
| 15 | user_3             | 2020-07-13  | NULL                | NULL                |
| 16 | user_4             | 2020-07-13  | NULL                | NULL                |
| 17 | user_5             | 2020-07-13  | NULL                | NULL                |
| 18 | user_6             | 2020-07-13  | NULL                | NULL                |
| 19 | user_7             | 2020-07-13  | NULL                | NULL                |
| 20 | user_8             | 2020-07-13  | NULL                | NULL                |
| 21 | user_9             | 2020-07-13  | NULL                | NULL                |
| 22 | user_10            | 2020-07-13  | NULL                | NULL                |
+----+--------------------+-------------+---------------------+---------------------+



-- Практическое задание по теме “NoSQL”

/* 1. В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.*/
-- вариант с Добавлением в хэш -таблицы
>redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> HSET ip_user '172.0.0.1' '1' 
(integer) 1
127.0.0.1:6379> HSET ip_user '172.0.0.2' '0' 
(integer) 1
127.0.0.1:6379> HSET ip_user '172.0.0.3' '3' 
(integer) 1
127.0.0.1:6379> HSET ip_user '172.0.0.1' '4' 
(integer) 0
127.0.0.1:6379> HGETALL ip_user
1) "172.0.0.1"
2) "4"
3) "172.0.0.2"
4) "0"
5) "172.0.0.3"
6) "3"

-- вариант с добавлением в множества, где только уникальные значения
127.0.0.1:6379> SADD user_ip '172.0.0.1' '172.0.0.2' '172.0.0.3'
(integer) 3
127.0.0.1:6379> SMEMBERS user_ip
1) "172.0.0.1"
2) "172.0.0.3"
3) "172.0.0.2"
127.0.0.1:6379> SCARD user_ip
(integer) 3


/* 2. При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, 
поиск электронного адреса пользователя по его имени.*/

-- В Redis поиск осуществляется только по ключу поэтому обозначим ключ имя(емаил)
 
127.0.0.1:6379> SET Bruce bruce@mail.ru
OK
127.0.0.1:6379> GET Bruce
"bruce@mail.ru"
127.0.0.1:6379> SET lena@rambler.ru Elena
OK
127.0.0.1:6379> GET lena@rambler.ru
"Elena"


/* 3.Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB. */
> use catalogs
> db.catalogs.insertMany([{"name":"CPU"},{"name":"MotherBoard"},{"name":"Video Card"}])
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("5f0c4fe448d9cc3065a8ab9c"),
		ObjectId("5f0c4fe448d9cc3065a8ab9d"),
		ObjectId("5f0c4fe448d9cc3065a8ab9e")
	]
}
> > db.catalogs.find()
{ "_id" : ObjectId("5f0c4fe448d9cc3065a8ab9c"), "name" : "CPU" }
{ "_id" : ObjectId("5f0c4fe448d9cc3065a8ab9d"), "name" : "MotherBoard" }
{ "_id" : ObjectId("5f0c4fe448d9cc3065a8ab9e"), "name" : "Video Card" }
> 
use products
db.catalogs.insertMany([{"name":"CPU"},{"name":"MotherBoard"},{"name":"Video Card"}])


> db.products.find()
{ "_id" : ObjectId("5f0c522fdd236a9bc62cc13f"), 
	"name" : "Intel Core i3-8100", 
	"description" : "CPU for PC in Intel", 
	"price" : "3000.00", 
	"catalog" : "CPU", 
	"created_at" : "Mon Jul 13 2020 15:23:11 GMT+0300 (MSK)" }
-- Добавили ключ updated_at
> db.products.update({name: 'Intel Core i3-8100'}, {$push: {'products.updated_at': Date()}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.products.find()
{ "_id" : ObjectId("5f0c522fdd236a9bc62cc13f"), 
	"name" : "Intel Core i3-8100", 
	"description" : "CPU for PC in Intel", 
	"price" : "3000.00", 
	"catalog" : "CPU", 
	"created_at" : "Mon Jul 13 2020 15:23:11 GMT+0300 (MSK)", 
	"products" : { "updated_at" : [ "Mon Jul 13 2020 15:27:23 GMT+0300 (MSK)" ] } }



>db.products.insertMany([
	{"name": "AMD FX-8320", "description": "Процессор для настольных ПК", "price": "4000.00", "catalog_id": "Процессоры", "created_at": new Date(), "updated_at": new Date()},
	{"name": "AMD FX-8320E", "description": "Процессор для настольных ПК", "price": "4500.00", "catalog_id": "Процессоры", "created_at": new Date(), "updated_at": new Date()}])





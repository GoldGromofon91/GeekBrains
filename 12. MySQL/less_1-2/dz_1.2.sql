/* 1. Установите СУБД MySQL. Создайте в домашней директории файл .my.cnf, 
 задав в нем логин и пароль, который указывался при установке.*/
brew install mysql
cd ~
cat >.my.cnf
[client]
user=root
password=
/* 2.Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, 
 числового id и строкового name.*/
mysql example
>DROP TABLE IF EXISTS users;
> CREATE table users (
		id INT UNSIGNED,
		name VARCHAR COMMENT 'имя_пользователя'
>);
>DESCRIBE users;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| id    | int unsigned | YES  |     | NULL    |       |
| name  | varchar(255) | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
/* 3. Создайте дамп базы данных example из предыдущего задания, 
 * разверните содержимое дампа в новую базу данных sample.*/

+--------------------+
| Database           |
+--------------------+
| example            |
| first              |
| information_schema |
| mysql              |
| performance_schema |       
| sys                |
+--------------------+
mysqldump example > sample/example.sql
mysql sample < sample/example.sql
mysql sample 
>show tables;
+------------------+
| Tables_in_sample |
+------------------+
| users            |
+------------------+

>show databases;
+--------------------+
| Database           |
+--------------------+
| example            |
| first              |
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| sys                |
+--------------------+
>describe users;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| id    | int unsigned | YES  |     | NULL    |       |
| name  | varchar(255) | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
>\q;
/*Создайте дамп единственной таблицы help_keyword базы данных mysql. 
 Причем добейтесь того, чтобы дамп содержал только первые 100 строк таблицы.*/
mysqldump --were='true limil 100' mysql help_keyword > ~/Descktop/1/help_keyword.sql
mysql 
> CREATE DATABASE key_;
>SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| example            |
| key_				 |
| information_schema |
| mysql              |
| performance_schema |
| sample             |
| sys                |

mysqldump key_ < ~/Descktop/1/help_keyword.sql


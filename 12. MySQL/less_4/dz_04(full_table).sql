-- Заполнение таблиц

USE vk;

-- заполняем пользователей
INSERT INTO users (`id`, `first_name`, `last_name`, `email`, `password_hash`, `phone`)
VALUES 
('1', 'Daren', 'Ryan', 'brakus.alvina@example.net', '322a76879289e5b57a66abefda54957721d1ee62', '89548139731'),
('2', 'Leda', 'Smith', 'carroll.treva@example.org', 'e1922c3e2fd2c9e5451bf28d9fa68b715338baaa', '89452446051'),
('3', 'Lambert', 'Leffler', 'orland38@example.com', '2375158be0a830c483aaced56e873078708922ba', '89514199955'),
('4', 'Aliyah', 'Mann', 'eloisa.marvin@example.org', 'd73dfc9b72b573343fcc467560678e36c2d05e47', '89461129690'),
('5', 'Kiana', 'Collier', 'xwhite@example.com', 'b6142aafd19cf03e5a270b36f105a049a093f495', '89458428910'),
('6', 'Joana', 'Sanford', 'bashirian.eleanora@example.org', '02837639f2e3ad1127c17cfda1da62864e1bb4ae', '89101487379'),
('7', 'Myles', 'Hackett', 'friesen.francesca@example.com', 'c7e8700c62e6ea687d651f9420bd59003423cda2', '89016874772'),
('8', 'Shanelle', 'Jones', 'sanford89@example.org', 'b0475b03634aa2416ea335d3a2c8534fb82903d1', '89799800205'),
('9', 'Haley', 'Hills', 'trinity24@example.org', 'fb26bb422ba32821616a99edac5fc679115ce622', '89049995369'),
('10', 'Velva', 'Mertz', 'iwalter@example.net', 'c7cdaa1c35e4505d374827b49462653913807a00', '89514275237'),
('11', 'Schuyler', 'Waters', 'hosea.howe@example.net', 'fd5fd06a6f2e1f8d4d4a44bf164e49200282195e', '89000532612'),
('12', 'Trever', 'Eichmann', 'rosie.schoen@example.com', '132c067172b9478b210d93190120914f2ef284fb', '89907985315'),
('13', 'Rachelle', 'Volkman', 'laisha51@example.net', '1b4c89f885c424be3818f288478a6321ab08f329', '89814184011'),
('14', 'Khalil', 'Dare', 'qwaters@example.org', '8db478b26f704b1a8629fdadb5d501ae7616cf53', '89357650772'),
('15', 'Frank', 'Doyle', 'khackett@example.net', '7cb82b9ebfdeffa9fe987a645bc465686f207ce2', '89187581661');

INSERT INTO users (`first_name`, `last_name`, `email`, `password_hash`, `phone`)
VALUES 
('Alex', 'Ronan', 'alex.alvina@example.net', '911a76879289e5b57a66abefda54957721d1ee62', '89548139999'),
('Alex', 'Figiero', 'figiero.treva@example.org', 'e12322c3e2fd2c9e5451bf28d9fa68b715338baa', '89452446052'),
('Ivan', 'Golovin', 'golovin38@example.com', '2373158be0a830c483aaced56e873078708922ba', '89514199956'),
('Ivan', 'Matinyan', 'iva.marvin@example.org', 'd73dfc9b72b573343fcc467560678e36c2d05e46', '89461129691'),
('Kiana', 'Wolf', 'xwoolf@example.com', 'b6141aafd19cf03e5a270b36f105a049a093f495', '89458428911');

-- заполнили таблицу статусов
INSERT INTO status_man (status_name)
VALUES 
('Свободен'), ('В поиске'), ('Счастлив');

-- заполнили таблицу типов меди файлов
INSERT INTO media_type (media_type_name )
VALUES ('.jpeg'),('.png'),('.svg'),('.gif'),('.avi'),('.mpeg'),('.mov'),('.wav'),('.mp3');

-- Заполнили сообщества 
INSERT INTO community (community_id,community_name , community_admin_id)
VALUES 
('1','geekbrains','1'),
('2','habrahabr','5'),
('3','stack_over_flow','10'),
('4','Привет_как_дела','15'),
('5','Workout','20');

-- Заполнили какие пользователи в каких сообществах состоят
INSERT INTO user_community (user_id , community_id )
VALUES 
('1','1'),('2','4'),('3','5'),('4','2'),('5','2'),('6','1'),('7','3'),('8','3'),('9','4'),('10','3'),
('11','5'),('12','5'),('13','2'),('14','2'),('15','4'),('16','1'),('17','3'),('18','2'),('19','4'),('20','5');

-- заполнили приглашения
-- Enum('отправлен','в ожидании','подтвержден','отклонен'),
INSERT INTO friends_request (friend_initiator_id , friend_victim_id , request_status )
VALUES 
('1','10','отправлен'),('2','3','отправлен'),('2','4','отправлен'),('10','20','отправлен'),('3','5','отправлен'),('4','6','отправлен'),
('6','7','отправлен'),('11','13','отправлен'),('12','1','отправлен'),('19','8','отправлен'),('17','16','отправлен'),('13','2','отправлен'),
('18','1','отправлен'),('6','14','отправлен'),('15','10','отправлен'),('17','7','отправлен'),('14','2','отправлен'),('20','1','отправлен');

UPDATE friends_request
SET request_status='подтвержден'
WHERE friend_initiator_id=1 AND friend_victim_id=10;

UPDATE friends_request
SET request_status='отклонен'
WHERE friend_initiator_id=11 AND friend_victim_id=13;

UPDATE friends_request
SET request_status='в ожидании'
WHERE friend_initiator_id=2 AND friend_victim_id=3;

UPDATE friends_request
SET request_status='в ожидании'
WHERE friend_initiator_id=2 AND friend_victim_id=4;

UPDATE friends_request
SET request_status='в ожидании'
WHERE friend_initiator_id=3 AND friend_victim_id=5;

UPDATE friends_request
SET request_status='отклонен'
WHERE friend_initiator_id=20 AND friend_victim_id=1;

UPDATE friends_request
SET request_status='подтвержден'
WHERE friend_initiator_id=18 AND friend_victim_id=1;

UPDATE friends_request
SET request_status='подтвержден'
WHERE friend_initiator_id=9 AND friend_victim_id=8;

-- Сообщение между пользователями

INSERT INTO massange (massange_id ,from_user_id , to_user_id , massange_body )
VALUES ('1','13','10','Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Eius expedita eos nisi commodi veritatis quod corporis facere? Quam recusandae 
ut quidem, nobis voluptatum minima amet, ipsam aliquid facilis quis. Pariatur!');

INSERT INTO massange (massange_id ,from_user_id , to_user_id , massange_body )
VALUES 
('2','2','11','Lorem HI!'),
('3','14','18','Lorem ipsum dolor sit amet, consectetur 
adipisicing elit. Qui dignissimos asperiores debitis in nam omnis, suscipit ab illum non, 
voluptatum aperiam, corporis modi fugit mollitia laborum quaerat eligendi impedit tempore. 
Error quia odit eligendi eveniet nihil tenetur in voluptatum a ad adipisci corrupti, beatae 
laboriosam officiis quae qui ut, reiciendis quibusdam! Perferendis reiciendis natus modi neque, 
harum quaerat. Blanditiis suscipit delectus animi maiores, doloribus quasi possimus temporibus 
voluptas explicabo odio ipsam repellendus quidem voluptatum laudantium autem ipsa maxime neque 
sint veritatis magni eos. Delectus sit voluptatem nobis dolores animi earum numquam deserunt excepturi, 
molestias quo nostrum doloremque aliquid eaque iste.'),
('11','10','4','text for example');

-- Селект запрос на выборку только уникальных имен в алфавитном порядке
SELECT DISTINCTROW (first_name)
FROM vk.users;


-- Селект запросы на вывод тех кому больше 18-ти


INSERT INTO profiles (`profile_id`, `photo__profile_id`, `gender`, `birthday`, `home_city`, `created_at`, `status_life`)
VALUES ('1', '1', NULL, '2014-10-03', 'North Vita', '1998-10-22 09:42:33', '1'),
('2', '2', NULL, '1970-08-03', 'Boyerton', '1990-11-20 06:33:36', '2'),
('3', '3', NULL, '1976-11-23', 'Port Stonefort', '1990-10-29 01:41:34', '2'),
('4', '4', NULL, '1986-01-04', 'South Gregshire', '1992-03-14 16:56:32', '3'),
('5', '5', NULL, '2017-05-31', 'Spinkashire', '1970-01-21 17:07:09', '1'),
('6', '6', NULL, '2013-10-14', 'Thoramouth', '1978-01-18 05:14:34', '2'),
('7', '7', NULL, '1992-11-12', 'South Elisashire', '2017-01-15 23:11:37', '1'),
('8', '8', NULL, '2006-11-02', 'New Austenburgh', '2000-10-19 20:51:09', '1'),
('9', '9', NULL, '2013-03-13', 'East Celestine', '2004-10-24 05:58:59', '1'),
('10', '10', NULL, '2014-09-05', 'West Beulah', '2010-08-07 12:46:28', '3'),
('11', '11', NULL, '1994-04-19', 'Lonzoview', '1993-01-17 12:40:21', '2'),
('12', '12', NULL, '2001-01-14', 'East Riverhaven', '2017-02-22 16:50:01', '1'),
('13', '13', NULL, '1971-06-06', 'Trantowbury', '2011-11-19 20:31:45', '2'),
('14', '14', NULL, '1977-07-06', 'Lake Felipe', '1975-01-01 03:51:39', '3'),
('15', '15', NULL, '1972-02-29', 'New Evelyn', '1989-03-04 02:51:07', '1'),
('16', '16', NULL, '2006-07-08', 'East Christinetown', '1997-11-21 16:43:10', '1'),
('17', '17', NULL, '2001-10-23', 'West Paul', '2009-02-11 01:50:37', '2'),
('18', '18', NULL, '2004-11-26', 'East Rooseveltborough', '1989-07-01 12:38:05', '1'),
('19', '19', NULL, '1986-09-13', 'West Tiana', '1978-02-02 09:39:03', '1'),
('20', '20', NULL, '1981-07-28', 'East Natashaview', '1970-08-25 08:05:02', '1');

-- Добавили столбец is_active
ALTER TABLE profiles ADD is_ACTIVE BIT DEFAULT 1 NULL;
-- Обновили значение is_active у людей кто младше 18-ти
UPDATE profiles 
SET is_ACTIVE = 0
WHERE  (YEAR(CURRENT_DATE)-YEAR(birthday)) - (RIGHT(CURRENT_DATE,5) < RIGHT(birthday, 5)) < 18; 


-- Удаляем сообщения из будующего

INSERT INTO massange (massange_id ,from_user_id , to_user_id , massange_body ,created_at )
VALUES ('6','11','20','Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Eius expedita eos nisi commodi veritatis quod corporis facere? Quam recusandae 
ut quidem, nobis voluptatum minima amet, ipsam aliquid facilis quis. Pariatur!','2020-09-15');

DELETE FROM massange
WHERE DATE(created_at) > CURRENT_DATE(); 
















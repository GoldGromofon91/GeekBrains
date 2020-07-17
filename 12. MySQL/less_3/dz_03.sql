DROP database if exists vk;
CREATE database vk;
use vk;
-- SERIAL = BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(25),
	last_name VARCHAR(25),
	email VARCHAR(100) UNIQUE,
	password_hash VARCHAR(100),
	phone BIGINT UNSIGNED UNIQUE,
	INDEX user_name_idx(first_name,last_name) -- поиск по имени/фамилии
);

-- 1 to 1
DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	profile_id BIGINT UNSIGNED NOT NULL UNIQUE,
	photo__profile_id BIGINT UNSIGNED NULL,
	gender CHAR(1),
	birthday DATE,
	home_city VARCHAR(100),
	created_at DATETIME DEFAULT NOW(),
	status_life BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (profile_id) REFERENCES users(id)
    -- FOREIGN KEY (photo__profile_id) REFERENCES media(фото_id)
);

-- 1 to M
DROP TABLE IF EXISTS message;
CREATE TABLE message (
	message_id BIGINT UNSIGNED NOT NULL UNIQUE,
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	massange_body TEXT,
	created_at DATETIME DEFAULT NOW(),
	
	FOREIGN KEY (from_user_id) REFERENCES users(id),
	FOREIGN KEY (to_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS friends_request;
CREATE TABLE friends_request (
	friend_initiator_id BIGINT UNSIGNED NOT NULL,
	friend_victim_id BIGINT UNSIGNED NOT NULL,
	request_status ENUM ('отправлен','в ожидании','подтвержден','отклонен'),
	request_time DATETIME DEFAULT NOW(), -- время отпрвки запроса
	confirmed_time DATETIME ON UPDATE NOW(), -- время подтверждения/отклонения запроса
	
	PRIMARY KEY (friend_initiator_id, friend_victim_id),
	FOREIGN KEY (friend_initiator_id) REFERENCES users(id),
	FOREIGN KEY (friend_victim_id) REFERENCES users(id),
	CHECK (friend_initiator_id <> friend_victim_id)
);

-- M to M
DROP TABLE IF EXISTS community; -- сообщества (отношение многие ко многим)
CREATE TABLE community (
	community_id BIGINT UNSIGNED NOT NULL UNIQUE,
	community_name VARCHAR(200),
	community_admin_id BIGINT UNSIGNED NOT NULL,
	community_created_at DATETIME DEFAULT NOW(), 
	
	INDEX community_name_idx(community_name),
	FOREIGN KEY (community_admin_id) REFERENCES users(id)	
);

-- создаем доп.таблицу с у-мя полями внешние ключи которой связывают две разные таблицы users и community
DROP TABLE IF EXISTS user_community; 
CREATE TABLE user_community (
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, community_id), -- чтобы не было 2 записей о пользователе и сообществе
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (community_id) REFERENCES community(community_id)
);

DROP TABLE IF EXISTS media_type;  -- абстрактная таблица с медиа-типами
CREATE TABLE media_type (
	id SERIAL,
	media_type_name VARCHAR(255)
);

DROP TABLE IF EXISTS content; -- все что выкладывает пользваотель (фото/видео/текст) 
CREATE TABLE content (
	id SERIAL,
	body TEXT,
	/* Для хранения типов данных(можно использовать ENUM и перечилсять)
	 * а можно пойти путем "справочной таблицы"
	 * */ 
	media_type_id BIGINT UNSIGNED NOT NULL,
	user_id  BIGINT UNSIGNED NOT NULL,-- id пользвоателя который выложил контент
	status_likes ENUM ('like','None'),
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE NOW(), 
	-- *Поля для хранения данных
	filename VARCHAR(255),
	-- file blob,  *способ хранения данных в формате байтов  	
    size INT,
	--metadata JSON, -- *способ хранения данных в файле json формата, представляющим из себя коллецию ключ:значение
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_type_id) REFERENCES media_type(id)
);

DROP TABLE IF EXISTS content_like; 
CREATE TABLE content_like (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL, -- *кто поставил лайки
	media_id BIGINT UNSIGNED NOT NULL, -- *чему поставили лайк
	created_at DATETIME DEFAULT NOW(), -- *когда
	
	FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (media_id) REFERENCES content(id)
);

DROP TABLE IF EXISTS photo_albums;
CREATE TABLE photo_albums (
	id  SERIAL PRIMARY KEY,
	name varchar(255) DEFAULT NULL,
    user_id BIGINT UNSIGNED DEFAULT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
	`id` SERIAL,
	`album_id` BIGINT unsigned NOT NULL,
	`media_id` BIGINT unsigned NOT NULL,

	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
    FOREIGN KEY (media_id) REFERENCES content(id)
);

ALTER TABLE profiles 
ADD CONSTRAINT fk_foto_user_inprofile 
FOREIGN KEY (photo__profile_id) REFERENCES content(id);

DROP TABLE IF EXISTS status_man;  -- таблица статусов для профайла
CREATE TABLE status_man (
	id SERIAL,
	status_name VARCHAR(255)
);

ALTER TABLE profiles 
ADD CONSTRAINT fk_status_user_inprofile 
FOREIGN KEY (status_life) REFERENCES status_man(id),

DROP TABLE IF EXISTS `song_albums`;
CREATE TABLE `song_albums` (
	`id`  SERIAL PRIMARY KEY,
	`name` varchar(255) DEFAULT NULL,
    `user_id` BIGINT UNSIGNED DEFAULT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS `user_song`;
CREATE TABLE `user_song` (
	`id` SERIAL,
	`name_song` VARCHAR (100),
	`album_id` BIGINT unsigned NOT NULL,
	`media_id` BIGINT unsigned NOT NULL,
	INDEX name_song_idx(name_song),

	FOREIGN KEY (album_id) REFERENCES song_albums(id),
    FOREIGN KEY (media_id) REFERENCES content(id)
);


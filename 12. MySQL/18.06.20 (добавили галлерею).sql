DROP TABLE IF EXISTS media_gallery_user;
CREATE TABLE media_gallery_user (
	id_media_user SERIAL PRIMARY KEY,
	photo_album_user BIGINT UNSIGNED NOT NULL UNIQUE,

	FOREIGN KEY (id_media_user) REFERENCES users(id)
);


DROP TABLE IF EXISTS photo_albums;
CREATE TABLE photo_albums (
	id SERIAL,
	name_albums VARCHAR(255),
	photo_in_albums BIGINT UNSIGNED NOT NULL UNIQUE,
	
	INDEX (name_albums,photo_in_albums),
	FOREIGN KEY (id) REFERENCES media_gallery_user(photo_album_user)
);

DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
	`id` SERIAL,
	`album_id` BIGINT UNSIGNED NOT NULL,
	`media_id` BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
    FOREIGN KEY (media_id) REFERENCES photo_albums(photo_in_albums)
);




/* Добавить дпнные после того как наладишь связи между таблицей profile и media_gallery
 * 
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
*/



ALTER TABLE photos 
ADD COLUMN 	type_photo BIGINT UNSIGNED NOT NULL;



ALTER TABLE photos 
ADD CONSTRAINT FK_type_photo 
FOREIGN KEY (type_photo) REFERENCES media_type(id);



DROP TABLE IF EXISTS video_albums;
CREATE TABLE video_albums (
	id SERIAL,
	name_albums VARCHAR(255),
	video_in_albums BIGINT UNSIGNED NOT NULL UNIQUE,
	
	INDEX (name_albums,video_in_albums),
	FOREIGN KEY (id) REFERENCES media_gallery_user(video_album_user)
);

DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
	`id` SERIAL,
	`album_id` BIGINT UNSIGNED NOT NULL,
	`media_id` BIGINT UNSIGNED NOT NULL,

	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
    FOREIGN KEY (media_id) REFERENCES photo_albums(photo_in_albums)
);
















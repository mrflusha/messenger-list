
CREATE TABLE messenger_name(messenger_id int(5),
messenger_title varchar(100),
PRIMARY KEY (messenger_id)
);

CREATE TABLE uploadmax(uploadmax_id int(1),
uploadmax_mb varchar(100),
PRIMARY KEY (uploadmax_id)
);
CREATE TABLE os_sup(os_sup_id int(1),
os_sup_title varchar(100),
PRIMARY KEY (os_sup_id)
);
CREATE TABLE yesorno(yesorno_id int(1),
yesorno_title varchar(100),
PRIMARY KEY (yesorno_id)
);


CREATE TABLE all_messengers(
name varchar (100),
upmax int(1),
supos int(1),
supvideo int(1),
supvs int(1),
supgc int(1),
PRIMARY KEY(name),
FOREIGN KEY(upmax)REFERENCES uploadmax(uploadmax_id),
FOREIGN KEY(supos)REFERENCES os_sup(os_sup_id),
FOREIGN KEY(supvideo)REFERENCES yesorno(yesorno_id),
FOREIGN KEY(supvs)REFERENCES yesorno(yesorno_id),
FOREIGN KEY(supgc)REFERENCES yesorno(yesorno_id)
);



INSERT INTO messenger_name(messenger_id, messenger_title) VALUES
(0,'TELEGRAM'),
(1,'VIBER'),
(2,'WhatsApp'),
(3,'ТамТам'),
(4,'Psi'),
(5,'WeChat'),
(6,'Skype'),
(7,'Signal'),
(8,'Riot.im'),
(9,'VK');
INSERT INTO yesorno(yesorno_id,yesorno_title)VALUES
(0,'Неизвестно'),
(1,'ДА'),
(2,'Нет');
INSERT INTO uploadmax(uploadmax_id,uploadmax_mb)VALUES
(0,'1500mb'),
(1,'200мб'),
(2,'100мб'),
(3, '16 мб'),
(4,'2мб'),
(5,'p2p');
INSERT INTO os_sup(os_sup_id,os_sup_title)VALUES
(0,'android/ios/windows/mac/*nix'),
(1,'android/ios');

INSERT INTO all_messengers(name,upmax,supos,supvideo,supvs,supgc)VALUES
('Telegram', 0, 0, 0, 1, 1),
('Viber', 1, 0, 1, 1, 1),
('VK', 1, 0, 1, 1, 1),
('TamTam', 1, 0, 1, 1, 1),
('WhatsApp', 1, 0, 1, 1, 1),
('Signal', 1, 0, 1, 1, 1),
('WeChat', 1, 0, 1, 1, 1),
('Skype', 1, 0, 1, 1, 1),
('Psi', 1, 0, 1, 1, 1);
select * from messenger_name;
select * from yesorno;
select * from uploadmax;
select * from os_sup;
select * from all_messengers;
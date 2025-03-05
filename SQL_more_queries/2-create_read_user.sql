-- créé la base de données hbtn_0c_0
create database if not exists `hbtn_0c_2`;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Accorde tous les privilèges à user_0d_1
GRANT SELECT ON hbtn_0c_2.* TO 'user_0d_2'@'localhost';

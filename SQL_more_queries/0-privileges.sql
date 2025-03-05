-- Crée l'utilisateur user_0d_1 s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1';
-- Accorde tous les privilèges à user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Crée l'utilisateur user_0d_2 s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

-- Affiche les privilèges des utilisateurs
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
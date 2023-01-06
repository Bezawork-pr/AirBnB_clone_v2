-- SQL script for setting up the mysql development server
-- This will be used in production of the airbnb clone project
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

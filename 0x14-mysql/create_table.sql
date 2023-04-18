-- creates sql table
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;

CREATE TABLE IF NOT EXISTS nexus6 (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);


GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';

INSERT INTO nexus6 VALUES (1, "Mwaura");

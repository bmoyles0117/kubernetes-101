CREATE TABLE messages (`id` INT NOT NULL AUTO_INCREMENT, `uuid` VARCHAR(36) NOT NULL DEFAULT '', `name` VARCHAR(100) NOT NULL DEFAULT '', `message` VARCHAR(1000) NOT NULL DEFAULT '', PRIMARY KEY (`id`), UNIQUE KEY (`uuid`));
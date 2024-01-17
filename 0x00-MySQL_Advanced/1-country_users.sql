-- Script that creates a table users
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    contry ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
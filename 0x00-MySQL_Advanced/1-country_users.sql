-- Task: Create a table named `users` with the specified attributes

-- create users table
CREATE TABLE IF NOT EXISTS users (
    -- id: integer, never null, auto increment, primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- email: string (255 characters), never null, unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- name: string (255 characters)
    name VARCHAR(255)
    -- country: enumarated list of countries, never null
    -- default value: first country in the list
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

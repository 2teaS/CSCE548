-- Movie Watchlist schema (MySQL 8+)
-- Create database (optional)
CREATE DATABASE IF NOT EXISTS csce548_watchlist;
USE csce548_watchlist;

-- Drop in dependency order
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS list_items;
DROP TABLE IF EXISTS lists;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30) NOT NULL UNIQUE,
  email VARCHAR(254) NOT NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE movies (
  movie_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  release_year SMALLINT NOT NULL,
  runtime_minutes SMALLINT NULL,
  genre VARCHAR(50) NULL,
  -- Basic validation
  CONSTRAINT chk_release_year CHECK (release_year BETWEEN 1888 AND 2100),
  CONSTRAINT chk_runtime CHECK (runtime_minutes IS NULL OR runtime_minutes BETWEEN 1 AND 600),
  UNIQUE KEY uq_movie_title_year (title, release_year)
);

CREATE TABLE lists (
  list_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  name VARCHAR(60) NOT NULL,
  description VARCHAR(255) NULL,
  is_public BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_lists_user FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  UNIQUE KEY uq_user_listname (user_id, name)
);

CREATE TABLE list_items (
  list_item_id INT AUTO_INCREMENT PRIMARY KEY,
  list_id INT NOT NULL,
  movie_id INT NOT NULL,
  status ENUM('PLANNED','WATCHING','WATCHED') NOT NULL DEFAULT 'PLANNED',
  added_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  watched_on DATE NULL,
  notes VARCHAR(255) NULL,
  CONSTRAINT fk_items_list FOREIGN KEY (list_id) REFERENCES lists(list_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_items_movie FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  -- prevent duplicates in same list
  UNIQUE KEY uq_list_movie (list_id, movie_id),
  -- watched_on should exist if WATCHED (MySQL CHECK supported in 8.0.16+, still keep app-level validation too)
  CONSTRAINT chk_watched_on CHECK (
    (status <> 'WATCHED' AND watched_on IS NULL)
    OR (status = 'WATCHED' AND watched_on IS NOT NULL)
  )
);

CREATE TABLE ratings (
  rating_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  movie_id INT NOT NULL,
  stars TINYINT NOT NULL,
  review TEXT NULL,
  rated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_ratings_user FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ratings_movie FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_stars CHECK (stars BETWEEN 1 AND 5),
  UNIQUE KEY uq_user_movie_rating (user_id, movie_id)
);


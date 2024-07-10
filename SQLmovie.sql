DROP DATABASE IF EXISTS movie_recommendation;

CREATE DATABASE movie_recommendation;

USE movie_recommendation;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100)
);

CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');
INSERT INTO movies (title) VALUES ('Inception'), ('Interstellar'), ('The Dark Knight');

DROP DATABASE IF EXISTS movie_recommendation;

CREATE DATABASE movie_recommendation;

USE movie_recommendation;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100)
);

CREATE TABLE ratings (
    user_id INT,
    movie_id INT,
    rating FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

INSERT INTO users (name) VALUES ('Luffy'), ('Zoro'), ('Sanji');
INSERT INTO movies (title) VALUES ('Harry Potter'), ('Godfather I'), ('The Dark Knight');

INSERT INTO ratings (user_id, movie_id, rating) VALUES
(1, 1, 5.0), (1, 2, 4.5),
(2, 1, 4.0), (2, 3, 5.0),
(3, 2, 4.0);



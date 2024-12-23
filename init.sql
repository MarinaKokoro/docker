
CREATE USER Marina WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE my_database TO Marina;

\connect my_database;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50)
);

INSERT INTO users (name, surname) VALUES
    ('Marina', 'Kokorovets'),
    ('Billi', 'Builder');

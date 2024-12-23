
CREATE USER Marina WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE my_database TO Marina;

\connect my_database;

CREATE TABLE emp (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    surname VARCHAR(50)
);

INSERT INTO emp (name, surname) VALUES
    ('Marina', 'Kokorovets'),
    ('Billi', 'Builder');

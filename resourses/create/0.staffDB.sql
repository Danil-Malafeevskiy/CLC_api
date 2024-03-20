CREATE TABLE IF NOT EXISTS "staff" (
    id serial PRIMARY KEY,
    position varchar(2047) NOT NULL,
    salary float NOT NULL
);
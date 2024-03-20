CREATE TABLE IF NOT EXISTS "child" (
    id serial PRIMARY KEY,
    name varchar(2047) NOT NULL,
    email varchar(2047) NOT NULL,
    phone_number varchar(2047) NOT NULL,
    address varchar(2047) NOT NULL,
    age integer NOT NULL,
    gender varchar(2047) NOT NULL,
    parent_id integer REFERENCES "parent" (id) NOT NULL
);
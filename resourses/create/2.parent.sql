CREATE TABLE IF NOT EXISTS "parent" (
    id serial PRIMARY KEY,
    name varchar(2047) NOT NULL,
    email varchar(2047) NOT NULL,
    phone_number varchar(2047) NOT NULL,
    address varchar(2047) NOT NULL
);

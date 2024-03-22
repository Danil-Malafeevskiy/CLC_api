CREATE TABLE IF NOT EXISTS "users" (
    id serial PRIMARY KEY,
    username varchar(2047) NOT NULL UNIQUE,
    password varchar(2047) NOT NULL,
    name varchar(2047) NOT NULL,
    email varchar(2047) NOT NULL,
    phone_number varchar(2047) NOT NULL,
    address varchar(2047) NOT NULL,
    is_superuser boolean NOT NULL
);
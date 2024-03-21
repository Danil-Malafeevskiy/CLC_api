CREATE TABLE IF NOT EXISTS "payment" (
    id serial PRIMARY KEY,
    method varchar(2047) NOT NULL,
    amount float NOT NULL,
    parent_id integer REFERENCES "parent" (id) NOT NULL,
    lesson_id integer REFERENCES "lesson" (id) NOT NULL
);
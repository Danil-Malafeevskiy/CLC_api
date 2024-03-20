CREATE TABLE IF NOT EXISTS "lesson" (
    id serial PRIMARY KEY,
    name varchar(2047) NOT NULL,
    date_lesson TIMESTAMP NOT NULL,
    duration float NOT NULL,
    price float NOT NULL,
    age integer NOT NULL,
    staff_id integer REFERENCES "staff" (id) NOT NULL
);


CREATE TABLE IF NOT EXISTS "feedback" (
    id serial PRIMARY KEY,
    text varchar(2047) NOT NULL,
    parent_id integer REFERENCES "parent" (id) NOT NULL,
    lesson_id integer REFERENCES "lesson" (id) NOT NULL
);
CREATE TABLE IF NOT EXISTS "record" (
    id serial PRIMARY KEY,
    parent_id integer REFERENCES "parent" (id) NOT NULL,
    child_id integer REFERENCES "child" (id) NOT NULL,
    lesson_id integer REFERENCES "lesson" (id) NOT NULL
);
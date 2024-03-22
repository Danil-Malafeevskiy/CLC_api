ALTER TABLE "child"
DROP COLUMN "parent_id";

ALTER TABLE "child"
ADD COLUMN parent_id integer REFERENCES "user" (id);


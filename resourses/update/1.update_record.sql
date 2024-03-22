ALTER TABLE "record"
DROP COLUMN "parent_id";

ALTER TABLE "record"
ADD COLUMN parent_id integer REFERENCES "user" (id);
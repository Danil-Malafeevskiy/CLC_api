ALTER TABLE "feedback"
DROP COLUMN "parent_id";

ALTER TABLE "feedback"
ADD COLUMN parent_id integer REFERENCES "users" (id);
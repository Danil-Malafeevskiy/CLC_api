ALTER TABLE "payment"
DROP COLUMN "parent_id";

ALTER TABLE "payment"
ADD COLUMN parent_id integer REFERENCES "user" (id);
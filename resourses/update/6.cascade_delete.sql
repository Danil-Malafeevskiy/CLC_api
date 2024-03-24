ALTER TABLE "lesson"
DROP COLUMN "staff_id";

ALTER TABLE "child"
DROP COLUMN "parent_id";

ALTER TABLE "record"
DROP COLUMN "parent_id";

ALTER TABLE "record"
DROP COLUMN "child_id";

ALTER TABLE "record"
DROP COLUMN "lesson_id";

ALTER TABLE "feedback"
DROP COLUMN "lesson_id";

ALTER TABLE "feedback"
DROP COLUMN "parent_id";

ALTER TABLE "payment"
DROP COLUMN "lesson_id";

ALTER TABLE "payment"
DROP COLUMN "parent_id";

ALTER TABLE "lesson"
ADD COLUMN staff_id integer REFERENCES "staff" (id) ON DELETE CASCADE;

ALTER TABLE "child"
ADD COLUMN parent_id integer REFERENCES "users" (id) ON DELETE CASCADE;

ALTER TABLE "record"
ADD COLUMN parent_id integer REFERENCES "users" (id) ON DELETE CASCADE;

ALTER TABLE "record"
ADD COLUMN child_id integer REFERENCES "child" (id) ON DELETE CASCADE;

ALTER TABLE "record"
ADD COLUMN lesson_id integer REFERENCES "lesson" (id) ON DELETE CASCADE;

ALTER TABLE "feedback"
ADD COLUMN parent_id integer REFERENCES "users" (id) ON DELETE CASCADE;

ALTER TABLE "feedback"
ADD COLUMN lesson_id integer REFERENCES "lesson" (id) ON DELETE CASCADE;

ALTER TABLE "payment"
ADD COLUMN parent_id integer REFERENCES "users" (id) ON DELETE CASCADE;

ALTER TABLE "payment"
ADD COLUMN lesson_id integer REFERENCES "lesson" (id) ON DELETE CASCADE;
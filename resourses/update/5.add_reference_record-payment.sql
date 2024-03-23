ALTER TABLE "payment"
ADD COLUMN record_id integer REFERENCES "record" (id);
-- Altering uniqueness constraints on first name and last name columns of table

ALTER TABLE user_comments DROP CONSTRAINT user_comments_first_name_key;
ALTER TABLE user_comments DROP CONSTRAINT user_comments_last_name_key;
CREATE TABLE IF NOT EXISTS accesses (
	access_id SERIAL PRIMARY KEY,
	alias TEXT NOT NULL UNIQUE
);
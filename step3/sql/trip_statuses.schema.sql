CREATE TABLE IF NOT EXISTS trip_statuses (
	trip_status_id SERIAL PRIMARY KEY,
	alias TEXT NOT NULL UNIQUE
);
CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	nickname TEXT NOT NULL UNIQUE,
	fullname TEXT NOT NULL,
	mobile TEXT UNIQUE,
	email TEXT UNIQUE,
	activestatus BOOL DEFAULT TRUE
)

mobile and email format are validated in front-end
CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    serialnumber TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    category_id INT,
    employee_id INT NOT NULL,
    FOREIGN KEY (category_id) references categories(id),
    FOREIGN KEY (employee_id) references employees(id)
)

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    nickname TEXT UNIQUE NOT NULL,
    fullname TEXT NOT NULL,
    mobile TEXT UNIQUE,
    email TEXT UNIQUE,
    activestatus BOOLEAN DEFAULT TRUE
)

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    category TEXT UNIQUE NOT NULL
)
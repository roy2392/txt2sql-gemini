CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    age INTEGER,
    height FLOAT,
    weight FLOAT
);

-- Insert sample data
INSERT INTO users (name, lastname, age, height, weight) VALUES
    ('John', 'Doe', 30, 175.5, 70.2),
    ('Jane', 'Smith', 25, 165.0, 55.5),
    ('Mike', 'Johnson', 35, 180.0, 85.0),
    ('Sarah', 'Williams', 28, 170.0, 63.5);

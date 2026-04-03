CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    coef INT
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    subject_id INT REFERENCES subjects(id),
    grade FLOAT
);

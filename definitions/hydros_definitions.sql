CREATE TABLE IF NOT EXISTS hydros_definitions (
    id INTEGER PRIMARY KEY,
    hydros_id TEXT,
    description TEXT
);

INSERT INTO hydros_definitions (hydros_id, description) VALUES
    ('0', 'No free-standing water'),
    ('1', '10%'),
    ('2', '20%'),
    ('3', '30%'),
    ('4', '40%'),
    ('5', '50%'),
    ('6', '60%'),
    ('7', '70%'),
    ('8', '80%'),
    ('9', '90%'),
    ('10', 'No land masses');

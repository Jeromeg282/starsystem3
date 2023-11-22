CREATE TABLE IF NOT EXISTS atmosphere_definitions (
    id INTEGER PRIMARY KEY,
    atmosphere_id TEXT,
    description TEXT
);

INSERT INTO atmosphere_definitions (atmosphere_id, description) VALUES
    ('0', 'No atmosphere'),
    ('1', 'Trace'),
    ('2', 'Very thin, tainted'),
    ('3', 'Very thin'),
    ('4', 'Thin, tainted'),
    ('5', 'Thin'),
    ('6', 'Standard'),
    ('7', 'Standard tainted'),
    ('8', 'Dense'),
    ('9', 'Dense tainted'),
    ('A', 'Exotic'),
    ('B', 'Corrosive'),
    ('C', 'Insidious'),
    ('D', 'Dense high'),
    ('E', 'Ellipsoid'),
    ('F', 'Thin, low');

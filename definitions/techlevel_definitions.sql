-- Create table
CREATE TABLE IF NOT EXISTS techlevel_definitions (
    id INTEGER PRIMARY KEY,
    techlevel_id TEXT,
    description TEXT
);

-- Insert data
INSERT INTO techlevel_definitions (techlevel_id, description) VALUES
    ('0', 'Stone age primitive'),
    ('1', 'Bronze age to middle ages'),
    ('2', 'Circa 1400 to 1700'),
    ('3', 'Circa 1700 to 1860'),
    ('4', 'Circa 1860 to 1900'),
    ('5', 'Circa 1900 to 1939'),
    ('6', 'Circa 1940 to 1969'),
    ('7', 'Circa 1970 to 1979'),
    ('8', 'Circa 1980 to 1989'),
    ('9', 'Circa 1990 to 2000'),
    ('A', 'Interstellar community'),
    ('B', 'Average imperial'),
    ('C', 'Technical maximum imperial'),
    ('F', 'Average imperial'),
    ('G', 'Occasional non-imperial');

-- Create table
CREATE TABLE IF NOT EXISTS gov_definitions (
    id INTEGER PRIMARY KEY,
    gov_id TEXT,
    description TEXT
);

-- Insert data
INSERT INTO gov_definitions (gov_id, description) VALUES
    ('0', 'No government structure'),
    ('1', 'Company/Corporation'),
    ('2', 'Participating democracy'),
    ('3', 'Self-perpetuating oligarchy'),
    ('4', 'Representative democracy'),
    ('5', 'Feudal technocracy'),
    ('6', 'Captive government'),
    ('7', 'Balkanization'),
    ('8', 'Civil service bureaucracy'),
    ('9', 'Impersonal bureaucracy'),
    ('A', 'Charismatic dictator'),
    ('B', 'Non-charismatic dictator'),
    ('C', 'Charismatic oligarchy'),
    ('D', 'Religious dictatorship');

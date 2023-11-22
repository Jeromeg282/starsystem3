-- Create table
CREATE TABLE IF NOT EXISTS mainworld_definitions (
    id INTEGER PRIMARY KEY,
    mainworld_id TEXT,
    description TEXT
);

-- Insert data
INSERT INTO mainworld_definitions (mainworld_id, description) VALUES
    ('0', 'No inhabitants'),
    ('1', 'Tens of inhabitants'),
    ('2', 'Hundreds of inhabitants'),
    ('3', 'Thousands of inhabitants'),
    ('4', 'Tens of thousands'),
    ('5', 'Hundreds of thousands'),
    ('6', 'Millions of inhabitants'),
    ('7', 'Tens of millions'),
    ('8', 'Hundreds of millions'),
    ('9', 'Billions of inhabitants'),
    ('10', 'Tens of billions');

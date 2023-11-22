CREATE TABLE IF NOT EXISTS starport_definitions (
    id INTEGER PRIMARY KEY,
    starport_id TEXT,
    description TEXT
);

INSERT INTO starport_definitions (starport_id, description) VALUES
    ('A', 'Excellent quality with refined fuel, overhaul, and shipyards'),
    ('B', 'Good quality with refined fuel and overhaul shipyards for non-starships'),
    ('C', 'Routine quality with unrefined fuel, some repair facilities'),
    ('D', 'Poor quality with unrefined fuel, no repair facilities'),
    ('E', 'Frontier installation: no facilities'),
    ('X', 'No starport, generally a red travel zone. Starports are established primarily to foster interstellar trade and commerce'),
    ('F', 'Good quality with unrefined fuel, minor repair facilities (spaceport)'),
    ('G', 'Poor quality with unrefined fuel, no repair facilities (spaceport)'),
    ('H', 'Primitive installation; no facilities (spaceport)'),
    ('Y', 'No spaceport. Spaceports are established primarily to foster in-system travel');

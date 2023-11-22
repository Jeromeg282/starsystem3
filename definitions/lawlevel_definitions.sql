CREATE TABLE IF NOT EXISTS lawlevel_definitions (
    id INTEGER PRIMARY KEY,
    lawlevel_id TEXT,
    description TEXT
);

INSERT INTO lawlevel_definitions (lawlevel_id, description) VALUES
    ('0', 'No prohibitions'),
    ('1', 'Body pistols undetectable by standard detectors, explosives (bombs, grenades), and poison gas prohibited'),
    ('2', 'Portable energy weapons (laser carbine, laser rifle) prohibited. Ship\'s gunnery not affected'),
    ('3', 'Weapons of a strict military nature (machine guns, automatic rifles) prohibited'),
    ('4', 'Light assault weapons (submachine guns) prohibited'),
    ('5', 'Personal concealable firearms (pistols, revolvers) prohibited'),
    ('6', 'Most firearms (all except short guns) prohibited, the carrying of any type of weapon openly is discouraged'),
    ('7', 'Shotguns are prohibited'),
    ('8', 'Long-bladed weapons (all but daggers) are controlled, and open possession is prohibited'),
    ('9', 'Possession of any weapon outside one\'s residence is prohibited'),
    ('10', 'Weapon possession is prohibited');

SET SQL_SAFE_UPDATES=0;
/*drop database People;*/
CREATE database People;
use People;

CREATE TABLE person (
	id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER
);

CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    breed VARCHAR(50),
    age INTEGER,
    dead INTEGER
);

CREATE TABLE person_pet (
    current_owner_id INTEGER,
    pet_id INTEGER,
    original_owner_id INTEGER
);

INSERT INTO person (id, first_name, last_name, age)
    VALUES (0, 'Dave', 'Wolfe', 25);

INSERT INTO pet (id, name, breed, age, dead)
    VALUES (0, 'Fluffy', 'Unicorn', 1000, 1);

/*1. insert myself*/
INSERT INTO person (id, first_name, last_name, age)
    VALUES (1, 'Avi', 'Drucker', 31);

/*1 cont.. insert my imaginary pet*/
INSERT INTO pet (id, name, breed, age, dead)
    VALUES (1, 'Yuna', 'Unicorn', 999, 0);

insert into person_pet values (0,0,0); # associate person Dave and pet Fluffy
insert into person_pet values (1,1,1); # associate person Avi and pet Yuna

# we now would like to bequeath the late Fluffy (or estate of) to Avi from David
update person_pet set current_owner_id = 1 where pet_id = 0; # pet id of 0 pets (Fluffy) should be assigned to person id of 1 persons (Avi)

# modify to take in Original Owner name instead of original owner ID
select first_name as 'Current Owner', name as 'Pet Name', pet.age as 'Pet Age', original_owner_id as 'Original Owner'
from person inner join 
person_pet on person.id = person_pet.current_owner_id
inner join pet on person_pet.pet_id = pet.id; # inner join person on person_pet.original_owner_id = person.id

SELECT * FROM person;
SELECT * FROM pet;
SELECT * FROM person_pet;
SET SQL_SAFE_UPDATES=1;
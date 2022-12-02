-- destruction des tables et des vues
DROP VIEW IF EXISTS LesAgesSportifs;
DROP VIEW IF EXISTS LesNbsEquipiers;

DROP TABLE IF EXISTS LesResultats;
DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS LesEpreuves;
DROP TABLE IF EXISTS LesSportifsEQ;

-- destruction des triggers
DROP TRIGGER IF EXISTS InsertCheck;
DROP TRIGGER IF EXISTS UpdateCheck;

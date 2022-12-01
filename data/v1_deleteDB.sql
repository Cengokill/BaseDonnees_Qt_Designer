-- TODO 1.3a : Détruire les tables manquantes et modifier celles ci-dessous
--DROP TABLE IF EXISTS LesEpreuves;
--DROP TABLE IF EXISTS LesSportifsEQ;

-- TODO 3.3 : pensez à détruire vos triggers !
DROP TRIGGER IF EXISTS InsertCheck1;
DROP TRIGGER IF EXISTS InsertCheck2;
DROP TRIGGER IF EXISTS UpdateCheck1;
DROP TRIGGER IF EXISTS UpdateCheck1;

DROP VIEW IF EXISTS LesAgesSportifs;
DROP VIEW IF EXISTS LesNbsEquipiers;

DROP TABLE IF EXISTS LesResultats;
DROP TABLE IF EXISTS LesInscriptions;
DROP TABLE IF EXISTS LesEpreuves;
DROP TABLE IF EXISTS LesSportifsEQ;

--Triggers crées (se créent sans erreur dans DB browser, mais pas ici)
CREATE TRIGGER InsertCheck
   BEFORE INSERT ON LesInscriptions
   WHEN (NEW.numIn NOT IN(SELECT numSp FROM LesSportifsEQ) OR NEW.numIn NOT IN(SELECT numEq FROM LesSportifsEQ) OR NEW.numEp NOT IN(SELECT numEp FROM LesEpreuves))
   BEGIN
        SELECT RAISE (ABORT, 'numIn/numEp non répertorié' );
   END;

CREATE TRIGGER UpdateCheck
   BEFORE UPDATE ON LesInscriptions
   WHEN (NEW.numIn NOT IN(SELECT numSp FROM LesSportifsEQ) OR NEW.numIn NOT IN(SELECT numEq FROM LesSportifsEQ) OR NEW.numEp NOT IN(SELECT numEp FROM LesEpreuves))
   BEGIN
        SELECT RAISE (ABORT, 'numIn/numEp non répertorié' );
   END;



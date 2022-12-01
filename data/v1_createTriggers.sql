-- TODO 3.3 Créer un trigger pertinent
--CREATE TRIGGER IF NOT EXISTS InsertCheck1
   -- BEFORE INSERT ON LesInscriptions
   -- WHEN EXISTS (NEW.numIn NOT IN(SELECT numSp FROM LesSportifsEQ) OR NEW.numIn NOT IN(SELECT numEq FROM LesSportifsEQ))
  --  BEGIN
   --     SELECT RAISE (ABORT, 'yuufey_')
 --   END;


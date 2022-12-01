-- TODO 1.3a : Créer les tables manquantes et modifier celles ci-dessous
-- TODO 1.4a : ajouter la définition de la vue LesAgesSportifs
-- TODO 1.5a : ajouter la définition de la vue LesNbsEquipiers
-- TODO 3.3 : ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)

CREATE TABLE LesSportifsEQ(
	numSp NUMBER(4),
	nomSp VARCHAR2(20)NOT NULL,
	prenomSp VARCHAR2(20)NOT NULL,
	pays VARCHAR2(20)NOT NULL, --TRIGGER EQUIPE > meme numEq=meme pays
	categorieSp VARCHAR2(10),
	dateNaisSp DATE NOT NULL,
	numEq NUMBER(4),
	CONSTRAINT SP_PK PRIMARY KEY (numSp, numEq),
	CONSTRAINT SP_CK1 CHECK(numSp > 0),
	CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
	CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE LesEpreuves(
    numEp NUMBER(3),
    nomEp VARCHAR2(20) NOT NULL,
    formeEp VARCHAR2(13),
    nomDi VARCHAR2(25) NOT NULL,
    categorieEp VARCHAR2(10),
    nbSportifsEp NUMBER(2),
    dateEp DATE,
    CONSTRAINT EP_PK PRIMARY KEY (numEp),
    CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
    CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
    CONSTRAINT EP_CK3 CHECK (numEp > 0),
    CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

CREATE TABLE LesInscriptions(
    numIn NUMBER(4),
	numEp NUMBER(3), --TRIGGER >Si Ep invididuelle, alors numIn=numSP, sinon numIN=numEq
	CONSTRAINT EP_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
    --BESOIN DE TRIGGER ICI pour numIn
	CONSTRAINT EP_IN_PK PRIMARY KEY (numEP, numIn)
);

CREATE TABLE LesResultats(
	numEp NUMBER(3),
	gold NUMBER(4), --TRIGGER> numEP et numIn concordent > forment une clé primaire dans LesInscriptions
	silver NUMBER(4),
	bronze NUMBER(4),
	CONSTRAINT EP_FK FOREIGN KEY (numEp) REFERENCES LesEpreuves(numEp),
	CONSTRAINT GOLD_FK FOREIGN KEY (gold) REFERENCES LesInscriptions(numIn),
	CONSTRAINT SILVER_FK FOREIGN KEY (silver) REFERENCES LesInscriptions(numIn),
	CONSTRAINT BRONZE_FK FOREIGN KEY (bronze) REFERENCES LesInscriptions(numIn)
);

CREATE VIEW LesAgesSportifs AS
	SELECT (DATE() - dateNaisSp) AS age, numSp
	FROM LesSportifsEQ
	GROUP BY numSp;

CREATE VIEW LesNbsEquipiers AS
	SELECT COUNT(numSp) AS nbEquipiers, numEq
	FROM LesSportifsEQ
	GROUP BY numEq;


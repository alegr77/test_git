CREATE TABLE STATO(
    ID NUMBER PRIMARY KEY,
    Nome VARCHAR2(30 CHAR),
    Valuta VARCHAR2(1O CHAR)
);
CREATE TABLE CITTA(
    ID NUMBER PRIMARY KEY,
    Nome VARCHAR(40 CHAR),
    ID_STATO NUMBER,
    FOREIGN KEY(ID_STATO)
    REFERENCES STATO(ID)
    	ON DELETE CASCADE
);
CREATE TABLE HOTEL(
    ID NUMBER PRIMARY KEY,
    Nome VARCHAR(40 CHAR),    
    Indirizzo VARCHAR(40 CHAR),
    ID_CITTA NUMBER,
    FOREIGN KEY(ID_CITTA)
    REFERENCES CITTA(ID)
    	ON DELETE CASCADE
);
CREATE TABLE SERVIZIO_EXTRA(
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(40 CHAR)
);
CREATE TABLE TIPOLOGIA_STANZA(
    ID NUMBER PRIMARY KEY,
    Posti_letto NUMBER NOT NULL,
    Mult_Prezzo NUMBER default 1,
    ID_SERVIZIO_EXTRA NUMBER
    FOREIGN KEY (ID_SERVIZIO_EXTRA)
    REFERENCES SERVIZIO_EXTRA(ID)
    	ON DELETE CASCADE
);
CREATE TABLE LISTINO(
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Data_Inizio DATE TIME,
    Data_Fine DATE TIME,
    Prezzo NUMBER
    check(DATA_INIZIO<=DATA_FINE)
);
CREATE TABLE CLIENTE(
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR2(40CHAR),
    Email VARCHAR2(50CHAR),
    Telefono VARCHAR(15CHAR)
    CONSTRAINT email_unic UNIQUE(Email),
    CONSTRAINT tel_unic UNIQUE(Telefono),
    CHECK (Email NOT NULL OR Telefono NOT NULL)
);
CREATE TABLE SERVIZIO_HOTEL(
	ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR2(40CHAR),
    Costo NUMBER DEFAULT 1,
    ID_HOTEL NUMBER,
    FOREIGN KEY (ID_HOTEL)
    REFERENCES HOTEL(ID)
    	ON DELETE CASCADE
);
CREATE TABLE STANZA(
	ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR2(25CHAR) NOT NULL,
    Piano VARCHAR2(25CHAR) NOT NULL,
    ID_HOTEL NUMBER,
    FOREIGN KEY (ID_HOTEL)
    REFERENCES HOTEL(ID)
    	ON DELETE CASCADE
    ID_TIPOLOGIA_STANZA NUMBER,
    FOREIGN KEY (ID_TIPOLOGIA_STANZA)
    REFERENCES TIPOLOGIA_STANZA(ID)
    	ON DELETE CASCADE
);
CREATE TABLE PRENOTAZIONE(
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Data_prenotazione DATE TIME,
    N_Adulti NUMBER NOT NULL,
    N_Bambini NUMBER DEFAULT 0,
    Checkin DATE TIME,
    Checkout DATE TIME,
    ID_SERVIZIO_HOTEL NUMBER,
    ID_CLIENTE NUMBER,
    ID_LISTINO NUMBER,
    ID_STANZA NUMBER,
    FOREIGN KEY (ID_SERVIZIO_HOTEL)
    	REFERENCES SERVIZIO_HOTEL(ID)
    	ON DELETE CASCADE,
    FOREIGN KEY (ID_CLIENTE)
   	    REFERENCES CLIENTE(ID)
    	ON DELETE CASCADE
    FOREIGN KEY (ID_LISTINO)
    	REFERENCES LISTINO(ID)
    	ON DELETE CASCADE
    FOREIGN KEY (ID_STANZA)
    	REFERENCES STANZA(ID)
    	ON DELETE CASCADE
);
CREATE TABLE SERVIZIO_PER_TIPOLOGIA_STANZA(
    ID TIPOLOGIA_STANZA NUMBER,
    ID SERVIZIO_EXTRA NUMBER,
    FOREIGN KEY(ID_TIPOLOGIA_STANZA)
        REFERENCES TIPOLOGIA_STANZA(ID)
        ON DELETE CASCADE,
    FOREIGN KEY(ID_SERVIZIO_EXTRA)
        REFERENCES SERVIZIO_EXTRA(ID)
        ON DELETE CASCADE
);
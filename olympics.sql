#visualizza tutti le discipline che hanno come sport "Aquatics"

select s.sport
     , d.discipline
    from olym.OLYM_DISCIPLINES D
	JOIN OLYM.OLYM_SPORTS S
	ON D.SPORT_ID = S.ID
WHERE S.SPORT = 'Aquatics'

#visualizzare ori, argenti e bronzi vinti per ogni atleta(ANCHE CON PIVOT)
SELECT *
    FROM(SELECT A.ATHLETE_NAME
              , M.MEDAL
     	 FROM OLYM.OLYM_MEDALS M
    	 JOIN OLYM.OLYM_ATHLETES A
    		ON M.ID = A.ID
        )
PIVOT (
    COUNT(MEDAL)
    FOR MEDAL IN('Gold', 'Silver', 'Bronze')
);

#visualizzare ori, argenti e bronzi vinti per ogni STATO e per ogni edizione (ANCHE CON PIVOT)
SELECT *
    FROM(SELECT M.MEDAL
    		  , N.NATION
    		  , G.CITY || ',' || G.YEAR OLYMPICS_EDITION
     	 FROM OLYM.OLYM_MEDALS M
    	 JOIN OLYM.OLYM_ATHLETE_GAMES AG
    		ON M.ATHLETE_GAME_ID = AG.ID
         JOIN OLYM.OLYM_NATIONS N
            ON AG.NATION_ID = N.ID
    	 JOIN OLYM.OLYM_GAMES G
    		ON AG.GAME_ID = G.ID
    	 WHERE G.CITY = 'Atlanta'
             AND G.YEAR = 1996   
    )

PIVOT (
    COUNT(1)
    FOR MEDAL IN('Gold', 'Silver', 'Bronze')
);

#Visualizzare tutte le nazioni che hanno partecipato ai giochi a Sydney 2000
SELECT N.NATION, 
       ROW_NUMBER() OVER (ORDER BY N.NATION) AS COUNT_NATION
FROM OLYM.OLYM_ATHLETE_GAMES AG
JOIN OLYM.OLYM_NATIONS N 
    ON AG.NATION_ID = N.ID
JOIN OLYM.OLYM_GAMES G 
    ON AG.GAME_ID = G.ID
WHERE G.CITY = 'Sydney'  
  AND G.YEAR = 2000
ORDER BY COUNT_NATION;


#Vedere tutti gli eventi a cui ha partecipato un determinato atleta
   (tutto ció che sappiamo di quel evento)

SELECT A.ATHLETE_NAME 
     , G.*
FROM OLYM.OLYM_ATHLETE_GAMES AG
JOIN OLYM.OLYM_ATHLETES A 
    ON AG.ATHLETE_ID = A.ID
JOIN OLYM.OLYM_GAMES G 
    ON AG.GAME_ID = G.ID
WHERE A.ATHLETE_NAME LIKE '%CHECHI%'
ORDER BY G.YEAR;

5) Vedere il numero di olimpiadi vinte da ogni stato (conta il numero di ori)
SELECT NATION, 
       COUNT(*) AS OLYMPIC_WINS
FROM (
    SELECT G.CITY, 
           G.YEAR,
           N.NATION,
           SUM(CASE WHEN M.MEDAL = 'Gold' THEN 1 ELSE 0 END) AS GOLD_COUNT
    FROM OLYM.OLYM_MEDALS M
    JOIN OLYM.OLYM_ATHLETE_GAMES AG ON M.ATHLETE_GAME_ID = AG.ID
    JOIN OLYM.OLYM_NATIONS N ON AG.NATION_ID = N.ID
    JOIN OLYM.OLYM_GAMES G ON AG.GAME_ID = G.ID
    GROUP BY G.CITY, G.YEAR, N.NATION
) MEDAL_COUNTS
WHERE (CITY, YEAR, GOLD_COUNT) IN (
    SELECT CITY, YEAR, MAX(GOLD_COUNT)
    FROM (
        SELECT G.CITY, 
               G.YEAR,
               N.NATION,
               SUM(CASE WHEN M.MEDAL = 'Gold' THEN 1 ELSE 0 END) AS GOLD_COUNT
        FROM OLYM.OLYM_MEDALS M
        JOIN OLYM.OLYM_ATHLETE_GAMES AG ON M.ATHLETE_GAME_ID = AG.ID
        JOIN OLYM.OLYM_NATIONS N ON AG.NATION_ID = N.ID
        JOIN OLYM.OLYM_GAMES G ON AG.GAME_ID = G.ID
        GROUP BY G.CITY, G.YEAR, N.NATION
    )
    GROUP BY CITY, YEAR
)
GROUP BY NATION
ORDER BY OLYMPIC_WINS DESC;

6) Media delle medaglie vinte per paese (considerare solo le olimpiadi a cui
   hanno effettivamente partecipato)

7) Vedere la percentuale di medaglie vinte per atleta(?)
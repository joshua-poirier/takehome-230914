-- Write only the SQL statement that solves the problem and nothing else
;WITH CTE_fsib AS (
    SELECT      companyName,
                sharePrice * sharesOutstanding AS marketCapitalization
    FROM        fsib
)
SELECT      companyName,
            marketCapitalization
FROM        fsia
UNION ALL
SELECT      companyName,
            marketCapitalization
FROM        CTE_fsib
ORDER BY    marketCapitalization DESC

# Take Home Assessment

Take home coding assessment associated with a job application, September 14, 2023.

## Solutions

### Demo
A quick demo problem I threw together to help setup my virtual environment to solve the
questions.

### Question 1
Text answer (no solution here).

### Question 2
You have a number of items to be packaged into large packages and small packages. You
have a given number of large packages available, and a given number of small packages
available. If the available packages cannot hold all of the items, return `-1`.

Large packages can hold 5 items (no more, no less), and small packages can hold 1 item
(no more, no less). What is the minimum number of packages (large + small) needed to
hold the given items?

If you have 16 items to be packages with 2 large packages and 10 small packages
available - the minimum number of packages will be `8` (2 large + 6 small).

### Question 3
Two stock market indexes are stored in two separate tables, `fsia` and `fsib`. The
`fsia` table contains the company name its market capitalization. The `fsib` table
contains the company name, the share price, and the number of shares outstanding.

Market capitalization can be calculated as:
`marketCapitalization = sharePrice * sharesOutstanding`

Construct a query to return the company name and market capitalization of each company,
ordered by market capitalization - from largest to smallest. The following provides
environment suggestions and can assist you in creating a database.

Suggested testing environment:  
For MS SQL: https://sqliteonline.com/ with language set as MS SQL  
For MySQL: https://www.db-fiddle.com/ with MySQL version set to 8  
For SQLite: http://sqlite.online/  

Example case create statement:
```sql
CREATE TABLE fsia (
  companyName VARCHAR(30) NOT NULL PRIMARY KEY,
  marketCapitalization FLOAT NOT NULL
);

CREATE TABLE fsib (
  companyName VARCHAR(30) NOT NULL PRIMARY KEY,
  sharePrice FLOAT NOT NULL,
  sharesOutstanding INTEGER NOT NULL
);

INSERT INTO fsia(companyName, marketCapitalization) VALUES('Baggage Enterprise.', 12500);
INSERT INTO fsia(companyName, marketCapitalization) VALUES('Fun Book Corporation', 10000);

INSERT INTO fsib(companyName, sharePrice, sharesOutstanding) VALUES('Macaroni Inc.', 8, 1000);
INSERT INTO fsib(companyName, sharePrice, sharesOutstanding) VALUES('Solitude Ltd.', 12.5, 600);
INSERT INTO fsib(companyName, sharePrice, sharesOutstanding) VALUES('Universal Exports LLC', 1.2, 2300);
```

-- Expected output:
-- companyName           marketCapitalization
-- ---------------------------------------------
-- Baggage Enterprise    12500 
-- Fun Book Corporation  10000 
-- Macaroni Inc.         8000 
-- Solitude Ltd.         7500 
-- Universal Exports LLC 2760  

-- Explanation:
-- In this example.
-- Baggage Enterprise is the largest company, it therefore appears first in the results.
-- The companies descend in order by marketCapitalization until Universal Exports LLC which is the smallest.

### Question 4
A SQL problem.

### Question 5
Fill in the blanks (no solution here).

### Question 6
Fill in the blanks (no solution here).

### Question 7
Number picker.

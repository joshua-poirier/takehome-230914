# Take Home Assessment

Take home coding assessment associated with a job application, September 14, 2023.

For the SQL coding questions, the following are suggested testing environments:
For MS SQL: https://sqliteonline.com/ with language set as MS SQL  
For MySQL: https://www.db-fiddle.com/ with MySQL version set to 8  
For SQLite: http://sqlite.online/  

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

Expected outut:
| companyName           | marketCapitalization |
| --------------------- | -------------------- |
| Baggage Enterprice    | 12500                |
| Fun Book Corporation  | 10000                |
| Macaroni Inc.         | 8000                 |
| Solitude Ltd.         | 7500                 |
| Universal Exports LLC | 2760                 |

Explanation:
In this example Baggage Enterprise is the largest company, it therefore appears first in
the results. The companies descend in order by marketCapitalization until Universal
Exports LLC which is the smallest.

### Question 4
Car companies are displaying their cars at an auto show. Each company displays at least
one car. The auto show also holds various events on which difference cars are compared
according to the selected features.

Given below is the data definition of tables that hold data for companies, their cars,
events, and participation:

```sql
CREATE TABLE companies (
  id INTEGER PRIMARY KEY,
  name VARCHAR(40) NOT NULL
);

CREATE TABLE cars (
  id INTEGER PRIMARY KEY,
  name VARCHAR(40) NOT NULL,
  companyId INTEGER NOT NULL,
  FOREIGN KEY (companyId) REFERENCES companies(id)
);

CREATE TABLE events (
  id INTEGER PRIMARY KEY,
  name VARCHAR(40) NOT NULL
);

CREATE TABLE eventParticipants (
  carId INTEGER NOT NULL,
  eventId INTEGER NOT NULL,
  PRIMARY KEY(carId, eventId),
  FOREIGN KEY (carId) REFERENCES cars(id),
  FOREIGN KEY (eventId) REFERENCES events(id)
);

INSERT INTO companies(id, name) VALUES(1, 'Ford');
INSERT INTO companies(id, name) VALUES(2, 'General Motors');

INSERT INTO cars(id, name, companyId) VALUES(1, 'Aspire-Sedan', 1);
INSERT INTO cars(id, name, companyId) VALUES(2, 'EcoSport-SUV', 1);
INSERT INTO cars(id, name, companyId) VALUES(3, 'Mustang-Convertible', 1);
INSERT INTO cars(id, name, companyId) VALUES(4, 'Chevrolet-Sedan', 2);
INSERT INTO cars(id, name, companyId) VALUES(5, 'GMC-Terrain', 2);

INSERT INTO events(id, name) VALUES(1, 'Sedan Event');
INSERT INTO events(id, name) VALUES(2, 'SUV Event');
INSERT INTO events(id, name) VALUES(3, 'Convertible Event');

INSERT INTO eventParticipants(carId, eventId) VALUES(1, 1);
INSERT INTO eventParticipants(carId, eventId) VALUES(4, 1);
```

Write a query that returns:
- The names of car companies
- Total number of their cars that will **not** be displayed at any event.

Car companies that have all their cars displayed at some event should not be returned.

Ford has fielded 3 cars, and General Motors has fielded 2 cars. Only one car,
'Aspire-Sedan' from Ford, and one car 'Chevrolet-Sedan' from General Motors have been
assigned for the events. So, now Ford has two cars and General Motors has one car that
didn't participated in any events. Hence, the below results.
 
Expected output (rows in any order):
| name           | count |
| -------------- | ----- |
| Ford           |  2    |
| General Motors |  1    |

### Question 5
Fill in the blanks (no solution here).

### Question 6
Fill in the blanks - demonstrating an understanding of recursive functions. Quick
implementation of the recursive function here.

### Question 7
It takes 2040 digits to give ID's to all employees. How many employee's are there?

For example, it takes 15 digits to cover 12 employees
([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).

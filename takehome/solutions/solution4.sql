SELECT      companies.name
	        ,COUNT(1)
FROM        cars
INNER JOIN  companies
ON          cars.companyid = companies.id
WHERE       cars.id NOT IN (
                SELECT      carid
                FROM        eventParticipants
            )
GROUP BY    companies.name

SELECT name FROM Employee
WHERE id IN (SELECT managerId from Employee GROUP BY managerId
HAVING count(managerId)>4);
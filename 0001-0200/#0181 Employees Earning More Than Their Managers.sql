SELECT
    z.Name AS Employee
FROM
    (
        SELECT
            x.Name,
            x.Salary,
            y.Salary AS ManagerSalary
        FROM
            Employee x
            JOIN Employee y ON x.ManagerId = y.Id
    ) AS z
WHERE
    z.Salary > z.ManagerSalary;
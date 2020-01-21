DELETE t1
FROM
    Person t1,
    Person t2
WHERE
    t1.id > t2.id
    AND t1.Email = t2.Email;
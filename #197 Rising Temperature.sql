SELECT
    x.Id
FROM
    Weather,
    Weather x
WHERE
    DATEDIFF(Weather.RecordDate, x.RecordDate) = 1
    AND Weather.Temperature > x.Temperature;
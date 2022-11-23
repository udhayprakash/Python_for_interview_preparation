/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/
select
    ctry.country_name, ct.city_name, COUNT(cmr.customer_name)
FROM country ctry
    INNER JOIN  city ct on ct.country_id = ctry.id
    INNER JOIN customer cmr on cmr.city_id = ct.id
GROUP BY ctry.country_name, ct.city_name
    HAVING COUNT(cmr.customer_name) > (
        SELECT  COUNT(cmr1.customer_name)/ COUNT( distinct ct1.city_name) as ct_avg
        FROM city ct1
        INNER JOIN customer cmr1 ON cmr1.city_id = ct1.id
    )
ORDER BY ctry.country_name ASC;
/*


        SELECT
        ct1.city_name, group_concat(cmr1.id)
        FROM city ct1
        INNER JOIN customer cmr1 ON cmr1.city_id = ct1.id
        group by ct1.city_name


/*
select
    ctry.country_name, ct.city_name, COUNT(*) as cstmr_count
FROM city ct
    INNER JOIN  country ctry on ct.country_id = ctry.id
    INNER JOIN customer cmr on cmr.city_id = ct.id
GROUP BY ctry.id, ctry.country_name, ct.id, ct.city_name
HAVING  count(*) > ( select count(*)/count(distinct cmr1.id) from customer cmr1)
ORDER BY ctry.country_name ASC;

select count(*), count(distinct cmr1.customer_name) from customer cmr1
*/

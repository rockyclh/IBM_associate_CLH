SELECT owner_id, owner_name, COUNT(DISTINCT category_id) as different_category_count
-- with two left join, we can have a table that contain all needed information
FROM article a 
    LEFT JOIN category_article_mapping c ON a.article_id = c.article_id
    LEFT JOIN owner o ON a.owner_id = o.owner_id
GROUP BY owner_id
ORDER BY different_category_count DESC

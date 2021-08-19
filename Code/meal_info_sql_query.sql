-- To select all rows from table
SELECT * FROM meal_info;

-- delete command
DELETE meal_info
where meal_id = 1109;
Select *from mmeal_info;

-- update command
UPDATE mytable 
SET category = "Extras" where meal_id = 2539;
Select *from mytable;

-- To limit our query
SELECT *from mytable limit 3;

-- To insert data in our table
INSERT into meal_info values(952, "Starters","Russian");
Select *from mytable;

-- To sort in descending order
SELECT *FROM meal_info
ORDER BY cuisine DESC;

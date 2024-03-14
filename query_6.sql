SELECT first_name , last_name
FROM Students s
WHERE group_id = (SELECT group_id FROM Groups WHERE group_name = "Group A")
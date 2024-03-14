SELECT s.first_name, s.last_name, g.grade, g.date
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE s.group_id = (SELECT group_id FROM Groups WHERE group_name = 'Group B')  -- Wybrana grupa
AND sub.subject_name = 'Physics'  -- Wybrany przedmiot
ORDER BY g.date DESC;

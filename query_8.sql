SELECT AVG(g.grade) AS average_grade
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE sub.lecturer_id = (SELECT lecturer_id FROM Lecturers WHERE last_name = 'Ramos')  -- Wybrany wykładowca
AND sub.subject_name = 'Chemistry';  -- Wybrany przedmiot

SELECT s.group_id, AVG(g.grade) AS average_grade
FROM Grades g
JOIN Students s ON g.student_id = s.student_id
WHERE g.subject_id = (SELECT subject_id FROM Subjects WHERE subject_name = 'Mathematics')  -- Wybrany przedmiot
GROUP BY s.group_id;

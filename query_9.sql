SELECT sub.subject_name
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE g.student_id = (SELECT student_id FROM Students WHERE last_name = 'Allen');  -- Wybrany uczeń

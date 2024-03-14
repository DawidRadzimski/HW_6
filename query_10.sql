SELECT sub.subject_name
FROM Subjects sub
WHERE sub.lecturer_id = (SELECT lecturer_id FROM Lecturers WHERE last_name = 'Ramos')  -- Wybrany wykładowca
AND sub.subject_id IN (SELECT subject_id FROM Grades WHERE student_id = (SELECT student_id FROM Students WHERE last_name = 'Allen'));  -- Wybrany uczeń

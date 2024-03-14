SELECT subject_name
FROM Subjects
WHERE lecturer_id = (SELECT lecturer_id FROM Lecturers WHERE last_name = 'Padilla');  -- Wybrany wykładowca

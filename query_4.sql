SELECT s.group_id, AVG(g.grade) AS average_grade
FROM Grades g
JOIN Students s ON g.student_id = s.student_id
GROUP BY s.group_id;

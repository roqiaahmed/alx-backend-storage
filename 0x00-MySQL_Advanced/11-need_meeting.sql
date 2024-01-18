-- need_meeting view
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW IF NOT EXISTS need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting = NULL OR last_meeting < ADDDATE(NOW(), INTERVAL -1 MONTH));
-- stored procedure ComputeAverageScoreForUser
DELIMITER $$
CREATE procedure ComputeAverageScoreForUser( p_user_id INT )
BEGIN
    DECLARE v_avg_score FLOAT;
    SELECT AVG(score) INTO v_avg_score FROM corrections WHERE user_id = p_user_id;
    UPDATE users SET average_score = v_avg_score WHERE id = p_user_id;
END$$
DELIMITER ;
-- Create a procedure that computes the average score of a given student
DROP PROCEDURE IF EXISTS `ComputeAverageScoreForUser`;

DELIMITER $$
CREATE PROCEDURE `ComputeAverageScoreForUser`(IN user_id INT)
COMMENT 'Compute the average score for a given student'
BEGIN
	DECLARE user_average FLOAT DEFAULT NULL;

	SELECT AVG(score)
	INTO user_average
	FROM `corrections`
	WHERE `corrections`.user_id = user_id;

	UPDATE `users`
	SET average_score = user_average
	WHERE id = user_id;
END
$$
DELIMITER ;

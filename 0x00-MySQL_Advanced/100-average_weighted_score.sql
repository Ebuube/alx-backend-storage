-- Create a stored procedure that computes the avearege weighted score for a student

DROP PROCEDURE IF EXISTS `ComputeAverageWeightedScoreForUser`;

DELIMITER $$
CREATE PROCEDURE `ComputeAverageWeightedScoreForUser`(IN user_id INT)
COMMENT 'Compute and store the average weighted score for a student'
BEGIN
	/* Assuming that user_id is linked to an existing users */
	/* The result is stored in `users`.`average_score` */
	DECLARE weight_sum FLOAT DEFAULT NULL;
	DECLARE total_score FLOAT DEFAULT NULL;
	DECLARE weighted_avg FLOAT DEFAULT NULL;

	-- Get the total sum of the weights since the weights don't add up to 1
	SELECT SUM(weight) INTO weight_sum
	FROM users
	JOIN corrections ON corrections.user_id = users.id
	JOIN projects ON projects.id = corrections.project_id
	WHERE users.id = user_id;

	-- SELECT weight_sum;	/* test */

	-- get sum of projects.weight * corrections.score
	SELECT SUM(weight * score) INTO total_score
	FROM users
	JOIN corrections ON corrections.user_id = users.id
	JOIN projects ON projects.id = corrections.project_id
	WHERE users.id = user_id;

	-- SELECT total_score; /* test */

	SET weighted_avg = total_score / weight_sum;

	-- SELECT weighted_avg; 	/* test */

	-- Update user's average score
	UPDATE users
	SET average_score = weighted_avg
	WHERE id = user_id;
END
$$
DELIMITER ;

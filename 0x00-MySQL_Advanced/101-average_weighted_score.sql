-- Create a stored procedure that computes and stores the average weighted score
-- for all students

DROP PROCEDURE IF EXISTS `CalcAverageWeightedScoreForUser`;
DROP PROCEDURE IF EXISTS `ComputeAverageWeightedScoreForUsers`;

DELIMITER $$
CREATE PROCEDURE `CalcAverageWeightedScoreForUser`(IN user_id INT)
COMMENT 'Compute and store the average weighted score for a student'
PROC_EXIT: BEGIN
	/* If a user does not exist, it ends execution */
	/* The result is stored in `users`.`average_score` */
	DECLARE weight_sum FLOAT DEFAULT NULL;
	DECLARE total_score FLOAT DEFAULT NULL;
	DECLARE weighted_avg FLOAT DEFAULT NULL;
	DECLARE user_name VARCHAR(255) DEFAULT NULL;

	-- Ensure that a user exists else quit
	SELECT name INTO user_name
	FROM users
	WHERE users.id = user_id;

	IF user_name IS NULL THEN
		LEAVE PROC_EXIT;
	END IF;
	

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


CREATE PROCEDURE `ComputeAverageWeightedScoreForUsers`()
COMMENT 'Compute the average weighted score for all students'
BEGIN
	DECLARE user_id INT DEFAULT NULL;
	DECLARE done INT DEFAULT FALSE;

	DECLARE cur_all_users
	CURSOR FOR
	SELECT id FROM users;

	-- continue handler
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	-- Start fetching data
	OPEN cur_all_users;

	calc_avg: LOOP
		IF done THEN
			LEAVE calc_avg;
		END IF;

		FETCH cur_all_users INTO user_id;
		CALL CalcAverageWeightedScoreForUser(user_id);		
	END LOOP;

	CLOSE cur_all_users;
END
$$
DELIMITER ;

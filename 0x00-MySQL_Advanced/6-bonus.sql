-- Create aprocedure 'AddBonus' that adds a new correction for a student
DROP PROCEDURE IF EXISTS `AddBonus`;

DELIMITER $$
CREATE PROCEDURE `AddBonus`(IN user_id INT, IN project_name VARCHAR(255),
	IN score INT)
COMMENT 'Add new correction for a user. Creates project if not exists'
BEGIN
	DECLARE main_project_id INT DEFAULT NULL;

	/* Get project id */
	SELECT id INTO main_project_id
	FROM `projects`
	WHERE name = project_name;

	/* If project is not available, create it */
	IF main_project_id IS NULL THEN
		INSERT INTO `projects` (name) VALUES (project_name);
		SET main_project_id = LAST_INSERT_ID();
	END IF;

	INSERT INTO `corrections` (user_id, project_id, score)
	VALUES (user_id, main_project_id, score);
END
$$
DELIMITER ;

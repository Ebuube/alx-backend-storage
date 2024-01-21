-- Create index `idx_name_first` on table `names` and the first letter of name

/*
-- Verify index exists before re
SELECT COUNT(*) INTO @index_exists
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = DATABASE() -- Ensure current database
	AND TABLE_NAME = 'names'
	AND INDEX_NAME = 'idx_name_first';

IF @index_exists = 1 THEN
	DROP INDEX `idx_name_first` ON `names`;
END IF;
*/

CREATE INDEX `idx_name_first` ON names (name(1));

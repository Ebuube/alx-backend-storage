-- List all bands with 'Glam rock' as their main style, ranked by their longevity
-- Upper limit of age for longevity is 2022
SELECT band_name,
	IF(split IS NULL OR split > 2022, (2022 - formed), (split - formed))
	AS lifespan
	FROM metal_bands
	WHERE FIND_IN_SET('Glam rock', IF(style = NULL, '', style))
	ORDER BY lifespan desc;

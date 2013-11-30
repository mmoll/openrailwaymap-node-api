<?php
	/*
	OpenRailwayMap Copyright (C) 2012 Alexander Matheisen
	This program comes with ABSOLUTELY NO WARRANTY.
	This is free software, and you are welcome to redistribute it under certain conditions.
	See http://wiki.openstreetmap.org/wiki/OpenRailwayMap for details.
	*/


	require_once("functions.php");

	if (isset($_GET['lang']) && array_key_exists($_GET['lang'], $langs))
		$lang = $_GET['lang'];
	else
		$lang = getUserLang();
	includeLocale($lang);

	$zoom = isset($_GET['zoom']) ? ($_GET['zoom']) : (null);
	$filename = isset($_GET['style']) ? ("../styles/".$_GET['style'].".json") : (null);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<? echo $lang; ?>" lang="<? echo $lang; ?>">
	<head>
		<title><?=$appname?></title>
		<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
		<meta http-equiv="content-language" content="<? echo $lang; ?>" />
		<link rel="stylesheet" type="text/css" href="../css/legend.css" />
		<meta http-equiv="content-style-type" content="text/css" />
	</head>
	<body>
		<table>
			<?
				if (file_exists($filename))
				{
					$legend = json_decode(file_get_contents($filename), true);

					foreach ($legend['mapfeatures'] as $feature)
					{
						if ($zoom >= $feature['minzoom'] && $zoom <= $feature['maxzoom'])
						{
							if ($feature['symbol'] != null)
								echo "<tr><td style=\"width: 80px; height: 16px;\"><svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">".$feature['symbol']."</svg></td><td>"._($feature['caption'])."</td></tr>\n";
							else
								echo "<tr><td style=\"width: 80px; height: 16px;\"><img src=\"../styles/".$feature['icon']."\" /></svg></td><td>"._($feature['caption'])."</td></tr>\n";
						}
					}
				}
			?>
		</table>
	</body>
</html>

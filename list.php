<?php
$results = array();
 $directory = "repo:/";
   $i = 0; // create a handler for the directory
    $handler = opendir($directory);
 
    // open directory and walk through the filenames
?>
<html>
<head>
<title>List of files</title>
</head>
<body>
<div align="center">
<?php
while ($file = readdir($handler)) {
 
      // if file isn't this directory or its parent, add it to the results
      if ($file != "." && $file != "..") {
        $results[] = $file;
 
  echo '<a href="'.$directory .$file . '">'.$file . '</a> <br /> <br />';
 
  }}
 
    // tidy up: close the handler
    closedir($handler);
?>
 
</div>
</body>
</html>

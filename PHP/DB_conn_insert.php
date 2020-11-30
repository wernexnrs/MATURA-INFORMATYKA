<?php

$link = mysqli_connect("host", "user", "pass", "db") or die ("error");

$var = $_POST["name"]; //z forma
$sql = "INSERT INTO tabela() VALUES ('$var')";

if(!mysqli_query($link, $sql)){
  echo "error";
}else{
  echo "added";
}

mysqli_query($link, $sql) or die("error"); // bez zwracania potwierdzenia dodania

header('Lociation: index.php'); // powrot do index.php

mysqli_close($link);

?>

<?php
  $sql = "SELECT nazwa, wystepowanie FROM ryby WHERE styl_zycia = 1";

  $result = mysqli_query($link, $sql);
  
  if (mysqli_num_rows($result) > 0) { //jezeli jest zero wierszy
    while($row = mysqli_fetch_assoc($result)) {
      echo $row["idklienta"].$row["imie"].$row["nazwisko"].$row["miejscowosc"]."<br>";
    }
  }	else echo "0 results;

?>

<?php
$mysqli = new mysqli("3.133.100.99", "kang851216", "rkdrudals1", "RAWDATA");
if($mysqli->connect_error) {
  exit('Could not connect');
}

$sql = "SELECT date, time, machineno, QRcode, weight
FROM data";

$stmt = $mysqli->prepare($sql);
$stmt->bind_param("s", $_GET['q']);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($date, $time, $machineno, $QRcode, $weight);
$stmt->fetch();
$stmt->close();

echo "<td>" . $date . "</td>";
echo "<td>" . $time . "</td>";
echo "<td>" . $machineno . "</td>";
echo "<td>" . $QRcode . "</td>";
echo "<td>" . $weight . "</td>";
?>
<?php
$mysqli = new mysqli("3.133.100.99", "kang851216", "rkdrudals1", "RAWDATA");
if($mysqli->connect_error) {
  exit('Could not connect');
}

$sql = "SELECT machineno, date, doorstat, hopperstat
FROM data WHERE machineno = 'AEL-001'";

$stmt = $mysqli->prepare($sql);
$stmt->bind_param("s", $_GET['q']);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($machineno, $date, $doorstat, $hopperstat);
$stmt->fetch();
$stmt->close();

echo "<td>" . $machineno . "</td>";
echo "<td>" . $date . "</td>";
echo "<td>" . $doorstat . "</td>";
echo "<td>" . $hopperstat . "</td>";
?>
<style>
table
{
    width: 100%;
    border-collapse: collapse;
}
table, td, th
{
    border: 1px solid black;
    padding: 5px;
}
th
{
    text-align: left;
}
</style>
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
echo "<th>time</th>";
echo "<td>" . $time . "</td>";
echo "<th>machineno</th>";
echo "<td>" . $machineno . "</td>";
echo "<th>QRcode</th>";
echo "<td>" . $QRcode . "</td>";
echo "<th>weight</th>";
echo "<td>" . $weight . "</td>";
?>
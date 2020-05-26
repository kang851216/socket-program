<?
    $conn = new mysqli("3.133.100.99", "kang851216", "rkdrudals1", "RAWDATA");

    if($conn->connect_errno) {
        echo "DB Connection Error";
    } else {
        echo "DB Connection Success";
    }
?>
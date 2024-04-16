<?php

$database = mysqli_connect("127.0.0.1", "root", "", "edoc", 4306);

// Check connection
if (!$database) {
    die("Connection failed: " . mysqli_connect_error());
}

?>
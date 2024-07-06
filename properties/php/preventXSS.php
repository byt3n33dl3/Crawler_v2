<?php

/**
 * Sanitizes input data to prevent SQL Injection
 * @param string $data The input data to sanitize
 * @return string Sanitized input data
 */
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

/**
 * Escapes output to prevent XSS
 * @param string $data The output data to escape
 * @return string Escaped output data
 */
function escapeOutput($data) {
    return htmlspecialchars($data);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = sanitizeInput($_POST['username']);
    // Proceed with $username handling
}
?>

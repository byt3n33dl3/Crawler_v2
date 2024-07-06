<?php
// OutputEscaper.php

/**
 * This module contains functions related to escaping output to prevent XSS attacks.
 */

/**
 * Escapes HTML entities in the output.
 * @param string $data The data to be escaped
 * @return string The escaped data
 */
function escapeForHTML($data) {
    return htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
}

/**
 * Securely renders user-generated content on the page.
 * @param string $content The user-generated content to be rendered
 */
function renderUserContent($content) {
    echo escapeForHTML($content);
}

// Example usage in a view
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Secure Page</title>
</head>
<body>
    <div>
        <?php
        // Assuming $userContent comes from a database or user input
        $userContent = "<script>alert('XSS');</script> This is user content.";
        renderUserContent($userContent);
        ?>
    </div>
</body>
</html>

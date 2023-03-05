<?php   
    if($_SERVER['REQUEST_METHOD'] !== 'POST') {
        die('Please use the requestmethod POST');
    }
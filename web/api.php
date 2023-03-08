<?php   
    // This api is not authenticated on purpose! I'm to lazy...!

    $debug = true;

    if($debug) {
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);
    }

    // -----------------------------------------
    // ----------------------------------------- FUNCTIONS
    // -----------------------------------------

    # json return
    function jr($text, $status = true) {
        header('Content-Type: application/json; charset=utf-8');
        return json_encode([
            'status' => $status,  
            'message' => $text
        ]);
    }

    function fireSingle($url) {
         if(count($url) !== 2) {
            die(jr('Please specify a channel to fire', false));
        }

        if(!is_numeric($url[1])) {
            die(jr('Please specify the channel number', false));
        }

        // execute the python script to fire channel x
        exec("sudo /usr/bin/python /var/www/html/fireAdapter.py fire {$url[1]}", $output, $r_code);

        if($r_code !== 0) {
            // if the python script returned an error code (code other than 0), print error message, if provided by python script.
            die(jr(isset($output[0]) ? $output[0] : 'something went wrong', false));
        }

        die(jr('ok', true));
    }

    function fireAll($url) {
         if(count($url) !== 1) {
            die(jr('Please specify nothing after the endpoint', false));
        }

        // execute the python script to fire all channels
        exec("sudo /usr/bin/python /var/www/html/fireAdapter.py fireall", $output, $r_code);

        if($r_code !== 0) {
            // if the python script returned an error code (code other than 0), print error message, if provided by python script.
            die(jr(isset($output[0]) ? $output[0] : 'something went wrong', false));
        }

        die(jr('ok', true));
    }

    // -----------------------------------------
    // ----------------------------------------- SCRIPT
    // -----------------------------------------

    // request method must be POST
    if($_SERVER['REQUEST_METHOD'] !== 'POST') {
        die(jr('Please use the method POST', false));
    }
    
    // the pathinfo (the part after *.php/ like: server.com/api.php/endpoint) must be set to something
    if(!isset($_SERVER['PATH_INFO'])) {
        die(jr('Please specify an endpoint', false));
    }

    // split different parts of endpoint into an array api.php/1/2/3/4 -> [1,2,3,4]
    $url = rtrim($_SERVER['PATH_INFO'], '/'); // remove last slash
    $url = substr($url, 1); // remove first slash
    $url = filter_var($url, FILTER_SANITIZE_URL); // sanitize URL
    $url = explode('/', $url);

    if($url[0] == '') {
        die(jr('Please specify an endpoint', false));
    }

    // switch over all possible endpoints
    switch ($url[0]) {
        case 'fire':
            fireSingle($url);
            break;
        case 'fireall':
           fireAll($url);
            break;
        default:
            die(jr('Please specify a valid endpoint', false));
            break;
    }
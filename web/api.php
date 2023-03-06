<?php   
    // This api is not authenticated on purpose! I'm to lazy...!

    $debug = true;
    if($debug) {
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);
    }

    // request method must be POST
    if($_SERVER['REQUEST_METHOD'] !== 'POST') {
        die('Please use the method POST');
    }
    
    // the pathinfo (the parte after *.php/ like: server.com/api.php/endpoint) must be set to something
    if(!isset($_SERVER['PATH_INFO'])) {
        die('Please specify an endpoint');
    }

    // split different parts of endpoint into an array api.php/1/2/3/4 -> [1,2,3,4]
    $url = rtrim($_SERVER['PATH_INFO'], '/'); // remove last slash
    $url = substr($url, 1); // remove first slash
    $url = filter_var($url, FILTER_SANITIZE_URL); // sanitize URL
    $url = explode('/', $url);

    if($url[0] == '') {
        die('Please specify an endpoint');
    }

    // switch over all possible endpoints
    switch ($url[0]) {
        case 'fire':
            // \/ START ----------------------------------------- FIRE \/
            if(count($url) !== 2) {
                die('Please specify a channel');
            }

            if(!is_numeric($url[1])) {
                die('Please specify a number as a channel');
            }

            // execute the python script
            exec("sudo /usr/bin/python /var/www/html/fireAdapter.py {$url[1]}", $output, $r_code);

            if($r_code !== 0) {
                // if the python script returned an error code (code other than 0), print error message, if provided by python script.
                die(isset($output[0]) ? $output[0] : 'something went wrong');
            }

            echo 'ok';

            // /\ END ----------------------------------------- FIRE /\
            break;
        case 'fireall':
            // \/ START ----------------------------------------- FIRE ALL \/
            echo "fireall";
            // /\ END ----------------------------------------- FIRE ALL /\
            break;
        default:
            die('Please specify a valid endpoint');
            break;
    }
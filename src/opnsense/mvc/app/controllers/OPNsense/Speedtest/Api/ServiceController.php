<?php
namespace OPNsense\Speedtest\Api;

use OPNsense\Base\ApiControllerBase;
use OPNsense\Core\Backend;

class ServiceController extends ApiControllerBase
{    
    public function listAction()
    {
        $backend = new Backend();
        $response = $backend->configdRun("speedtest serverlist");
        return array("response" => $response);
    }

    public function testAction($serverid = 0)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest run ${serverid}"));
        return array("response" => $response);
    }

    public function test1Action($serverid = 0)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest run1 ${serverid}"));
        return array("response" => $response);
    } 

    public function runAction($serverid = 0)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest run ${serverid}"));
        return array("response" => $response);
    }
    
    public function run1Action($serverid = 0)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest run1 ${serverid}"));
        return array("response" => $response);
    }

    public function statAction()
    {
        $backend = new Backend();
        $response = $backend->configdRun("speedtest stat");
        return array("response" => $response);
    }

    public function logAction()
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest log"));
        return array("response" => $response);
    }

    public function deletelogAction()
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest deletelog"));
        return array("response" => $response);
    }


}


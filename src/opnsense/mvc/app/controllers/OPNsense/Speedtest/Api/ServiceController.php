<?php
namespace OPNsense\Speedtest\Api;

use OPNsense\Base\ApiControllerBase;
use OPNsense\Core\Backend;

class ServiceController extends ApiControllerBase
{

    public function pytestAction(int $serverid)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest pytest ${serverid}"));
        return array("response" => $response);
    } 

    public function testAction(int $serverid)
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest test ${serverid}"));
        return array("response" => $response);
    }

    public function listAction()
    {
        $backend = new Backend();
        $response = $backend->configdRun("speedtest serverlist");
        return array("response" => $response);
    }

    public function runAction()
    {
        $backend = new Backend();
        $response = trim($backend->configdRun("speedtest run"));
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


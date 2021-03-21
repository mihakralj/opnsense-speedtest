<?php

/*
# Copyright 2021 Miha Kralj
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.   You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/
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

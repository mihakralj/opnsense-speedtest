<?php

/*
# Copyright 2021 Miha Kralj
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.   You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/
namespace OPNsense\Speedtest;

class IndexController extends \OPNsense\Base\IndexController
{
    public function indexAction()
    {
        // pick the template to serve to our users.
        $this->view->pick('OPNsense/Speedtest/index');
    }
}

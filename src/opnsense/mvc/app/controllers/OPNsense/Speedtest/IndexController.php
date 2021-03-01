<?php
namespace OPNsense\Speedtest;
class IndexController extends \OPNsense\Base\IndexController
{
    public function indexAction()
    {
        // pick the template to serve to our users.
        $this->view->pick('OPNsense/Speedtest/index');
    }
}
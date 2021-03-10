<?php
namespace OPNsense\Speedtest;
class ChartController extends \OPNsense\Base\IndexController
{
    public function indexAction()
    {
        // pick the template to serve to our users.
        $this->view->pick('OPNsense/Speedtest/chart');
    }
    
}
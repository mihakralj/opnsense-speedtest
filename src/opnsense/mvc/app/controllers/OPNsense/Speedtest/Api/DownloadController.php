<?php
namespace OPNsense\Speedtest\Api;
use OPNsense\Base\ApiControllerBase;

class DownloadController extends ApiControllerBase
{
    const DATA_CSV = '/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv';

    public function csvAction()
    {
        $this->response->setStatusCode(200, "OK");
        $this->response->setContentType('text/csv', 'UTF-8');
        $this->response->setHeader("Content-Disposition", "attachment; filename=\"speedtest.csv\"");
        $data = file_get_contents(self::DATA_CSV);
        $this->response->setContent($data);
    }

    public function afterExecuteRoute($dispatcher)
    {
        $this->response->send();
    }
}

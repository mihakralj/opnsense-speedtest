# opnsense-speedtest
speedtest plugin for OPNsense

## install
```
sudo pkg add https://github.com/mihakralj/opnsense-speedtest/raw/main/work/pkg/os-speedtest-devel-0.7_1.txz
```

## remove
`sudo pkg delete os-speedtest-devel`

### Version 0.7
- no dependency at install time; plugin detects if speedtest is missing and allows installation
- complete rewrite of Python wrapper (opn_speedtest.py) that now accepts tons or parameters:
-> no paramter == default speedtest test
-> numeric parameter == server id for specific speedtest test
-> t or list == list of the nearest 10 speedtest servers
-> l or log == show the most recent 50 results from CSV file
-> s or stat == display statistics of all tests in CSV file
- added the install_speedtest.sh with three paramters:
->  bin == install Oookla binary
->  cli == install Python speedtest-cli
->  delete == uninstall it all

### Version 0.6
- we are back with embedded binary copy of speedtest...

### Version 0.5
- removed local binary copy of speedtest - needs to be installed separately
- cleanup, copyright notices, getting ready for a pull request to main OPNsense/plugins repo

### Version 0.4
- better exception-handling logic
- widget for the dashboard
- moved the speedtest menu entry into the Reporting menu structure

### Version 0.3
- added log output at the bottom - with the export and delete actions
- cron job accepts the speedtest serverid as an argument to lock down the target for cron jobs

### Version 0.2
- enabled cron task - you can add it at System-Settings-Cron and add a new command `Run Speedtest`
- added the api call to execute the statistical test: `/api/speedtest/service/run`
- added the api call to get json with statistics: `/api/speedtest/service/stat`
- added the output to .csv file - all tests for statistics are inserted into `/usr/local/opnsense/scripts/OPNsense/speedtest/speedtest.csv`
- deleting `speedtest.csv` will zero-out statistics

### Version 0.1
Core diagnostics (socket test and http test)

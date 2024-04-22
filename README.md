# DevOps-Internship-Task---LAMS
A LAMS (Log Analysis and Monitoring System) application made in Python.

Syntax of using this app: `python3 log-monitor.py <logfile-absolute-path>`

SCENARIO-1: Monitoring User Authentication Logs at `/var/log/auth.log`<br />
  [+] Add keywords to track in the keyword.txt file
  
  ![Screenshot from 2024-04-22 21-26-06](https://github.com/0xDAYZ/DevOps-Internship-Task---LAMS/assets/98089001/8eaabd6a-59b9-495c-8c03-e70aaa6a61b5)

  [+] Start the Logger
  
  ![Screenshot from 2024-04-22 20-44-30](https://github.com/0xDAYZ/DevOps-Internship-Task---LAMS/assets/98089001/e9ab61c0-2d20-4dda-8dae-1768f9118661)
  
  ![Screenshot from 2024-04-22 20-45-28](https://github.com/0xDAYZ/DevOps-Internship-Task---LAMS/assets/98089001/63ee42d5-37c2-4ef9-b04b-91a82c015305)

SCENARIO-2: Monitoring WebServer(apache2) Logs at `/var/log/apache2/access.log`<br />
  [+] Add keywords to track in the keyword.txt file
  
  ![Screenshot from 2024-04-22 20-53-03](https://github.com/0xDAYZ/DevOps-Internship-Task---LAMS/assets/98089001/27327421-5b2e-4758-8149-473244c07a44)

  [+] Start the Logger
  ![Screenshot from 2024-04-22 20-52-03](https://github.com/0xDAYZ/DevOps-Internship-Task---LAMS/assets/98089001/530828d5-13d4-4f15-90e3-89ad0d07c661)

Note: apache2 log files require sudo privileges to view logs, so use `sudo python3 log-monitor.py /var/log/apache2/access.log`


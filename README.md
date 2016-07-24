# fsnd-linux-server
Info for FSND Linux Server App

i. The IP address and SSH port so your server can be accessed by the reviewer.

- ip address: 52.37.97.169
- ssh -p 2200 -i ~/.ssh/udacity_key.rsa grader@52.37.97.169

ii. The complete URL to your hosted web application.

http://ec2-52-37-97-169.us-west-2.compute.amazonaws.com/

iii. A summary of software you installed and configuration changes made.
- installed flask, sql alchemy, 
- added finger
- added grader acct (grader@glf), setup rsa key
- added a catalog acct. for the catalog db with pw access to catalog db
- installed ntp
- changed ssh to 2220
- setup ufm to only allow port 80, ssh on 2200, ntp

iv. A list of any third-party resources you made use of to complete this project.
- digital ocean's apache server, flask, mod_wsgi, psql setup documentation

* Note: this repo is saved in ~/FlaskApp, not in /var/www/

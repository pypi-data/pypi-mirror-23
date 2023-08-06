Introduction
============

A nagios-like plugin to check if task jobs executed successfully

Configuration
=============

On the first run, it will ask you for basic configuration.
- `basePath` is where each job will put his folder containing the logs

    (if a job log is in `/var/log/task/job/timestamp.log`, the basePath is `/var/log/task/`)
- `endingString` is the string the script will look for too check if a job executed successfully, if the string is in the last line of file, then it's OK, CRITICAL otherwise. It will should be something like `;END\n`

To change configuration go to the script install directory and open the config.ini file.


Changelog
=========

0.1-dev (unreleased)
------------------------

- Elio Maisonneuve <maisonneuv@eisti.eu>


Contributors
==============

Elio Maisonneuve, Author



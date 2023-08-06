Tool: 2_check_and_report

Description:
************

This program performs some checks and return a report in case some of these checks fail:
- The number of databases created is under a specific threshold parametrized through the -m argument.
- The disk used by postgresql is not over a percentage of the total disk. The specific percentage is parametrized through the -p argument.
- The number of connections stablished to the database is not over a percentage of the max connections value. The specific percentage is parametrized through the -c argument.


How to:
*******

Note: The next commands are meant to be run in the same that directory in which this Readme.txt file is stored.

- Disable any previously activated virtualenv:

$ deactivate

- Setup environment:

$ ../../setup_env.sh

- Enable virtualenv:

$ source venvs/2_check_and_report/bin/activate

- Get the program help:

$ ./run -v

- Run the tool (example):

This command checks:
the amount of databases is less than 10,
the percentage of partition disk used by postgresql is less than 0.2%, and
the percentage of active connections to the postgresql service is less than 2.5%.

$ ./run.py -m 10 -p 0.2 -c 2.5



Tool: pg_stats

Description:
************

This program iterates over all the databases and their datasets, get and shows these info:
- Average of rows per database
- Total rows in the entire server

How to:
******

Note: The next commands are meant to be run in the same that directory in which this Readme.txt file is stored.

- Disable any previously activated virtualenv:

$ deactivate

- Setup environment:

from this directory, run the next command:

$ ../../setup_env.sh

- Enable virtualenv:

$ source venvs/3_stats/bin/activate

- Get the program help:

$ pg_stats -v

- Run the tool:

$ pg_stats



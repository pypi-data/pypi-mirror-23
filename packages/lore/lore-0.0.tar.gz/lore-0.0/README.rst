Sybil
-----

Sybil is a python data science framework to build, train, test and run data science models in production. It codifies best practices to simplify deploying models developed on a laptop with jupyter notebook, into high availability clusters for production.

Example
=======
::

$ sybil create my_project # sybil setup my_project && workon my_project
$ sybil generate my_model
$ sybil fit my_model
$ sybil serve my_model &
$ curl -X POST in http://localhost:3000/my_model



Project Structure
=================
::

├── .env.template            <- Template for environment variables for developers (mirrors production)
├── .python-version          <- keeps dev and production in sync (pyenv)
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- keeps dev and production in sync (pip)
│
├── bin/                     <- application processes
│   ├── clocks               <- defines cron jobs (daemonized in production)
│   ├── console              <- launches an interactive session
│   ├── api                  <- runs hub endpoints (daemonized in production)
│   ├── start                <- start everything required based on environment (delegates to systemd/upstart/applescript)
│   ├── stop                 <- stop everthing that has been started
│   └── test                 <- run tests
│
├── docs/
│
├── notebooks/               <- explorations of data and models
│       └── my_exploration/
│            └── exploration_1.ipynb
│
├── src/
│   ├── __init__.py          <- loads the various components (makes this a module)
│   │
│   ├── api/                 <- external entry points to runtime models
│   │   └── __init__.py      <- loads the various components (makes this a module)
│   │
│   ├── config/              <- environment, logging, exceptions, metrics initializers
│   │   └── __init__.py      <- loads the various components (makes this a module)
│   │
│   ├── tasks/               <- run manually, cron or aiflow
│   │   ├── __init__.py      <- loads the various components (makes this a module)
│   │   └── my_model/
│   │       ├── etl.py
│   │       └── train.py
│   │
│   ├── data/                <- Scripts to move data between sources
│   │   ├── __init__.py      <- loads the various components (makes this a module)
│   │   └── etl/             <- etl sql between DBs (local/production too)
│   │       └── table_name.sql
│   │
│   ├── features/            <- abstractions for dealing with processed data
│   │   ├── __init__.py      <- loads the various components (makes this a module)
│   │   └── my_features.py
│   │
│   └── models/              <- Code that make predictions
│       ├── __init__.py      <- loads the various components (makes this a module)
│       └── my_objective/
│           ├── deep_model.py
│           └── linear_model.py
│
└── test/
    ├── upstart/             <- production scripts to start/stop/monitor daemons (endpoints/workers/consumers)
    └── init.sls




Sybil stands on the shoulders giants
====================================

We support workflows that utilize

* tensorflow (keras)
* scikitlearn
* pandas
* numpy
* sqlalchemy
* psychopg
* virtualenv, pyenv, python (2.7, 3.3+)


Design Philosophies
===================

* Convention over configuration (https://en.wikipedia.org/wiki/Convention_over_configuration)
* Minimal Abstraction

Inspiration
===========

* Rails (https://en.wikipedia.org/wiki/Ruby_on_Rails)
* Cookie Cutter Data Science (https://drivendata.github.io/cookiecutter-data-science/)



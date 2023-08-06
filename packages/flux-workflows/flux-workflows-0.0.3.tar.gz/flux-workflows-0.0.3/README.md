flux-workflows
==============

flux-workflows is a command line tool for interacting with Flux.

Installation
------------

Install, upgrade and uninstall fluxer with these commands:
```sh
$ pip install flux-workflows
$ pip install --upgrade flux-workflows
$ pip uninstall flux-workflows
```
or fork this repository

Usage
-----

```sh
workflow --help

Usage: workflow [OPTIONS] COMMAND [ARGS]...

  Workflow manages your flux workflows from the terminal

Options:
  -h, --help  Show this message and exit.

Commands:
  config           Configure the CMP URL and credentials
  create           Create a workflow skeleton
  delete           Delete a workflow
  delete-instance  Delete an instance
  get              Download a workflow to edit or view locally
  list             List existing flux workflows
  list-instances   List instances of a workflow
  logs             Get logs for a workflow
  run              Run a workflow
  show             Display details of a Flux workflow
  show-instance    Display details of an instance
  update           Update (patch) a workflow
  update-instance  Update an instance's event for debugging
  upload           Upload the current workflow
  validate         Validate the current workflow


```

Dependencies
------------

The flux-workflows tool is supported on Python 2.7.

The main dependencies are:
* [requests]: HTTP for Humans
* [click]: for creating beautiful command line interfaces
* [jsonschema]: an implementation of JSON Schema for Python
* [jinja2]: modern and designer-friendly templating language for Python

The testing dependencies are:
* [pytest]: helps you write better programs
* [mock]: a library for testing in Python

Testing
-------

Make sure you have [tox] by running the following:
```sh
$ pip install tox
```

To run the package tests:
```sh
$ tox
```
or
```sh
$ make test
```

License
-------

[GNU General Public License, version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

[//]: #
   [requests]: <http://docs.python-requests.org>
   [click]: <http://click.pocoo.org>
   [jsonschema]: <https://python-jsonschema.readthedocs.io/en/latest/>
   [jinja2]: <http://jinja.pocoo.org>
   [mock]: <https://pypi.python.org/pypi/mock>
   [pytest]: <http://doc.pytest.org>
   [tox]: <https://tox.readthedocs.io/>

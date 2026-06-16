# PythonStarterPackage Tutorial

The purpose of this tutorial is to show you how to create a standard Python
package from scratch. Feel free to reference
[PythonStarterPackage](https://github.com/ArcticTechnology/PythonStarterPackage)
when going through this tutorial. It is what the end result will look like.

## Background

In order to create a Python package that can be used with `pip`, it is strongly
recommended that you use Python's modern
standards, such as `pyproject.toml` and the 
[build](https://build.pypa.io/en/stable/) tool to set up your package and then
push it to PyPI.

## `pyproject.toml` intro

The critical file at the heart of your package is `pyproject.toml`, which
replaces the older `setup.py` and `setup.cfg` files, as reported in these PEPs:

- [PEP 517](https://peps.python.org/pep-0517/)
- [PEP 518](https://peps.python.org/pep-0518/)
- [PEP 621](https://peps.python.org/pep-0621/)
- possibly other PEPs
- [Is `setup.py` deprecated?](https://packaging.python.org/en/latest/discussions/setup-py-deprecated/#setup-py-deprecated)

The `pyproject.toml` file is consumed by
[build](https://build.pypa.io/en/stable/) as well as other Python tools which
can read their configurations inside it, instead of relying from extra files.
`setup.py` and `setup.cfg` are no longer strictly required for new packages.

Just like `setup.cfg`, `pyproject.toml` uses a declarative approach.

## `pyproject.toml` sections

> [!NOTE]
> [Here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
> you can find a detailed tutorial. 

`pyproject.toml` is broken up into three main sections called tables:

- `[build-system]`: tells what tool to use to build the project. Setuptools
  is the most common choice for
  legacy package, but there are
  more modern alternatives
- `[project]`: all projects metadata goes here, such as project name, author 
  name, license, etc...
- `[tool]`:  tool specific configurations, usually contained in subtables

### Build system

Depending on the content of your package, you have to [choose a build
backends](https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-a-build-backend).
Other recommendations [here](https://packaging.python.org/en/latest/guides/tool-recommendations/#build-backends)

Setuptools is the historical tool for this but there are more modern official
alternatives such as Hatchling and Flit. What changes is the compatibility with
C, C++, and other language extensions, build speed, etc... Setuptools should
be used for legacy and extensions written in different programming languages.

You can use this, for example:

```toml
[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"
```

or this:

```toml
[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"
```

### Project

The `[project]` section contains all of the key metadata of the package such as
name, version, license, etc. It looks like the following:

```toml
[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
license = "MIT"
license-files = ["LICEN[CS]E*"]

[project.urls]
Homepage = "https://github.com/pypa/sampleproject"
Issues = "https://github.com/pypa/sampleproject/issues"
```

A full list of descriptions of key-value pairs is present on the [Python
Packaging User Guide website](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml).

#### Dependencies

If a package is not trivial, it usually makes use of some Python dependency
from PyPI. You can specify them as a list. For example:

```toml
dependencies = [                                       
    "requests>=2.27.1",                                
]
```

See
[this](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#dependencies-and-requirements)
for more details.

#### Version naming

Using [Semantic Versioning](https://semver.org/) is a good approach to name
versions of your package. 

The
[Version specifiers](ttps://packaging.python.org/en/latest/specifications/version-specifiers/#semantic-versioning)
in Python accept the use of semantic
versioning as a way to define this value, although some details differ from Semantic Versioning:

> The “Major.Minor.Patch” (described in this specification as “major.minor.micro”) aspects of semantic versioning (clauses 1-8 in the 2.0.0 specification) are fully compatible with the version scheme defined in this specification, and abiding by these aspects is encouraged.

Generally, you can use SemVer in your projects without problems.

#### Classifiers

[Classifiers](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#classifiers)
are values used in the PyPI website for filtering packages during a search.
A full list is available on [this PyPI page](https://pypi.org/classifiers/)

#### More sections and values

What follows is a list of other important key-values to place in the
`[project]` table

- `requires-python`
  - Python version
- `authors` and `maintainers`
- `description`
  - package description
- `readme`
  - links the `README.md` from the root of your repository
- `license` and `license-files`
  - software license of the package
- `[project.urls]`
  - a table with all necessary urls, such as homepage, documentation, issue
    tracker, etc...
- `[project.scripts]`
  - a table that defines the executable scripts for your package so you can
    define a binary entry point

### Tools

Extra tools such as setuptools, tox, bandit, and lots of other python packages
are able to parse `pyproject.toml` and read specific parts of its
configuration. This way you can centralize all configurations in a single file
instead of relying on tool specific paths.

With Setuptools, for example, you can define where to look for app data,
assets, environmental variables, documentation, external and sample data, etc.
This is set up in the `[tool.setuptools]` table.

## Updating the requirements

> [!IMPORTANT]                                         
> Always [start the virtual environment first](../README.md#virtual-environment).

During package development you might need to use external Python dependencies.
The standard mode of operation is to update the [dependencies](#dependencies)
list and `[project.optional-dependencies]` table list in `pyproject.toml`.

You then need to install the dependencies in **editable** mode, which means
any changes done to your local package will be reflected in the environment
without having to do any reinstall:

```shell
pip install --editable .[dev]
```

## Files and directories

### Repository

A Python open source repository typically includes several files and a specific
directory structure:

| Path | Description |
|------|-------------|
| `./.gitignore` | files and directories you want Git to exclude from commits. [GitHub has a Python specific template](https://raw.githubusercontent.com/github/gitignore/refs/heads/main/Python.gitignore) for this |
| `./LICENSE` | file defining your package license |
| `./README.md` | readme file for basic documentation |
| `./tests/` | a directory containing the test scripts (for example unit tests) |
| `./doc/` | a directory containing the documentation files |

Take a look at the contents of each of the above files and directories in this
package to see how they are structured.

### Application

The application files of your package should be located in a directory named
`./src/${packageName}/`. Python can also auto discover the package if you name
the application file directory as `./${packageName}/`. This specific template
follows the former convention, so the application directory is
`./src/pythonstarterpackage/`.

| Path | Description |
|------|-------------|
| `./src/${packageName}/__init__.py` | each of the subdirectories under `./src/${packageName}/` should contain an `__init__.py` file which tells python to discover that directory and include it in the release |
| `./src/${packageName}/__main__.py` | this allows an execution entry point. For example: `python3 -m pythonstarterpackage`. See this guide explaining [`__main__.py`](https://stackoverflow.com/questions/4042905/what-is-main-py) |
| `./src/${packageName}/main.py` | this is an entry point called by `__main__.py` and contains all the necessary logic to start the program |
| `./src/${packageName}/starterpkg.py` | contains the CLI interface or the main logic of your project |
| `./src/${packageName}/utils/` | a directory containing utility submodules for your program |

The reason of having separate `__main__.py` and `main.py` is to be able to
import the modules within Python, which is not possible by putting all the
entry point logic in `__main__.py`.

## Deploying your package

### Testing

> [!IMPORTANT]                                         
> Always [start the virtual environment first](../README.md#virtual-environment).

Before you deploy your package you should test it. You can do this by
following the [**Local install**](../README.md#local-install),
[**Usage**](../README.md#usage), and [**Removal**](../README.md#removal)
instructions.

You can then import the `main.py` module and run it directly.

1. open a Python shell:

   ```shell
   python3
   ```

2. import:

   ```python
   >>> from pythonstarterpackage import main
   ```

3. run:

   ```python
   >>> main.main()
   ```

You can also test the packages without having to install the package locally:

1. move in the `src` directory

   ```shell
   cd src
   ```

2. follow previous steps 1 to 3

Alternatively, you can run tests via [tox](https://github.com/tox-dev/tox):

1. run `tox`:

   ```shell
   tox
   ```

### PyPI account setup

PyPi is the default Python package index for people to upload their public
packages.

These instructions need to be followed only once.

1. go to [pypi.org](https://pypi.org) and create an account
2. validate your email
3. go to *Account Settings* and create an API token. Your API token will look
   like this: `pypi-OFJou945u2fd0i94u93ut....`
4. Create a `.pypirc` file in your home directory. The `.pypirc` file allows
   you to define the configuration for package indices, so that you don't have
   to enter the URL, username, or password whenever you upload a package.

   That is where `twine` will look for a `.pypirc` file. See this
   [twine install guide](https://github.com/areed1192/sigma-coding/blob/master/resources%20and%20note/installation_twines.md)
   for more details.
5. in your `.pypirc` add the following. Note that the password is your API
   token:

   ```ini
   [distutils]
   index-servers=
           pypi
           testpypi
           pypi-username
           testpypi-username
   [pypi]
   username = __token__
   password = pypi-OFJou945u2fd0i94u93ut....
   ```

6. if you have a testpypi account with a test api token you can add it to
   `.pypirc` as well:

   ```shell
   [testpypi]
   username = __token__
   password = pypi-OFJou945u2fd0i94u93ut....
   ```

### Building the package distribution

> [!IMPORTANT]
> Always [start the virtual environment first](../README.md#virtual-environment).

1. upgrade the development tools:

   ```shell
   pip3 install --upgrade setuptools wheel twine build
   ```

2. build the package with the modern
   [`build`](https://build.pypa.io/en/stable/) tool:

   ```shell
   python3 -m build
   ```

3. check the contents of the `.whl` and `.tar.gz` distributions. The key things
   to look for are:
   1. all of your package subdirectories like utils are added to both
      distributions
   2. your config and package data are included in both distributions

   Extract the dist files like this:

   ```shell
   unzip -l dist/*.whl && tar --list -f dist/*.tar.gz
   ```

4. test a local install of the package and run the binary directly to make sure
   it is working:

   ```shell
   pip3 install .
   pythonstarterpackage
   ```

5. uninstall the package:

   ```shell
   pip3 uninstall pythonstarterpackage
   ```

6. delete the distribution files:

   ```shell
   rm -rf build dist src/*.egg-info
   ```

> [!NOTE]
> If there are any issues with the steps you can uninstall the package, delete
> the distributions then proceed to troubleshoot the issue. Once completed,
> start over from the beginning.

> [!CAUTION]
> Be careful not to remove necessary files. Follow the steps verbatim.

### Upload to PyPI

> [!IMPORTANT]
> Always [start the virtual environment first](../README.md#virtual-environment).

1. upload using `twine`:

   ```shell
   twine upload dist/*
   ```

2. quit and remove the virtual environment. We need to check if the package
   installs correctly from PyPI:

   ```shell
   deactivate
   rm -rf .venv
   ```

3. install your package with `pip`:

   ```shell
   pip3 install pythonstarterpackage
   ```

4. run the app:

   ```shell
   pythonstarterpackage
   ```

5. uninstall:
   ```shell
   pip3 uninstall pythonstarterpackage
   ```

> [!NOTE]
> If you get a `Requirements already satisfied...` for pythonstarterpackage
> when trying to install, it may be because `pip` still thinks you have the
> package already installed from the testing earlier. Remove the
> `./src/PythonStarterPackage.egg-info` file, then try uninstalling and
> reinstalling again.

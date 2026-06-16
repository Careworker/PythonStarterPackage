# Python Starter Package

The purpose of this project is to show you how to create a standard Python
package from scratch. This project is inspired by the excellent
[getmyip package](https://github.com/iamtennislover/getmyip)
by [@iamtennislover](https://github.com/iamtennislover)
and [this tutorial](https://github.com/areed1192/sigma-coding) on deploying
python packages by [@areed1192](https://github.com/areed1192).

For a step-by-step guide on how to deploy a package check the
[PythonStarterPackage tutorial](doc/PythonStarterPackage_Tutorial.md).
If you are using this starter package for the first time, I definitely
recommend following the tutorial first.

This repository can also be used as a template each time you create a new
package. Use the instructions below for installing, testing, and deploying.

## Prerequisites

### Requirements

- Python3 >= 3.8
  - depending on the platform you can either download Python 3 from the
    [official website](https://www.python.org/downloads/), use the package
    manager of your distribution or the Windows store
  - see the [Virtual environment](#virtual-environment) section below
  - check the version with `python3 --version`
- pip3 >= 20.2.1 
  - make sure to install the `python3-pip` package in order to use the
    `pip install` command
  - check the version with `pip3 --version`
- [a Python virtual environment](#virtual-environment)

### Virtual environment

Using a virtual environment is a solution strongly suggested by
[PEP 668](https://peps.python.org/pep-0668/). When you attempt to install a
package directly from PyPI using pip, you might get this error message:

```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
```

If you follow all the instructions below, depending on your operating system,
the process of creating a virtual environment should require just a few
minutes. See also
[*How venvs work*](https://docs.python.org/3/library/venv.html#how-venvs-work).

Historically there have been lots of different tools to manage virtual
environments and dependencies (requirements), and new ones continue to pop up.
To keep things simple, it's better to stick to the two standard built-in tools:
pip and venv.

> [!NOTE]
> Have a look at
> [this comparison list](https://pipx.pypa.io/stable/explanation/comparisons/)
> of the different tools.

#### Linux

1. open a terminal and go into the project directory
2. if you are on a new Debian-based system and never created a Python virtual
   environment before, you most probably need to install this package:

   ```shell
   sudo apt install python3-venv
   ```

   Other distrubutions might have this package bundled in Python, or the name
   might differ

3. [after you clone the repository](#local-install) go to the project directory
   and create the virtual environment

   ```shell
   python3 -m venv .venv
   . .venv/bin/activate
   ```

4. install the package in *editable mode*:

   ```shell
   pip install -e .[dev]
   ```

4. depending on the shell, the prompt changes to something similar to
   `(.venv) $`
5. after working on the package, to quit the Python virtual environment run:

   ```shell
   deactivate
   ```

#### Windows

There are two ways to work with this app in Windows. Choose either one or the
other. The [Git bash](#git-bash) way (Linux emulation layer) is the suggested method.

##### Native method

> [!IMPORTANT]
> These instructions work without emulation layers.

1. install Python 3.13 from the
   [**Windows store**](https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=en-US&gl=US)
   which works out of the box. **Don't use the releases from the Python website**.
2. open the Powershell **as administrator**, then set the execution policy to
   `Unrestricted`. This needs to be done only once, not every time you create a
   virtual environment. See also
   [https://go.microsoft.com/fwlink/?LinkID=135170](https://go.microsoft.com/fwlink/?LinkID=135170)

   ```shell
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted
   ```

3. close the **administrator** Powershell
4. open a normal Powershell
5. [after you clone the repository](#local-install) (see also the
   [Git Bash](#git-bash) instructions on how to install Git), go to the project
   directory and proceed to create the virtual environment

   ```shell
   python3 -m venv .venv
   . .\.venv\Scripts\activate
   ```

5. install the package in *editable mode*:

   ```shell
   pip install -e .[dev]
   ```

7. after working on the package, to exit the Python virtual environment run:

   ```shell
   deactivate
   ```
   
##### Git Bash

You can run this app on a Linux emulation layer like the Git Bash terminal.
To install and set up Git Bash:

1. go to the [official Git website](https://git-scm.com/downloads) and click
   download (version >= 2.34.1)
2. during the setup, make sure to include OpenSSH. The recommended setting
   should be fine:

   ```
   Use bundled OpenSSH - This uses ssh.exe that comes with Git.
   ```

3. leave the other settings as default, click through, and install
4. download and install [Python3](https://www.python.org/downloads/)
5. open a new PowerShell from the start menu
6. open Bash:

   ```shell
   C:\Program Files\Git\bin\bash.exe
   ```

5. [after you clone the repository](#local-install), go into the project
   directory and proceed to create the virtual environment

   ```shell
   python3 -m venv .venv
   . .venv/Scripts/activate
   ```

6. install the package in *editable mode*:

   ```shell
   pip install -e .[dev]
   ```

7. after working on the package, to exit the Python virtual environment run:

   ```shell
   deactivate
   ```

> [!IMPORTANT]
> Use the `bash.exe` terminal rather than `git-bash.exe` (which is also the one
> in the start menu).
>
> There is a known issue with `git-bash.exe` messing up Python `os` commands in
> `import os`. See
> [this thread](https://stackoverflow.com/a/33623136) for details.
>
> You can find the `bash.exe` Git folder in the `bin/` directory. For example,
> if `git-bash.exe` is in `C:\Program Files\Git\git-bash.exe` then you should
> find `bash.exe` in `C:\Program Files\Git\bin\bash.exe`.

#### MacOS

1. open a terminal and go into the project directory
2. if not already installed, install Python

   ```shell
   brew install python
   ```

3. [after you clone the repository](#local-install) go to the project directory
   and create the virtual environment

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
4. install the package in *editable mode*:

   ```shell
   pip install -e .[dev]
   ```

5. after working on the package, to exit the Python virtual environment run:

   ```shell
   deactivate
   ```

## Installation

There several ways to install this app in *production* mode, i.e. as a
standalone Python package.

> [!IMPORTANT]
> Always [start the virtual environment first](#virtual-environment).

### Install via pip

This Python app is hosted on PyPI and can be installed with the following
command:

```shell
pip3 install PythonStarterPackage
```

### Local Install

Alternatively, you can download or Git clone the GitHub repo and install it
locally with the following. This method is useful also if you need to test
local changes and is equivalent to a [virtual environment](#virtual-environment) install, if done inside one.

```shell
git clone https://github.com/ArcticTechnology/PythonStarterPackage.git
cd PythonStarterPackage
pip3 install -e .
```

## Usage

After installation, you have a few ways to run this app. 

> [!IMPORTANT]
> Always [start the virtual environment first](#virtual-environment).

- run this app from the terminal with this command:

  ```shell
  pythonstarterpackage
  ```

- run this app by letting Python discover the module:

  ```shell
  python3 -m pythonstarterpackage
  ```

- you can also import the package resources and run them in your own project:

  ```python
  >>> from pythonstarterpackage import *
  >>> starter = StarterPkg()
  >>> starter.run()
  ```

## Deployment

To deploy this package make sure you have gone through all the
[PythonStarterPackage tutorial](doc/PythonStarterPackage_Tutorial.md) file.

## Removal

1. uninstall the app:

   ```shell
   pip3 uninstall PythonStarterPackage
   ```

   If you used the local install option, you will also want to delete the
   `.egg-info` file located in the `src/` directory of the repo. This gets
   created automatically with `pip3 install -e .`.

2. deactivate the environment once you stopped working with it:

   ```shell
   deactivate
   ```

3. remove the virtual envoronment:

   ```shell
   rm -rf .venv
   ```

## Troubleshooting

This section goes over some of the common issues found and how to resolve them.

### `Command Not Found` error When Running the App

#### Linux

On Linux, if you are getting a `command not found` error when trying to run the
app, you may need to add `~/.local/bin/` to the `PATH` environment variable.
This should only be needed when installing the package outside a virtual
environment.

See [this thread](https://stackoverflow.com/a/34947489) for details.

If you use the Bash shell:

1. add the Python path into the `PATH` environment variable:

   ```shell
   echo export PATH=~/.local/bin:$PATH > ~/.bash_profile
   ```

2. close the terminal
3. open a new terminal

### `"ImportError: No module named 'tkinter'`

Your python version is probably missing tkinter which typically comes default.
See [this post](https://stackoverflow.com/a/25905642) for details. Install it
with the following.

#### Linux

```shell
sudo apt-get install python3-tk
```

#### Mac

```shell
brew install python-tk
```

## Support, contributions and resources

Our software is open source and free for public use. If you found any of these
repos useful and would like to support this project financially, feel free to
donate to our bitcoin address.

- Bitcoin Address 1: `1GZQY6hMwszqxCmbC6uGxkyD5HKPhK1Pmf`
- [Github repo](https://github.com/ArcticTechnology/PythonStarterPackage)
- [PyPI](https://pypi.org/project/PythonStarterPackage/)
- [Official Python Packaging User Guide](https://packaging.python.org/en/latest/guides/tool-recommendations/)

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/main/btcaddr1.png?raw=true)

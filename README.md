## Local Machine Installation & Configuration

### Pip

Even though the package management for this repo is handled by Poetry, `pip` is still required to download and
configure Python modules. To install pip:

```shell
sudo apt update
sudo apt install python3-pip
```

To check this has been installed correctly, simply run:

```shell
pip --help
```

To verify you have the latest version installed, run:

```shell
pip --version
pip 21.2.4
```

If an older version is installed, upgrade by running:

```shell
pip install --upgrade pip
```

### Pyenv

Pyenv is used to easily control the versions of Python being used across different projects and repositories.
To install pyenv:

```shell
sudo apt install -y make build-essential \
                         libssl-dev \
                         zlib1g-dev \
                         libbz2-dev \
                         libreadline-dev \
                         libsqlite3-dev \
                         wget \
                         curl \
                         llvm \
                         libncurses5-dev \
                         libncursesw5-dev \
                         xz-utils \
                         tk-dev \
                         libffi-dev \
                         liblzma-dev \
                         python-openssl \
                         git
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Ensure to restart your terminal after performing the above. To check this has been installed correctly, simply run:

```shell
pyenv --help
```

Please ensure to install the `pyenv-update` plugin so that it can be updated from the command line. To do this:

```shell
git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
```

This will allow `pyenv` to be updated by running the following. It is important to do this as `pyenv` caches the
versions of Python available and so major and/or minor patches may not appear available to use without doing this.

```shell
pyenv update
```

This repository uses Python 3.9, so to install the latest version of that via `pyenv`:

```shell
pyenv install -v 3.9.7
```

This will take a few minutes as it builds Python from source. To then use this version of Python going forward:

```shell
pyenv local 3.9.7
pyenv global 3.9.7
```

To confirm the correct python version is being used, run the following command:

```shell
python --version
Python 3.9.7
```

To confirm the correct python version is being used by pyenv, run the following command:

```shell
pyenv version
3.9.7 (set by <directory>/pipeline-testing/.python-version)
```

### Poetry

The project is managed by [Poetry](https://python-poetry.org/). To install poetry, please follow the
[official guide](https://python-poetry.org/docs/).

Once Poetry is installed, to create the virtual environment and install the necessary packages, run the following
command from the root of this repo:

```shell
poetry config virtualenvs.in-project true
poetry install
```

This should create a `.venv` directory at the root of the repo.

### PyCharm

After opening the `pipeline-tests` repo as a project inside PyCharm, it needs attaching as a standalone project
within PyCharm. This allows it to be assigned its own Python interpreter (i.e. the virtual environment created by
Poetry above). To do this:

- Click `File -> Open...`
- Select the `pipeline-tests` directory
- Click `OK`
- Select the `Attach` option to attach this as an additional project

Once done, the `pipeline-tests` directory in the `Project` pane should be bolded.

To configure the Python interpreter for the `pipeline-tests` project:

- Open the PyCharm settings dialog (`Ctrl+Alt+S`)
- Expand the `Project` caret in the pane on the left-hand side
- Select `Python Interpreter`
- Select `pipeline-tests`
- Click the cog on the right-hand side of the dialog
- Select `Show All...`
- Click `+` to add a new interpreter
- Select the `Existing Environment` radio button
- Click the `...` button
- Navigate to `pipeline-tests/.venv/bin/python`
- Click `OK`
- Rename the new interpreter to `pipeline-tests` (for easier traceability)
- Click `OK`
- Click `Apply`

This should have correctly configured the `pipeline-tests` project to use the Python interpreter
created by Poetry. To confirm:

- Open any Python file in the `pipeline-tests` project
- Expand the `Imports` section at the top of the file
- All imports should be recognised and not underlined in red

### Pre-commit checks

The `pre-commit` module is used to ensure the code in this repo adheres to a set of coding standards on each and every
commit. To setup the `pre-commit` hooks, run the following (this only needs doing once):

```shell
poetry run pre-commit install --install-hooks
```

Before committing code, it is recommended that you run the following command to see if any changes have caused the
static code analysis tools to highlight an issue:

```shell
poetry run pre-commit run --all-files
```

### ChromeDriver

Install the latest release of the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Ensure to move the ChromeDriver executable to a location available to the system path:

```shell
sudo mv ~/Downloads/chromedriver /usr/local/bin
```

To test this is installed correctly, open a new terminal and run:

```
chromedriver
```
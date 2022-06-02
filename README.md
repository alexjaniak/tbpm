# CLPM: A Command-Line Password Manager. 
## About 
CLPM is a is an easy-to-use out-of-the-box password manager accesible solely through the command-line. The passwords are encrypted using 256 bit AES and the master password is hashed using 256 bit SHA-3. The master password is used to generate a key for encryption and for accessing the accounts. The accounts are stored in an SQL database. 

## Installation
### Requirements
* `python >= 3.9`
* `pip >= 21.1.2`

Automatically installed by pip:
* `Click >= 8.1.3`
* `pycryptodome >= 3.14.1`
* `prettytable >= 3.3.0`

### Through pip
For most, installing this project can be done using `pip install clpm`
which pulls the project from [PyPI](https://pypi.org/project/clpm/).


### Local Installation
If needed, you can install and run this project locally:
1. Clone this project to a local repository.
2. Run `python setup.py install`
*Note: setup.py uses pip to install the project as a package on the local system*

### Uninstallation
For both remote and local installation, the project can be uninstalled from your system with `pip uninstall clpm`

If you had already initialized clpm, pip won't delete the file `passwords.db` which contains all stored account information. This means that clpm can be reinstalled and still retain the same accounts & master password. If you wish to completely remove clpm from your device, you must manually remove `passwords.db` by either using the `rm` command or a file explorer. 

   
## Usage
Run `clpm init` to initialize the database. A prompt & confirmation will appear to input a master password.
*clpm will not work unless a master password is set through `clpm init` first.* 



## Extras

### TODO
* Encrypt all account information rather than just passwords.
* Add usage to the README.
* Revamp menu.
* Fix double init/reset error
* Clear terminal history after query/add




won't delete passwords.db file unless manually removed using rm ...
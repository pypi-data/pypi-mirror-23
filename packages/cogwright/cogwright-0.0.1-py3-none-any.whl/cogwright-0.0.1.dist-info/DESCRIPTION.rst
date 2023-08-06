Implements the `cog` command. `cog make` will run the standard build procedure in the current working directory. The working directory should be the project root of your git repository. Module-specific parameters and methods are specified via the `__blueprint__.py` file, which should be in the working directory. FTP login credentials may be specified in the `__auth__.py` file, which should be in the working directory, and listed in the `.gitignore` file.
`cog -A download\archivename.zip make` will specify a different archive to use as the module payload.

Home-page: https://github.com/philipov/cogwright
Author: Philip Loguinov
Author-email: philipov@gmail.com
License: UNKNOWN
Description: UNKNOWN
Platform: UNKNOWN
Classifier: Development Status : : 2 - Pre - Alpha
Classifier: Environment :: Console
Classifier: Environment :: Other Environment
Classifier: Intended Audience :: Information Technology
Classifier: Intended Audience :: Developers
Classifier: Intended Audience :: System Administrators
Classifier: Intended Audience :: End Users/Desktop
Classifier: Intended Audience :: Customer Service
Classifier: License :: Other/Proprietary License
Classifier: Operating System :: Microsoft :: Windows :: Windows 7
Classifier: Operating System :: POSIX :: Linux
Classifier: Programming Language :: Python :: 3.6
Requires: twine
Requires: wheel

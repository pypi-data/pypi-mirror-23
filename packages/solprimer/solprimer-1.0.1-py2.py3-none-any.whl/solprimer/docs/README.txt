===== Installation instructions

The ‘solprimer’ package is written in pure universal Python. It does not contain any code in other languages or any precompiled modules. The code has been developed in Python3.5 on the Ubuntu operating system and tested for compatibility with Python2.7. As such, it should work on any Python environment independently of the operating system.

The code is in clear text and can be copied into any user folder. It is *not* meant to be installed in the 'site-packages' folder, as it will make its use much more complicated. The pip installation utility, however, will first try to put all the files exactly there. This should be prevented as follows.


BEST INSTALL: 

- download and copy the package wheel into a user directory, e.g., the root directory $home

- use command
'pip install solprimer-1.0.1-py2.py3-none-any.whl --no-compile -t <target subdirectory>'

The '--no-compile' option avoids the creation of '.pyc' modules, which here would only be a nuisance

The '-t' switch indicates the name of the target directory where the 'solprimer' subdirectory and its subdirectories are copied into, for example, '-t newinstall'


ALTERNATIVE INSTALL: 

extract/unzip the package from .whl into the target directory


===== File structure

'solprimer' contains the main Python scripts 

'solprimer/solprim' contains packages with functions called from the scripts

'solprimer/data-input' is the default directory for input data

'solprimer/data-output' is the default directory for output data

'solprimer/data-TMY' contains the 'Typical Meteorological Year' (TMY) source and processed datasets. Online sources for TMY files are indicated in the documentation primer.

'solprimer/docs' contains the documentation, in particular, 'solprimer.pdf'


All directory names are clearly marked in the Python code and can be changed. Directories can have relative or absolute paths according to the rules of the Python installation and of the operating system.


===== Dependencies

'solprimer' needs for its operation the packages 'numpy', 'pandas', 'xlrd', and 'matplotlib'. These must be separately downloaded from the PyPI repository, in this case the command line is very simple:

'pip install numpy' etc.

Other packages, e.g. 'math', are already part of the standard Python distribution.


===== Script execution

The scripts are executed under the terminal by calling python:

'~/solprimer$ python clearsky_profile.py'

alternatively, they can be opened with the IDLE editor and started with <F5>


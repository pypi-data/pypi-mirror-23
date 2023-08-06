To install on Windows, you need ``cmdstan``, the command line interface to the Stan probabilistic programming language.
In brief,

1. If you do not have git Install Rtools. The default settings are fine. If you aleady have a functioning unix environment, do not add this one to the path.
2. 

.. code::
    
    git clone https://github.com/stan-dev/cmdstan.git
    git checkout v2.16.0
    git submodule update --init --recursive

    set PATH=c:\Rtools\bin;c:\Rtools\mingw_32\bin;%PATH%

    make build


Use Python to download and unzip cmdstan.
Use Python to cd to cmdstan.


     "https://github.com/stan-dev/cmdstan/releases/download/v2.16.0/cmdstan-2.16.0.zip" C:\cmdstan.zip
    Expand-Archive C:\cmdstan.zip -dest C:\

    make all

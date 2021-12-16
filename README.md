# Unzip Recursive

_Unzip .jar, .tgz and .zip files recursively_

## Usage

    ❯ ./unzip-recursive.py help
    Usage:
        unzip-recursive [files|directories]

    Examples:
        unzip-recursive .
        unzip-recursive *.jar *.tar.gz

## Installation

There is a simple `Makefile` to install the script on macOS or Linux. Install by running:

    make install
    unzip-recursive help

Make sure `/usr/local/bin` is in your `$PATH`. Requires Python 2.

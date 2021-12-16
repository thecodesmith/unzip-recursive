# Unzip Recursive

_Unzip .jar, .tgz and .zip files recursively_

## Usage

    ❯ ./unzip-recursive.py help
    Usage:
        unzip-recursive [files|directories]

    Examples:
        unzip-recursive .
        unzip-recursive *.jar *.tar.gz

This extracts each archive file into a directory next to it named `<archive-name>.contents`.
Once extracted, this is useful for things like finding class files in arbitrarily nested jars:

    unzip-recursive my-app.jar
    find . -name JndiLookup.class

## Installation

There is a simple `Makefile` to install the script on macOS or Linux. Install by running:

    make install
    unzip-recursive help

Make sure `/usr/local/bin` is in your `$PATH`. Requires Python 2.

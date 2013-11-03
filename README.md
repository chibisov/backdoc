## About

Backdoc is a tool for backbone-like documentation generation.
Backdoc main goal is to help to generate one page documentation from one markdown source file.  

Resulting html is a solid markup with inline styles.  

After generation you can save result to github-pages or even send html file by email.

* [Demo source](https://raw.github.com/chibisov/backdoc/master/demo/demo.md)
* [Demo result](http://chibisov.github.io/backdoc/demo/demo.html)

## Usage

    $ wget https://raw.github.com/chibisov/backdoc/master/backdoc.py
    $ python backdoc.py --source doc.md > doc.html
    $ # or
    $ echo "# Hello" | python backdoc.py > doc.html

## Usage without installation

    $ echo "# Hello" | python -c "$(curl https://raw.github.com/chibisov/backdoc/master/backdoc.py)" > doc.html

## Input parameters:

* `-s`, `--source` - markdown source file path
* `-t`, `--title` - documentation title header

Example - generate documentation from `~/doc.md` with title `Backbone documentantion` to `~/doc.html` file:

    $ python backdoc.py --source ~/doc.md --title "Backbone documentation" > ~/doc.html

Or using short names:

    $ python backdoc.py -s ~/doc.md -t "Backbone documentation" > ~/doc.html


## Requirements

Python >= 2.7. Not tested under 3.x versions

## Development process

For simplicity sake `backdoc.py` script should be solid python script, without any requirements to install.  
If you add any third-party libraries you should download theme to `src` folder.  

This is the folder, where all source files keeped. After dowload you should add compilation logic to `compile.py`.

Development algorithm:

    1. Write code to src/backdoc.py
    2. Run `python compile.py`
    3. Regenerate demo with `python backdoc.py --source demo/demo.md --title "Backdoc demo" > demo/demo.html`
    4. Commit

How to test:

    $ cd src/
    $ python tests.py

## Changelog

* 2013-11-03:
    - Added title param
    - Added unit tests
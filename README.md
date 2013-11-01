## About

Backdoc is a tool for backbone-like documentation generation.
Backdoc main goal is to help to generate one page documentation from one markdown source file.  

Resulting html is a solid markup with inline styles.  

After generation you can save result to github-pages or even send html file by email.

* [Demo source](https://raw.github.com/chibisov/backdoc/master/demo/demo.md)
* [Demo result](http://chibisov.github.io/backdoc/demo/demo.html)

## Usage

    $ wget https://raw.github.com/chibisov/backdoc/master/backdoc.py
    $ python backdoc.py doc.md > doc.html
    $ # or
    $ echo "# Hello" | python backdoc.py > doc.html

## Usage without installation

    $ echo "# Hello" | python -c "$(curl https://raw.github.com/chibisov/backdoc/master/backdoc.py)" > doc.html


## Development process

For simplicity sake `backdoc.py` script should be solid python script, without any requirements to install.  
If you add any third-party libraries you should download theme to `src` folder.  

There is a folder, where all source files keeped. After dowload you should add compilation logic to `compile.py`.

Development algorithm:

    1 Write code to src/backdoc.py
    2 Run `python compile.py`
    3 Commit
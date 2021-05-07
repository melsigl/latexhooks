# latexhooks

Some latex related hooks for pre-commit.


## Available hooks

The following hooks are currently supported:

### LaTeXIndent

Wrapper around [latexindent](https://github.com/cmhughes/latexindent.pl) for pre-commit.

*latexindent* is a perl script to indent code within environments, commands, after
headings and within special code blocks. It has the ability to align delimiters in
environments and commands, and can modify line breaks.
It is written by Chris Hughes and released under the GPL-3.0 license.

*latexindent* is installed as part of the the `texlive-extra-utils` package. If not
already installed (verify with `latexindent --version`), it can be installed using
`sudo apt install texlive-extra-utils` or the full texlive bundle
`sudo apt install texlive-full`.

The following default argument are used:

`--local .latexindent.yaml --silent --overwrite`

The local settings file `.latexindent.yaml` is the only supported option as it is hardcoded.
Other filenames may be added later.

### ChkTeX

Mirror of [ChkTeX](https://www.nongnu.org/chktex/) for pre-commit.

*ChkTeX* finds typographic errors in LaTeX documents. It is released under the GNU
Public License version 2 or greater.

If not already installed (verify with `chktex --version`), it can be installed using
`sudo apt install chktex` or the full texlive bundle `sudo apt install texlive-full`.

The following default argument are used:

`--quiet --verbosity=0`

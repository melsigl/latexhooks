#!/usr/bin/env python3
import os
import subprocess
import sys

FILE_EXTENSIONS = (".tex", ".sty", ".cls", ".bib")


def _fix_cruft_dir_arg(options):
    # latexindent.pl does not understand dir cli argument is a
    # directory if it does not end with a '/'. It appends the cruft
    # dir name to `indent.log`
    arg = options[-1]
    if not arg.endswith("/"):
        options.append(options.pop() + "/")

    # latexindent.pl expects the cruft dir to exist
    _, _, cruft_dir = arg.rpartition("=")
    os.makedirs(cruft_dir, exist_ok=True)


def main() -> int:
    filenames = []
    options = []
    is_cruft_arg = False
    for arg in sys.argv[1:]:
        if any(map(arg.endswith, FILE_EXTENSIONS)):
            filenames.append(arg)
        else:
            options.append(arg)
            if arg in ("-c", "--cruft"):
                # cruft-dir is the next argument
                is_cruft_arg = True
                continue
            elif arg.startswith("-c=") or arg.startswith("--cruft="):
                # cruft-dir is the part after the equal
                _fix_cruft_dir_arg(options)
            elif is_cruft_arg:
                # cruft dir is the next arg after --cruft or -c
                assert not arg.startswith("-"), f"--cruft must be a dir, given {arg!r}"
                is_cruft_arg = False
                _fix_cruft_dir_arg(options)

    local_settings = os.path.abspath(".latexindent")
    argv = ["--local", local_settings, "--silent", "--overwrite", *options]
    retcode = 0
    for filename in filenames:
        cmd = ["latexindent", *argv, filename]
        retcode |= subprocess.call(cmd)
    return retcode


if __name__ == "__main__":
    exit(main())

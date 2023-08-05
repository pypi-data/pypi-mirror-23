#!/usr/bin/env python
#
# Copyright (C) 2016-2017 Mattia Basaglia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import sys
import argparse
from patsi.document import tree, formatter, loader, _misc, color, palette


def load_dir(path):
    doc = tree.Document(_misc.basename(path))
    for file in os.listdir(path):
        if file in palette.colors16.names:
            doc.layers.append(tree.Layer(
                open(os.path.join(path, file)).read(),
                color.IndexedColor(file, palette.colors16)
            ))
    return doc


def parse_args():
    parser = argparse.ArgumentParser(
        description="Renders an patsi document."
    )

    parser.add_argument(
        "--debug",
        help="Enable debugging",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--input", "-i",
        type=str,
        help="Input file (Use - for standard output)",
        default="-",
    )

    parser.add_argument(
        "--input-format", "-if",
        help="Input format",
        default="auto",
        choices=["auto", "ansi_dir"] + loader.factory.formats(),
    )

    # auto makes sense when -o is defined
    parser.add_argument(
        "--output-format", "-of",
        help="Output format",
        default="auto",
        choices=["auto"] + formatter.factory.formats(),
    )

    parser.add_argument(
        "--ansi",
        help="Ansi output features",
        default=[],
        #choices=formatter.AnsiFormatter.Features.constants_dict().keys(),
        nargs="+",
        dest="ansi_features",
    )

    parser_output = parser.add_mutually_exclusive_group()

    # If -of is defined, default to output_directory/basename(input).output_format
    parser_output.add_argument(
        "--output", "-o",
        help="Output file (Use - for standard output)",
        default="",
    )

    # Defaults to dirname(input)
    parser_output.add_argument(
        "--output-directory", "-d",
        help="Output directory (Used when -o is omitted)",
        default=None,
    )

    return parser.parse_args()


class RenderException(Exception):
    pass


def run(args):
    uses_stdin = args.input == "-" or not args.input

    if args.ansi_features:
        formatter.AnsiFormatter.features = formatter.AnsiFormatter.Features(args.ansi_features)

    # Load the document
    if uses_stdin:
        if args.input_format == "ansi_dir":
            raise RenderException("You must pass a path to open an ANSI directory")
        elif args.input_format == "auto":
            # TODO Avoid this if the factory is set to use libmagic
            raise RenderException("Cannot autodetect format from standard input")
        doc = loader.factory.load(sys.stdin, args.input_format)
    else:
        if args.input_format == "ansi_dir" or \
                (args.input_format == "auto" and os.path.isdir(args.input)):
            doc = load_dir(args.input)
        else:
            hint = None if args.input_format == "auto" else args.input_format
            doc = loader.factory.load(args.input, hint)

    # Get the file name
    if not args.output:
        if args.output_format == "auto":
            raise RenderException("You must give an explicit file name to autodetect the output format")

        if args.output_directory is not None:
            dirname = args.output_directory
        elif uses_stdin:
            dirname = os.getcwd()
        else:
            dirname = os.path.dirname(args.input)

        if uses_stdin:
            basename = "stdin" if not doc.name else doc.name
        else:
            basename = _misc.basename(args.input)

        output_name = os.path.join(dirname, basename) + "." + args.output_format
    else:
        output_name = args.output

    if output_name == "-" and args.output_format == "auto":
        args.output_format = "ansi"

    # Write to output
    out = sys.stdout if output_name == "-" else output_name
    hint = None if args.output_format == "auto" else args.output_format
    formatter.factory.save(doc, out, hint)


def main():
    args = parse_args()
    with ExceptionManager(args.debug):
        run(args)


class ExceptionManager(object):
    def __init__(self, debug=False):
        self.debug = debug

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, traceback):
        if self.debug or exc is None:
            return
        if isinstance(exc, RenderException) or isinstance(exc, IOError):
            self._error(exc)
        elif isinstance(exc, KeyError):
            self._error("Unrecognized format: %s" % exc)
        else:
            self._error("Unexpected error")

    def _error(self, msg):
        sys.stderr.write(str(msg) + "\n")
        sys.exit(1)


main()

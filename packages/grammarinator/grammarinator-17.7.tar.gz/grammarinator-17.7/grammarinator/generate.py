# Copyright (c) 2017 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import codecs
import importlib
import logging
import sys

from argparse import ArgumentParser
from multiprocessing import Pool
from os import cpu_count, getcwd, makedirs
from os.path import abspath, basename, dirname, join, splitext

from .pkgdata import __version__

logger = logging.getLogger('grammarinator')
logging.basicConfig(format='%(message)s')


def generate(unlexer_cls, unparser_cls, rule, max_depth, transformers, out, encoding):
    unparser = unparser_cls(unlexer_cls(max_depth=max_depth))
    start_rule = getattr(unparser, rule)

    if not hasattr(start_rule, 'min_depth'):
        logger.warning('The \'min_depth\' property of %s is not set. Fallback to 0.', rule)
    elif start_rule.min_depth > max_depth:
        logger.error('%s cannot be generated within the given depth (min needed: %d).', rule, start_rule.min_depth)
        return

    root = start_rule()
    for transformer in transformers:
        root = transformer(root)

    with codecs.open(out, 'w', encoding) as f:
        f.write(str(root))


def import_entity(name):
    steps = name.split('.')
    return getattr(importlib.import_module('.'.join(steps[0:-1])), steps[-1])


def execute():
    parser = ArgumentParser(description='Grammarinator: Generate', epilog="""
        The tool acts as a default execution harness for unlexers and unparsers
        created by Grammarinator:Processor.
        """)
    parser.add_argument('-p', '--unparser', required=True, metavar='FILE',
                        help='grammarinator-generated unparser.')
    parser.add_argument('-l', '--unlexer', required=True, metavar='FILE',
                        help='grammarinator-generated unlexer.')
    parser.add_argument('-r', '--rule', metavar='NAME',
                        help='name of the rule to start generation from (default: first parser rule).')
    parser.add_argument('-t', '--transformers', metavar='LIST', nargs='+', default=[],
                        help='list of transformers (in package.module.function format) to postprocess the generated tree.')
    parser.add_argument('-d', '--max-depth', default=float('inf'), type=int, metavar='NUM',
                        help='maximum recursion depth during generation (default: %(default)f).')
    parser.add_argument('-j', '--jobs', default=cpu_count(), type=int, metavar='NUM',
                        help='test generation parallelization level (default: number of cpu cores (%(default)d)).')
    parser.add_argument('-o', '--out', metavar='FILE', default=join(getcwd(), 'test_%d'),
                        help='output file name pattern (default: %(default)s).')
    parser.add_argument('--encoding', metavar='ENC', default='utf-8',
                        help='output file encoding (default: %(default)s).')
    parser.add_argument('--log-level', default='INFO', metavar='LEVEL',
                        help='verbosity level of diagnostic messages (default: %(default)s).')
    parser.add_argument('-n', default=1, type=int, metavar='NUM',
                        help='number of tests to generate (default: %(default)s).')
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()

    logger.setLevel(args.log_level)

    out_dir = dirname(abspath(args.out))
    makedirs(out_dir, exist_ok=True)

    if '%d' not in args.out:
        base, ext = splitext(args.out)
        args.out = '{base}%d{ext}'.format(base=base, ext=ext) if ext else join(base, '%d')

    sys.path.append(dirname(args.unparser))
    sys.path.append(dirname(args.unlexer))
    unlexer = splitext(basename(args.unlexer))[0]
    unparser = splitext(basename(args.unparser))[0]

    unlexer_cls = import_entity('.'.join([unlexer, unlexer]))
    unparser_cls = import_entity('.'.join([unparser, unparser]))
    transformers = [import_entity(transformer) for transformer in args.transformers]

    if args.rule is None:
        args.rule = unparser_cls.default_rule.__name__

    if args.n > 1 and args.jobs > 1:
        with Pool(args.jobs) as pool:
            pool.starmap(generate, [(unlexer_cls, unparser_cls, args.rule, args.max_depth, transformers, args.out % i, args.encoding) for i in range(args.n)])
    else:
        for i in range(args.n):
            generate(unlexer_cls, unparser_cls, args.rule, args.max_depth, transformers, args.out % i, args.encoding)


if __name__ == '__main__':
    execute()

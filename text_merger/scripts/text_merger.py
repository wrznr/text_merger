# -*- coding: utf-8 -*-
from __future__ import absolute_import

import click

from text_merger import utils
from text_merger import Dictionary
from text_merger import Merger

@click.command()
@click.option('--text', '-t', 'left', type=click.File('r'), help='Text file 1', required=True)
@click.option('--Text', '-T', 'right', type=click.File('r'), help='Text file 2', required=True)
@click.option('--dictionary', '-d', type=click.File('r'), help="Gold dictionary", required=True)
def cli(left, right, dictionary):

    #
    # Collect lines
    #
    lines = utils.lines(left)
    Lines = utils.lines(right)

    #
    # perform diff
    #
    gold = Dictionary(dictionary)
    merger = Merger(gold)

    length = min(len(lines), len(Lines))
    for k in range(0,length):
        text = lines[k]
        Text = Lines[k]

        merged_line = merger.merge(text,Text)
        click.echo(merged_line)

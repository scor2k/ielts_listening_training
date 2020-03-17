#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import click
from datetime import datetime

@click.group()
def cli():
    """IELTS Listening Training"""

@cli.command(name="test")
def test():
    """Show test and exit."""

    print ("Hello world!")
    


if __name__ == "__main__":
    cli()

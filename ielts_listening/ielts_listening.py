#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import click
from datetime import datetime
from google_speech import Speech
from random import randrange
from time import sleep

@click.group()
def cli():
    """IELTS Listening Training"""

@cli.command(name="digits")
@click.option("--amount", type=int, help="How many numbers you wanna check", required=True)
@click.option("--max", help="The max number you wanna listen.", default=2500 )
def test_digits(amount, max):
    """Show and check digits."""

    lang = "en"
    result = 0

    for idx in range(amount) :
        sleep(0.5)
        print ("~"*10)
        rnd = randrange(0, max)
        text = f"{rnd}"
        Speech(text, lang).play()

        test = input("Your answer: ")

        if test == text :
            result += 1
            print ("You are right.")
        else :
            print (f"The right answer is: {rnd}")
    
    print ("Result:")
    print (f" {amount} - the number of questions")
    print (f" {result} - the number of RIGHT answers")


if __name__ == "__main__":
    cli()

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import click
import datetime
from google_speech import Speech
from random import randrange
from time import sleep


@click.group()
def cli():
    """IELTS Listening Training"""


@cli.command(name="weekdays")
@click.option("--amount", type=int, help="How many weekdays you wanna check", required=True)
def test_weekdays(amount):
    """Test your knowledge about weekdays"""
    lang = "en"
    result = 0
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for idx in range(amount):
        sleep(0.8)
        print("~" * 10)

        rnd = randrange(0,len(weekdays))
        text = weekdays[rnd]

        Speech(text, lang).play()

        test = input("Your answer (Weekday): ")

        if test == text:
            result += 1
            print("You are right.")
        else:
            print(f"The right answer is: {text}")
            sleep(2)

    print("Result:")
    print(f" {amount} - the number of questions")
    print(f" {result} - the number of RIGHT answers")




@cli.command(name="dates")
@click.option("--amount", type=int, help="How many dates you wanna check", required=True)
@click.option("--weekday", is_flag=True, help="Ask for weekday")
def test_dates(amount, weekday):
    """Test your knowledge about dates"""
    lang = "en"
    result = 0

    prev_dates = list()

    start_date = datetime.date(1200, 1, 1)
    end_date = datetime.date(2200, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for idx in range(amount):
        sleep(0.8)
        print("~" * 10)

        random_number_of_days = randrange(days_between_dates)

        while random_number_of_days in prev_dates :
          random_number_of_days = randrange(days_between_dates)
        prev_dates.append(random_number_of_days)

        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        if weekday :
            text = random_date.strftime("%A %B %d")
        else :
            text = random_date.strftime("%B %d")
        
        Speech(text, lang).play()

        if weekday :
            test = input("Your answer (Weekday Month Day): ")
        else :
            test = input("Your answer (Month Day): ")

        if test == text:
            result += 1
            print("You are right.")
        else:
            print(f"The right answer is: {text}")
            sleep(2)

    print("Result:")
    print(f" {amount} - the number of questions")
    print(f" {result} - the number of RIGHT answers")


@cli.command(name="digits")
@click.option(
    "--amount", type=int, help="How many numbers you wanna check", required=True
)
@click.option("--max", help="The max number you wanna listen.", default=2500)
@click.option("--min", help="The min number you wanna listen.", default=0)
def test_digits(amount, max, min):
    """Test your knowledge about digits."""
    prepositions = [
        "on",
        "it",
        "from",
        "to",
        "before",
        "after",
        "around",
        "until",
        "about",
        "over",
        "outside",
        "inside",
        "below",
        "above",
    ]

    lang = "en"
    result = 0

    prev_rnd = list()

    for idx in range(amount):
        sleep(0.8)
        print("~" * 10)
        rnd = randrange(min, max)

        while rnd in prev_rnd :
          rnd = randrange(min, max)
        prev_rnd.append(rnd)


        prep = prepositions[randrange(0, len(prepositions))]
        text = f".{prep} {rnd}"
        Speech(text, lang).play()

        test = input("Your answer (digit only): ")

        if int(test) == int(rnd):
            result += 1
            print("You are right.")
        else:
            print(f"The right answer is: {rnd}")

    print("Result:")
    print(f" {amount} - the number of questions")
    print(f" {result} - the number of RIGHT answers")


if __name__ == "__main__":
    cli()

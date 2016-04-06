#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
survey.py

Created on 2016-04-06
by Mike Zawitkowski
for fun.

This plots the data for the 2015 Data Science Salary,


"""
from __future__ import division, print_function
import logging as log


def main():
    # 30572 intercept
    result = 30572

    # +1395 age (per year of age above 18)
    age = raw_input("Enter your age in years: ")
    age = int(age)
    if age < 18:
        print("You are only {} years old? \n This survey probably doesn't apply.. quitting early.".format(age))
        return
    elif age == 18:
        age = 1
    else:
        age = 34 - 18
    age = age * 1395
    result += age

    # +5911 bargaining skills
    # (times 1 for “poor” skills to 5 for “excellent” skills)
    bargain = raw_input("""How strong are your bargaining skills?\n
                        1 poor
                        2 not good
                        3 neither good nor bad
                        4 good
                        5 excellent
                        Enter a number 1 through 5: """)
    bargain = int(bargain)
    bargain *= 5911
    result += bargain

    # +382 work_week (times # hours in week)
    work_week = raw_input("How many hours do you work in a week?")
    work_week = int(work_week)
    work_week *= 382
    result += work_week

    # -2007 gender=Female
    # TODO: add gender

    # +1759 industry=Software (incl. security, cloud services)
    # -891 industry=Retail / E-Commerce
    # -6336 industry=Education
    # TODO: add this input
    result += 1759

    # +718 company size: 2500+
    # -448 company size: <500
    # TODO: add this input
    compsize = -448
    result += compsize

    # +8606 PhD
    # +851 master’s degree (but no PhD)
    # TODO: add this input

    # +13200 California
    # +10097 Northeast US
    # -3695 UK/Ireland
    # -18353 Europe (except UK/I) -23140 Latin America
    # -30139 Asia
    # TODO: add location input
    loc = 13200
    result += loc

    # +7819 Meetings: 1 - 3 hours / day
    # +9036 Meetings: 4+ hours / day
    # TODO: add this input
    result += 7819

    # +2679 Basic exploratory data analysis: 1 - 4 hours / week
    # TODO: add this input
    result += 2679
    # -4615 Basic exploratory data analysis: 4+ hours / day
    # TODO: add this input
    # +352 Data cleaning::1 - 4 hrs / week
    # TODO: add this input
    result += 352

    # +2287 cloud computing amount: Most or all cloud computing
    # TODO: add this input
    # -2710 cloud computing amount: Not using cloud computing
    # TODO: add this input
    result += 2287

    # +9747 Spark
    # TODO: add this input
    # result += 9747
    # TODO: add this input
    # +6758 D3
    # TODO: add this input
    # +4878 Amazon Elastic MapReduce (EMR)
    # TODO: add this input
    # +3371 Scala
    # TODO: add this input
    # +2309 C++
    # TODO: add this input
    # +1173 Teradata
    # TODO: add this input
    # +625 Hive
    # TODO: add this input
    # -1931 Visual Basic/VBA
    # TODO: add this input

    # +31280 level: Principal
    # TODO: add this input
    # +15642 title: Architect
    # TODO: add this input
    # +3340 title: Data Scientist
    # TODO: add this input
    # +2819 title: Engineer
    # TODO: add this input
    # -3272 title: Developer
    # TODO: add this input
    # -4566 title: Analyst

    print("Your estimated salary is ${:,}".format(result))
    # TODO: pickle the last round of numbers that were entered

if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")

    main()

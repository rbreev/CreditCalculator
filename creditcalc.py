import sys
import argparse
from math import ceil, log


def diff_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    overpayment = 0
    for payment_months in range(1, periods + 1):
        payment = ceil(
            (principal / periods) + nominal_rate * (principal - (principal * (payment_months - 1)) / periods))
        overpayment += payment
        print(f'Month {payment_months}: paid out {payment}')
    print(f'Overpayment = {ceil(overpayment - principal)}')


def annuity_payment(principal, periods, interest):
    nominal_rate = interest / (12 * 100)
    payment = ceil(
        principal * (nominal_rate * pow((1 + nominal_rate), periods)) / (pow((1 + nominal_rate), periods) - 1))
    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {ceil((payment * periods) - principal)}')


def credit_principal(payment, periods, interest):
    nominal_rate = interest / (12 * 100)
    c_principal = payment / ((nominal_rate * pow((1 + nominal_rate), periods))/(
        pow((1 + nominal_rate), periods) - 1))
    print(f'Your credit principal = {round(c_principal)}!')
    print(f'Overpayment = {ceil((payment * periods) - c_principal)}')


def count_of_months(principal, payment, interest):
    nominal_rate = interest / (12 * 100)
    period_count = ceil(log(payment / (payment - nominal_rate * principal), 1 + nominal_rate))
    if period_count < 12:
        print(f'You need {period_count} months to repay this credit!')
        print(f'Overpayment = {ceil((payment * period_count) - principal)}')
    elif period_count % 12 == 0:
        print(f'You need {period_count // 12} years to repay this credit!')
        print(f'Overpayment = {ceil((payment * period_count) - principal)}')
    else:
        print(f'You need {period_count // 12} years and {period_count % 12} months to repay this credit!')
        print(f'Overpayment = {ceil((payment * period_count) - principal)}')


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of payments: 'annuity' or 'diff'")
parser.add_argument("--principal", help="credit principal", type=int)
parser.add_argument("--periods", help="month periods", type=int)
parser.add_argument("--payment", help="monthly payment", type=int)
parser.add_argument("--interest", help="interest rate", type=float)
args = parser.parse_args()


if len(sys.argv) != 5:
    print("Incorrect parameters")
elif args.type == "diff" and not args.payment:
    diff_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity" and not args.payment:
    annuity_payment(args.principal, args.periods, args.interest)
elif args.type == "annuity" and not args.principal:
    credit_principal(args.payment, args.periods, args.interest)
elif args.type == "annuity" and not args.periods:
    count_of_months(args.principal, args.payment, args.interest)
else:
    print("Incorrect parameters")

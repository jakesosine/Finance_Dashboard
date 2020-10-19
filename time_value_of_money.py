# This is to understand the concept and application of time value of money (TMV)

# future_value using quarterly interest
def future_value_quarterly_interest(present_value, annual_interest_rate, years):
    fv = present_value * (1 + (annual_interest_rate / 4))**(years * 4)
    quarterly = annual_interest_rate / 4
    return f"If you invest {present_value}, with an quartery interest rate of {quarterly}%, in {years} years you will have {fv}"


def future_value_annual_interest(present_value, annual_interest_rate, years):
    fv = present_value * (1 + annual_interest_rate)**years
    return f"If you invest {present_value}, with an annual interest rate of {annual_interest_rate}%, in {years} years you will have {fv}"


def pv_annual_interest(fv, rate, time_in_years):
    return fv / (1 + rate)**time_in_years


def pv_quarterly_interest(fv, annual_interest_rate, time_in_years):
    return fv / (1 + (annual_interest_rate / 4))**time_in_years


if __name__ == '__main__':
    example1 = future_value_quarterly_interest(2_500, .04, 10)
    print(example1)
    example2 = future_value_annual_interest(2_500, .04, 10)
    print(example2)
    example3 = pv_annual_interest(68_500, .09, 24)
    print(example3)
    test1 = pv_quarterly_interest(8658.738441686897, .03, 24)
    print(test1)

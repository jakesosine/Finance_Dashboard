
# calculating_free_cash_flow

# step 1 Calculate Net Operating Profit After Taxes
def net_operating_profit_after_taxes_NOPAT(earnings_before_interest_and_taxes, tax_rate):
    return earnings_before_interest_and_taxes * (1 - tax_rate)

# step 2 calculate Net Operating Working Capital


def net_operating_working_capital(operating_current_assets, operating_current_liabilities):
    return operating_current_assets - operating_current_liabilities

# step 3 calculate Total net operating capital


def total_net_operating_capital(net_operating_working_capital, net_fixed_assets_with_PlantPropertyEquipment):
    return net_operating_working_capital + net_fixed_assets_with_PlantPropertyEquipment

# step 4 calculate net investment in operating capital


def net_investment_in_operating_capital(total_net_operating_capital_current_year, total_net_operating_capital_last_year):
    return total_net_operating_capital_current_year - total_net_operating_capital_last_year
# step 5 free cash flow


def free_cash_flow(net_operating_profit_after_taxes_NOPAT, net_investment_in_operating_capital):
    return net_operating_profit_after_taxes_NOPAT - net_investment_in_operating_capital


if name == "__main__":

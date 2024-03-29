from IPython.display import clear_output

class real_estate:
    def __init__(self):
         self.values={
             'income':{
                 'rental':0,
                 'misc': 0
             },
             'expenses':{
                 'tax':0,
                 'insurance':0,
                 'utilities':0,
                 'HOA':0,
                 'landscaping':0,
                 'repairs':0,
                 'property management':0,
                 'mortgage':0,
                 'misc':0
             },
             'cashflow':{
                 'total income(monthly)':0,
                 'total expenses(monthly)':0,
                 'total cashflow':0
             },
             'cash on cash':{
                 'down payment':0,
                 'closing cost':0,
                 'rehab budget':0,
                 'total investment':0
             }
         }
  
    def add_income(self):
        clear_output()
        while True:
            prompt_income = input("""Section 1 - Income. Please pay attention to the prompts that follow.
            \nType 'x' at any point exit and return to the main prompt. Press the enter key to continue.\n""" )
            if prompt_income.lower() == "x":
                break
            else:
                prompt_income1 = input("What is your monthly rental income? \n")
                self.values['income']["rental"] = int(prompt_income1)
                prompt_income2 = input("If you have any miscellaneous income (if left blank,default value will be 0)")
                if prompt_income2.lower() == "":
                    pass
                else:
                    self.values['income']["misc"] = int(prompt_income2)
            break
        global monthly_total_income
        monthly_total_income = sum(self.values['income'].values())
        print(f'\n Your  monthly income is ${monthly_total_income}')
        cont = input("Press enter to continue")
                                  
    def add_expenses(self):
        clear_output()
        while True:
            prompt_expense = input("""Section 2 - Expenses. Please pay attention to the prompts that follow.
            \nType 'x' at any point exit and return to the main prompt. Press the enter key to continue.\n""" )
    
            if prompt_expense.lower() == "x":
                break

            else:
                prompt_expense1 = input("What is your monthly tax expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense1.lower() == "":
                    pass
                elif prompt_expense1.lower() == "x":
                    break
                else:
                    self.values['expenses']["tax"] = int(prompt_expense1)

                prompt_expense2 = input("What is your monthly insurance expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense2.lower() == "":
                    pass
                elif prompt_expense2.lower() == "x":
                    break
                else:
                    self.values['expenses']["insurance"] = int(prompt_expense2)
                
                prompt_expense3 = input("What is your monthly utilities expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense3.lower() == "":
                    pass
                elif prompt_expense3.lower() == "x":
                    break
                else:
                    self.values['expenses']["utilities"] = int(prompt_expense3)

                prompt_expense4 = input("What is your monthly HOA expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense4.lower() == "":
                    pass
                elif prompt_expense4.lower() == "x":
                    break
                else:
                    self.values['expenses']["HOA"] = int(prompt_expense4)

                prompt_expense5 = input("What is your monthly landscaping expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense5.lower() == "":
                    pass
                elif prompt_expense5.lower() == "x":
                    break
                else:
                    self.values['expenses']["landscaping"] = int(prompt_expense5)

                prompt_expense6 = input("What is your monthly property management expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense6.lower() == "":
                    pass
                elif prompt_expense6.lower() == "x":
                    break
                else:
                    self.values['expenses']["property management"] = int(prompt_expense6)

                prompt_expense7 = input("What is your monthly mortgage expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense7.lower() == "":
                    pass
                elif prompt_expense7.lower() == "x":
                    break
                else:
                    self.values['expenses']["mortgage"] = int(prompt_expense7)

                prompt_expense8 = input("What is your monthly repair expense in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense8.lower() == "":
                    pass
                elif prompt_expense8.lower() == "x":
                    break
                else:
                    self.values['expenses']["repairs"] = int(prompt_expense8)

                prompt_expense9 = input("What is your monthly expense on any other miscellanious items in US Dollars? (if left blank,default value will be 0)\n")
                if prompt_expense9.lower() == "":
                    pass
                elif prompt_expense9.lower() == "x":
                    break
                else:
                    self.values['expenses']["misc"] = int(prompt_expense9)

            break
        global monthly_total_expenses
        monthly_total_expenses = sum(self.values['expenses'].values())
        print(f'Your  monthly expense is ${monthly_total_expenses}')
        cont = input("Press enter to continue")
            
    def cashflowcalc(self):
        clear_output()
        global monthly_total_cashflow
        monthly_total_cashflow = monthly_total_income - monthly_total_expenses
        print(f'Your monthly total cashflow =  monthly total income({monthly_total_income}) - monthly total expenses ({monthly_total_expenses}) = $ {monthly_total_cashflow} ')
        global annual_total_cashflow
        annual_total_cashflow = monthly_total_cashflow*12
        print(f'Your annual total cashflow is ${annual_total_cashflow}')
        cont = input("Press enter to continue")

    def add_cash_on_cash(self):
        clear_output()
        while True:
            prompt_cash_on_cash= input("""Section 3 - Cash on Cash. Please pay attention to the prompts that follow.
            \nType 'x' at any point exit and return to the main prompt. Press the enter key to continue.\n""" )

            if prompt_cash_on_cash.lower() == "x":
                break

            else:
                prompt_cash_on_cash1 = input("What was your down payment? (if left blank,default value will be 0\n)")
                if prompt_cash_on_cash1.lower() == "":
                    pass
                elif prompt_cash_on_cash1.lower() == "x":
                    break
                else:
                    self.values['cash on cash']["down payment"] = int(prompt_cash_on_cash1)

                prompt_cash_on_cash2 = input("What was your closing cost? (if left blank,default value will be 0\n)")
                if prompt_cash_on_cash2.lower() == "":
                    pass
                elif prompt_cash_on_cash2.lower() == "x":
                    break
                else:
                    self.values['cash on cash']["closing cost"] = int(prompt_cash_on_cash2)

                prompt_cash_on_cash3 = input("What was your rehab budget? (if left blank,default value will be 0\n)")
                if prompt_cash_on_cash3.lower() == "":
                    pass
                elif prompt_cash_on_cash3.lower() == "x":
                    break
                else:
                    self.values['cash on cash']["rehab budget"] = int(prompt_cash_on_cash3)
            break
        global total_investment
        total_investment= sum(self.values['cash on cash'].values())
        print(f'Your  total investment is ${total_investment}')
        cont = input("Continue?")

    def ROI_ratio(self):
        ROI= annual_total_cashflow/total_investment *100
        print(f'\n------------------------------------------------------------------\n Your ROI based on the responses you entered is {ROI} %\n------------------------------------------------------------------\n')
        print(f'monthly total income: ${monthly_total_income}\nmonthly total expenses: ${monthly_total_expenses}\nmonthly total cashflow: ${monthly_total_cashflow}\nannual total cashflow: ${annual_total_cashflow}\ntotal investment: ${total_investment}\n')
        

                

def calc():
    
    Death_Star = real_estate()
    active=True

    while active:
        prompt=input("This is the ROI calculator. Please read and answer the series of questions that follows in order to calculate your ROI.\nEnter 'x' anytime to quit. Press Enter to continue.\n")

        if prompt.lower() == 'x':
            print("Thanks for using the ROI calculator")
            active = False

        else: 
            Death_Star.add_income()
            Death_Star.add_expenses()
            Death_Star.cashflowcalc()
            Death_Star.add_cash_on_cash()
            Death_Star.ROI_ratio()
            print("Thanks for using the ROI calculator")
            active = False

calc()
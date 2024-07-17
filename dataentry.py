from datetime import datetime

date_format = "%m-%d-%Y"
CATEGORIES = {"I" : "Income", "E": "Expense"}

def get_date(prompt, allow_default = False):
    datestr = input(prompt)
    if allow_default and not datestr:
        return datetime.today().strftime(date_format)
    else:
        try:
            valid_date = datetime.strptime(datestr,date_format)
            return valid_date.strftime(date_format)
        except ValueError:
            print("Please enter a valid date in correct format - 'mm-dd-yyyy'  ")
            return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Please enter an amount :  "))
        if amount <= 0:
            raise ValueError("Amount must be non negative and non zero! ")
        return amount
    except Exception as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category : 'I' for Income or 'E' for Expense :  ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid Category: Please enter a valid category : 'I' for Income or 'E' for Expense :  ")
    return get_category()

def get_description():
    return input("Enter a Description (optional): ")
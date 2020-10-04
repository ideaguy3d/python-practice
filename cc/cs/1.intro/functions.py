def loading_screen():
    print("This page is loading...")


loading_screen()


def mult_two_add_three(number):
    print(number * 2 + 3)


# Call mult_two_add_three() here:
mult_two_add_three(0)


def mult_x_add_y(number, x, y):
    print(number * x + y)


mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)


# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
    print("Creating a " + title + " with " + str(row_count) + " rows")


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")

create_spreadsheet("Applications", 10)


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)

dads_age = calculate_age(2049, 1953)

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)
print(calculate_age(70))
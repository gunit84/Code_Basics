#!python3

"""Learning Functions... """

__author__ = "Gavin Jones"

"""

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

# Tom's total expense list
total = 0
for item in tom_exp_list:
    total += item
print("Tom's total expenses: {}".format(total))

# Joes total expense list
total = 0
for item in joe_exp_list:
    total += item
print("Joe's total expenses: {}".format(total))
"""

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]


def toms_expense_list(exp):
    total = 0
    for item in exp:
        total += item
    return "Tom's total expenses {}".format(total)


def joes_expense_list(exp):
    total = 0
    for item in exp:
        total += item
    return "Tom's total expenses {}".format(total)

#  Run the function MANUALLY
# print(toms_expense_list(tom_exp_list))
# print(joes_expense_list(joe_exp_list))


# Another way to call the Function
toms_total = toms_expense_list(tom_exp_list)
joes_total = joes_expense_list(joe_exp_list)

# Run the function now
print(toms_total)
print(joes_total)


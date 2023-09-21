from kanren import var,membero
from kanren.core import lall,eq,run

# declare the variable person
person = var()

# Define all the rules using lall. The first rule is that there are four person:
rules = lall(
# There are 4 persons
(eq, (var(), var(), var(), var()), person),

# Steve has a blue car:
(membero, ('Steve', var(), 'blue', var()), person),

# Person who owns a cat lives in Canada
(membero, (var(), 'cat', var(), 'Canada'), person),

# Matthew lives in the USA
(membero, ('Matthew', var(), var(), 'USA'), person),

# The person with a black car lives in Australia
(membero, (var(), var(), 'black', 'Australia'), person),

# Jack has a cat
(membero, ('Jack', 'cat', var(), var()), person),
# Alfred lives in Australia
(membero, ('Alfred', var(), var(), 'Australia'), person),

# Person who has a dog lives in France
(membero, (var(), 'dog', var(), 'France'), person),

# Who has a rabbit?
(membero, (var(), 'rabbit', var(), var()), person)
)

solutions = run(0, person, rules)
output = [house for house in solutions[0] if 'rabbit' in house][0][0]

# Print the output
print('\n' + output + ' is the owner of the rabbit')

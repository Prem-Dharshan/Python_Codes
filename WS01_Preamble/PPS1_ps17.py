# 17) The US Census Bureau projects population based on the following assumptions.
# i) One birth every 7 seconds
# ii) One death every 13 seconds
# iii) One new immigrant every 45 seconds
# Write a program to display the population of the next year. Assume the current population
# is 312032486 and one year has 365 days.

pop = 312032486
secs = 365*24*60*60
print(f"The population in the next year is {pop + secs//7 - secs//13 + secs//5}.")
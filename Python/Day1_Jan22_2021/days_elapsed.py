"""
PROBLEM:
Given a start date and end date, find the number of days between them.
Using datetime module in python.
"""


from datetime import date, datetime, timedelta
print("### PROVIDE DATE IN THIS FORMAT :: YYYY-MM-DD")
# using date.fromisoformat()
start_date = date.fromisoformat(input("Start date: "))
end_date = date.fromisoformat(input("End date: "))

# #OPTIONAL :: using datetime.strptime()
# start_date = datetime.strptime(input("Start date: "),"%Y-%m-%d")
# end_date = datetime.strptime(input("End date: "),"%Y-%m-%d")

days_elapsed = end_date - start_date
print(days_elapsed.days)
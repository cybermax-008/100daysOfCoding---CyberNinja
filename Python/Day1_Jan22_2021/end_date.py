"""
PROBLEM:
Given a start date and no of days before or after, find the end date.
"""

from datetime import date, timedelta
print("### PROVIDE DATE IN THIS FORMAT :: YYYY-MM-DD")
# using date.fromisoformat()
start_date = date.fromisoformat(input("Start date: "))

# #OPTIONAL :: using datetime.strptime()
# start_date = datetime.strptime(input("Start date: "),"%Y-%m-%d")

days_elapsed = int(input("No of days from(+) or before(-) start date: "))

end_date = start_date + timedelta(days=days_elapsed)
print(end_date)
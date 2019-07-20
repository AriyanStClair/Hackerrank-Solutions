# Problem: 
# Your local library needs your help! Given the expected and actual return dates for a library book, 
#create a program that calculates the fine (if any). The fee structure is as follows:

#If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)

#If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, 
#fine = 15 x number of days late

#If the book is returned after the expected return month but still within the same calendar year as the expected return date, the 
# fine = 500 x the number of months late

#If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.

# reading user input
return_date = input().split()
due_date = input().split()
fine = 0

return_date_day = return_date[0]
return_date_month = return_date[1]
return_date_year = return_date[2]

due_date_day = due_date[0]
due_date_month = due_date[1]
due_date_year = due_date[2]

if return_date_year == due_date_year: # if return is in same year 
    if return_date_month == due_date_month: # if return is in same month
        if int(return_date_day) <=  int(due_date_day): # if returned on due date
            fine = 0
        else: 
            fine = 15 * (int(return_date_day) - int(due_date_day))
    elif int(return_date_month) <=  int(due_date_month): # if returned months in advance
            fine = 0
    else: # same year, different month
        fine = 500 * (int(return_date_month) - int(due_date_month))

else: # if it isn't the same year 
    if int(return_date_year) <=  int(due_date_year): # if previous year 
        fine = 0
    else: # if returned years later
        fine = 10000


print(fine)




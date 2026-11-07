student_name = input("Student name: ")
daily_transport_cost = float(input("Daily transport cost: "))
daily_feeding_cost = float(input("Daily feeding cost: "))
number_of_days_on_campus = int(input("Number of days on campus: "))
other_expenses_for_the_week = float(input("Other expenses for the week: "))


transport_total = daily_transport_cost * number_of_days_on_campus
feeding_total = daily_feeding_cost * number_of_days_on_campus
weekly_total = transport_total + feeding_total + other_expenses_for_the_week


print(f"Student Name: {student_name}")
print(f"transport total: NGN {transport_total:.2F}")
print(f"feeding total: NGN {feeding_total: .2F}")
print(f"other expenses: NGN {other_expenses_for_the_week : .2F}")
print(f"weekly total: NGN {weekly_total: .2F}")




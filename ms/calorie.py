date_time = input("Today's date?")
breakfast_calories = input('Breakfast calories?')
lunch_calories = input('Lunch calories?')
dinner_calories = input('Dinner calories?')
snack_calories = input('Snack calories?')
print('Calorie content for '+str(date_time)+': ' +
      str(breakfast_calories + lunch_calories + dinner_calories + snack_calories))

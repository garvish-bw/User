from datetime import datetime, timedelta

class BirthdayCalculator:
    def __init__(self, birthday):
        self.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
    
    def calculate_age(self):
        today = datetime.today().date()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age
    
    def calculate_time_until_next_birthday(self):
        today = datetime.today().date()
        next_birthday = datetime(today.year, self.birthday.month, self.birthday.day).date()

        if next_birthday < today:
            next_birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day).date()

        time_until_next_birthday = next_birthday - today
        days = time_until_next_birthday.days
        hours, remainder = divmod(time_until_next_birthday.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return days, hours, minutes, seconds

# Example usage:
birthday = input("Enter your birthday (YYYY-MM-DD): ")
calculator = BirthdayCalculator(birthday)

age = calculator.calculate_age()
days, hours, minutes, seconds = calculator.calculate_time_until_next_birthday()

print("Age:", age)
print("Time until next birthday: {} days, {} hours, {} minutes, {} seconds".format(days, hours, minutes, seconds))

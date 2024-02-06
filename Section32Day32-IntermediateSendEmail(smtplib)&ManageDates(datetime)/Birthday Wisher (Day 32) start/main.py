# import smtplib
#
# my_email = "rangelrob@gmail.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection: connection.starttls() connection.login(user=my_email,
# password=password) connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com",
# msg="Subject:Hello\n\nThis is the " "body of my email") import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year=1981, month=4, day=30)
# print(date_of_birth)
#
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "email"
# MY_PASSWORD = "pw"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 7:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Monday Motivation\n\n{quote}")



import pandas
import datetime as dt
import random
import smtplib
##################### Normal Starting Project ######################
MY_EMAIL = "najlla.meraj@gmail.com"
MY_PASSWORD = "Najllameraj1996$"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_PASSWORD,
            to_addrs= birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )








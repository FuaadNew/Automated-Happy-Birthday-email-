##################### Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib


my_email = "environ@gmail.com"
password = "aggimpjikkbiiqtc"


now= dt.datetime.now()
df = pandas.read_csv('birthdays.csv')
print(df)
print(now.day)
print(now.month)
newindex= random.randint(1,3)
for index, row in df.iterrows():
    if row["day"] == now.day and row["month"] ==now.month:
        name = row["name"]
        email= row["email"]
        print("yay")
        with open(f"letter_templates/letter_{newindex}.txt", "r") as letter:
            readletter= letter.read()
            newletter= readletter.replace("[NAME]", f"{name}")
            print(newletter)
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{email}",
                                msg=f"Subject:Happy Birthday!\n\n {newletter}")



import random
import pandas
import datetime as dt
import smtplib

# ----------- CONSTANTS ----------- #

BIRTHDAYS = "birthdays.csv"
LETTERS = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
SENDER_EMAIL = "tohirjon060821@gmail.com"
PASSWORD = "rbaz qcsh kuab crot"

# ----------- TODAY'S BIRTHDAYS ----------- #


def today_birthdays():
    """
    Retrieves today's birthdays if there is any
    :return: map object with pandas tuple objects
    """
    birthdays_data = pandas.read_csv("birthdays.csv")
    now = dt.datetime.now()
    month = now.month
    day = now.day

    todays_birthdays = birthdays_data[(birthdays_data["month"] == month) & (birthdays_data["day"] == day)]

    return todays_birthdays.itertuples(index=False)


# ----------- BIRTHDAY LETTER ----------- #


def write_letter(name):
    """
    Writes a letter for a specific person
    :param name: recipient name
    :return: letter with a specific name and subject for the email
    """
    random_letter = random.choice(LETTERS)
    with open(random_letter) as letter_file:
        raw_letter = letter_file.read()
        letter = raw_letter.replace("[NAME]", name)
        letter = "Subject: Happy Birthday\n\n" + letter
        return letter


# ----------- SEND BIRTHDAY EMAILS ----------- #

for birthday_person in today_birthdays():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=birthday_person.email,
                            msg=write_letter(birthday_person.name)
                            )

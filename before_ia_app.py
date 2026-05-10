"""

Name: Hernan Ramoz

Course: ADD 100

Project: Finance Flow

Description:

This web app helps users understand their monthly finances.

It asks for income, expenses, and debt payments.

Then it calculates how much money is left.

"""

import streamlit as st

# Global Constants

WELCOME_MESSAGE = "Welcome to Finance Flow"

PROGRAM_MESSAGE = "This app helps you understand your monthly finances."

ERROR_MESSAGE = "Please enter valid numbers."

def calculate_balance(income, expenses, debt):

    balance = income - expenses - debt

    return balance

def show_summary(balance):

    st.subheader("Financial Summary")

    st.write("Money left after expenses and debt:", balance)

    if balance < 0:

        st.warning("You are spending more than you earn.")

    elif balance == 0:

        st.info("You have no money left this month.")

    else:

        st.success("Good job! You still have money left.")

def save_report(balance):

    file = open("finance_report.txt", "w")

    file.write("Financial Report\n")

    file.write("--------------------\n")

    file.write("Balance: " + str(balance) + "\n")

    if balance < 0:

        file.write("Warning: You are spending more than you earn.\n")

    elif balance == 0:

        file.write("You have no money left this month.\n")

    else:

        file.write("Good job! You still have money left.\n")

    file.close()

def main():

    st.title(WELCOME_MESSAGE)

    st.write(PROGRAM_MESSAGE)

    income = st.number_input("Enter your monthly income:", min_value=0.0)

    expenses = st.number_input("Enter your monthly expenses:", min_value=0.0)

    debt = st.number_input("Enter your monthly debt payments:", min_value=0.0)

    if st.button("Calculate"):

        balance = calculate_balance(income, expenses, debt)

        show_summary(balance)

        save_report(balance)

        st.write("Report saved to finance_report.txt")

main()
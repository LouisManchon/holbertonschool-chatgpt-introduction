#!/usr/bin/env python3

class Checkbook:
    """
    A simple checkbook management system that allows deposits, withdrawals,
    and checking the current balance.
    """

    def __init__(self):
        """
        Initialize the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add the specified amount to the balance.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtract the specified amount from the balance if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw. Must be positive.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Entry point for the checkbook application. Provides a simple command-line interface.
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()


import json
import random
import string
from pathlib import Path


class Bank:
    DATABASE = "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ==============================
    # LOAD DATA
    # ==============================

    def load_data(self):
        try:
            if Path(self.DATABASE).exists():

                with open(self.DATABASE, "r") as file:
                    return json.load(file)

            return []

        except (json.JSONDecodeError, OSError):
            return []

    # ==============================
    # SAVE DATA
    # ==============================

    def save_data(self):

        try:

            with open(self.DATABASE, "w") as file:
                json.dump(
                    self.data,
                    file,
                    indent=4
                )

        except OSError as error:

            raise Exception(
                f"Unable to save data: {error}"
            )

    # ==============================
    # GENERATE ACCOUNT NUMBER
    # ==============================

    def generate_account_number(self):

        while True:

            letters = "".join(
                random.choices(
                    string.ascii_uppercase,
                    k=3
                )
            )

            numbers = "".join(
                random.choices(
                    string.digits,
                    k=3
                )
            )

            special = random.choice(
                "!@#$%^&*"
            )

            account_number = (
                letters +
                numbers +
                special
            )

            if not any(
                account["accountNo."] == account_number
                for account in self.data
            ):
                return account_number

    # ==============================
    # CREATE ACCOUNT
    # ==============================

    def create_account(
        self,
        name,
        age,
        email,
        pin
    ):

        if not name.strip():

            return False, "Name cannot be empty."

        if age < 18:

            return False, (
                "You must be at least 18 years old."
            )

        if not email.strip():

            return False, (
                "Email cannot be empty."
            )

        pin = str(pin)

        if not pin.isdigit() or len(pin) != 4:

            return False, (
                "PIN must contain exactly 4 digits."
            )

        account = {

            "name": name.strip(),

            "age": age,

            "email": email.strip(),

            "pin": int(pin),

            "accountNo.": (
                self.generate_account_number()
            ),

            "balance": 0
        }

        self.data.append(account)

        self.save_data()

        return True, account

    # ==============================
    # FIND ACCOUNT
    # ==============================

    def find_account(
        self,
        account_number,
        pin
    ):

        try:

            pin = int(pin)

        except (ValueError, TypeError):

            return None

        for account in self.data:

            if (
                account["accountNo."] ==
                account_number
                and
                account["pin"] == pin
            ):

                return account

        return None

    # ==============================
    # READ ACCOUNT
    # ==============================

    def get_account(
        self,
        account_number,
        pin
    ):

        account = self.find_account(
            account_number,
            pin
        )

        if account is None:

            return (
                False,
                "Invalid account number or PIN."
            )

        return True, account

    # ==============================
    # DEPOSIT
    # ==============================

    def deposit(
        self,
        account_number,
        pin,
        amount
    ):

        account = self.find_account(
            account_number,
            pin
        )

        if account is None:

            return (
                False,
                "Invalid account number or PIN."
            )

        if amount <= 0:

            return (
                False,
                "Deposit amount must be greater than 0."
            )

        if amount > 10000:

            return (
                False,
                "Maximum deposit is ₹10,000."
            )

        account["balance"] += amount

        self.save_data()

        return True, account["balance"]

    # ==============================
    # WITHDRAW
    # ==============================

    def withdraw(
        self,
        account_number,
        pin,
        amount
    ):

        account = self.find_account(
            account_number,
            pin
        )

        if account is None:

            return (
                False,
                "Invalid account number or PIN."
            )

        if amount <= 0:

            return (
                False,
                "Withdrawal amount must be greater than 0."
            )

        if amount > account["balance"]:

            return (
                False,
                "Insufficient balance."
            )

        account["balance"] -= amount

        self.save_data()

        return True, account["balance"]

    # ==============================
    # UPDATE ACCOUNT
    # ==============================

    def update_account(
        self,
        account_number,
        pin,
        name=None,
        email=None,
        new_pin=None
    ):

        account = self.find_account(
            account_number,
            pin
        )

        if account is None:

            return (
                False,
                "Invalid account number or PIN."
            )

        if name:

            account["name"] = name.strip()

        if email:

            account["email"] = email.strip()

        if new_pin:

            new_pin = str(new_pin)

            if (
                not new_pin.isdigit()
                or len(new_pin) != 4
            ):

                return (
                    False,
                    "New PIN must contain exactly 4 digits."
                )

            account["pin"] = int(new_pin)

        self.save_data()

        return True, account

    # ==============================
    # DELETE ACCOUNT
    # ==============================

    def delete_account(
        self,
        account_number,
        pin
    ):

        account = self.find_account(
            account_number,
            pin
        )

        if account is None:

            return (
                False,
                "Invalid account number or PIN."
            )

        self.data.remove(account)

        self.save_data()

        return (
            True,
            "Account deleted successfully."
        )
# Defineerime algväärtused
class Kalkulaator():
    def __init__(self):
        self.order_total = 0
        self.order_amount = 0 
        self.order_ppi = 0
        self.discount_percent = 0
        self.tax_total = 0
        self.tax_percent = 0
        self.state_code = "EE"

# Kusime tarbijalt mis koguses ta soovib tellida,kui palju yks toode maksab ja mis osariigist/riigist tellija tellib toote.

    def main_order(self): 
        self.order_amount = int(input("How many items do you order? "))
        if self.order_amount < 1:
            print("You can not order a negative amount of items! ")
        self.order_ppi = float(input("How much does one item cost? "))
        if self.order_ppi < 0:
            print("An item can not cost a negative amount! ")
        self.state_code = str(input("What is your 2-letter state code? "))

        self.order_total = self.order_amount * self.order_ppi

# Hinna abil, mida tellija kirjutas yleval, saame teada allahindluse arvu.

    def discount_rate(self): 
        value = self.order_amount * self.order_ppi
        if value > 1000:
            self.discount_percent = 0.03
        if value > 5000:
            self.discount_percent = 0.05
        if value > 7000:
            self.discount_percent = 0.07
        if value > 10000:
            self.discount_percent = 0.1
        if value > 15000:
            self.discount_percent = 0.15

# Tellija andis teada mis osariigis/riigis ta elab, selle abil saame teada käibemaksu, mis läheb toote summale.

    def state(self):
        state = self.state_code
        if state == "EE":
            self.tax_percent = 0.2
        if state == "UT":
            self.tax_percent = 0.0685
        if state == "NV":
            self.tax_percent = 0.08
        if state == "TX":
            self.tax_percent = 0.0625
        if state == "AL":
            self.tax_percent = 0.04
        if state == "CA":
            self.tax_percent = 0.0825


    def checkout(self):
        self.tax_total = self.order_total * self.tax_percent
        print(f"""
===============================
# Pricing
Order amount: {self.order_amount}
Order price per item: $ {self.order_ppi}
Order value: $ {self.order_amount * self.order_ppi}


# Discount and Tax
Order discount rate: $ {self.order_total * self.discount_percent} ({self.discount_percent}%)
Order tax: $ {self.tax_total} ({self.tax_percent}%)
================================
Total: $ {(self.order_total + self.tax_total) - (self.order_total * self.discount_percent)}

Thank you for the order! :D
        """)
class Category:
    def __init__(self, name):
        self.name = name  # Store the category name
        self.ledger = []  # Initialize ledger as a list
    
    def deposit(self, amount, description=""):
        # Add a positive amount to the ledger
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        # If not enough funds, return False
        if not self.check_funds(amount):
            return False
        # Otherwise, add a negative amount to the ledger
        self.ledger.append({"amount": -amount, "description": description})
        return True
    
    def get_balance(self):
        # Sum of all amounts in the ledger
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, other_category):
        # Transfer between categories if enough funds
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {other_category.name}")
        other_category.deposit(amount, f"Transfer from {self.name}")
        return True
    
    def check_funds(self, amount):
        # True if amount <= current balance
        return amount <= self.get_balance()
    
    def __str__(self):
        # Title line centered with '*'
        title = f"{self.name:*^30}\n"
        items_str = ""
        for entry in self.ledger:
            # Description up to 23 chars
            desc = entry["description"][:23]
            # Amount with 2 decimal places
            amt = f"{entry['amount']:.2f}"
            # Left-align desc (max width 23), right-align amount (width 7)
            items_str += f"{desc:<23}{amt:>7}\n"
        # Final total line
        total_line = f"Total: {self.get_balance():.2f}"
        return title + items_str + total_line


def create_spend_chart(categories):
    """
    Returns a bar chart of the percentage of total withdrawals
    for each category, rounded down to the nearest 10.
    """
    # 1) Calculate total withdrawal per category
    total_spent = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        total_spent.append(spent)
    
    # 2) Compute overall total and percentages
    total_all = sum(total_spent)
    # Each category's percentage (integer, 0..100)
    percentages = [int((s / total_all) * 100) for s in total_spent]
    
    # 3) Build the chart header
    result = "Percentage spent by category\n"
    
    # 4) Loop from 100 down to 0 in steps of 10
    for level in range(100, -1, -10):
        result += f"{str(level).rjust(3)}| "
        for p in percentages:
            if p >= level:
                result += "o  "
            else:
                result += "   "
        result += "\n"
    
    # 5) Horizontal line (two spaces past the final bar = len(categories)*3 + 1)
    result += "    " + "-" * (len(categories)*3 + 1) + "\n"
    
    # 6) Print category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        # Five leading spaces to align with the chart above (3 digits + '| ' = 5)
        result += " " * 5
        for c in categories:
            if i < len(c.name):
                result += c.name[i] + "  "
            else:
                result += "   "
        result += "\n"
    
    # 7) rstrip to remove the final newline
    return result.rstrip("\n")
def deposit(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError
    else:
        balance += amount
        return balance

def withdraw(balance: float, amount: float) -> float:
    if amount <= 0 or amount > balance:
        raise ValueError
    else:
        balance -= amount
        return balance

def show_balance(balance: float) -> str:
    statment = f"Current balance: {balance : 2f}"
    return statment

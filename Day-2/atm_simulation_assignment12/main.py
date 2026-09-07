# 12. ATM Simulation 
# Build an ATM program. 
# Flow: 
# Enter PIN 
# ↓ 
# Validate PIN 
# ↓ 
# Show menu 
# 1. Check balance 
# 2. Withdraw 
# 3. Deposit 
# 4. Change PIN 
# 5. Exit 
# Rules 
# ● Maximum 3 incorrect PIN attempts 
# ● Withdrawal cannot exceed balance 
# ● Withdrawal must be a valid amount 
# ● Deposit must be positive 
# ● PIN must satisfy validation rules 
# Use functions and exceptions properly.

from utils import run_atm

if __name__ == "__main__":
    run_atm()



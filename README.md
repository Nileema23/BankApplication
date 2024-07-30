# BankApplication
This Project was made using Python language. This is a simple Banking Application that performs many common bank transactions that a bank employee or customer might perform on one or more accounts.

Basic Structure
When executed, the program will display a menu with the following choices as follows:
============================================================
What do you want to do?
1. Open an account
2. Get account information and balance
3. Change PIN
4. Deposit money in account
5. Transfer money between accounts
6. Withdraw money from account
7. ATM withdrawal
8. Deposit change
9. Close an account
10. Add monthly interest to all accounts
11. End Program
============================================================
The program will continuously loop and prompt the user to enter the number of the transaction to perform and then perform the transaction. If the user enters ‘11’ the program should end. If the user enters an invalid option, the program display “Invalid choice” and let the user tryagain.
For each menu option, program perform a different transaction as follows:

1. Open an account
For open account, the program prompt the user to enter their first and last name and their social security number:
OPEN ACCOUNT
Enter Account Owner's First Name:George
Enter Account Owner's Last Name:Washington
Enter Account Owner's SSN (9 digits):999741776
Once the above information is entered, a new Account object should be created, and the six fields of the Account object should be populated using the setter methods based on the criteria defined above under the Account class. Any special logic (i.e. to generate a random number) should happen BEFORE calling the setter. Once the account is initialized, the toString() method on the account should be involved to print out the Account fields as follows:
============================================================
Account Number: 75927164
Owner First Name: George
Owner Last Name: Washington
Owner SSN: XXX-XX-1776
PIN: 3198
Balance: $0.00
============================================================
2. Get account information and balance
For ‘Get account information and balance’, the program prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program print the account information and balance formatted as shown below with the dollar sign and cents after the decimal.
Enter account number:75927164
Enter PIN:3198
============================================================
Account Number: 75927164
Owner First Name: George
Owner Last Name: Washington
Owner SSN: XXX-XX-1776
PIN: 3198
Balance: $0.00
============================================================
Then the program returns to the main menu.
3. Change PIN
For ‘Change PIN’, the program prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter a new PIN number twice as show below. If the PIN numbers match, the PIN should be updated in the account and the “PIN updated” message should be displayed.
Enter account number: 95705452
Enter PIN: 3958
Enter new PIN: 1776
Enter new PIN again to confirm: 1776
PIN updated
Then the program returns to the main menu.
4. Deposit money into account
For ‘Deposit money into account’, the program prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter the dollars and cents to deposit as a decimal as shown below. If the amount is less than or equal to 0, print a message that says “Amount cannot be negative. Try again.” Otherwise, convert the amount entered to a long and call the deposit method on the Account. Then the program print the   updated balance of the account.
Enter account number: 37658351
Enter PIN: 4444
Enter amount to deposit in dollars and cents (e.g. 2.57): 5.25
New balance: $5.25
Then the program returns to the main menu.
5. Transfer money between accounts
For ‘Transfer money between accounts’, the program should prompt the user to enter their account number and then the PIN for the account number to transfer from and then the account number and PIN of the account to transfer to. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account numbers are valid and the PINs match the PINs on the accounts, the program should prompt the user to enter the dollars and cents to transfer as a decimal as shown below. If the amount is less than or equal to 0, print a message that says “Amount cannot be negative. Try again.” Otherwise, convert the amount entered to a long and call the withdraw method on the “from” Account and then the deposit method on the “to” Account. Then the program should print the updated balances of both accounts.
Account to Transfer From:
Enter account number: 37658351
Enter PIN: 4444
Account to Transfer To:
Enter account number: 36279555
Enter PIN: 8571
Enter amount to transfer in dollars and cents (e.g. 2.57): 2.50
Transfer Complete
New balance in account:37658351 is:$2.75
New balance in account:36279555 is:$2.50
Then the program returns to the main menu.
6. Withdraw money from an account
For ‘Withdraw money from account’, the program should prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter the dollars and cents to withdraw as a decimal as shown below. If the amount is less than or equal to 0, print a message that says “Amount cannot be negative. Try again.” Otherwise, convert the amount entered to a long and call the withdraw method on the Account. Then the program should print the updated balance of the account.
Enter account number: 35816930
Enter PIN: 2010
Enter amount to Deposit in dollars and cents (e.g. 2.57): 123.45
New balance:$123.45
Then the program returns to the main menu.
7. Make an ATM withdrawal from an account
For ‘Make an ATM withdrawal from an account’, the program should prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter the amount to withdraw in whole dollars as a multiple of $5 as shown below. If the amount is less than 5, greater than 1000, or not divisible by 5, print a message that says “Invalid amount. Try again.” Otherwise, calculate the number of $20 bills, $10 bills and $5 required to equal the amount withdrawn, print the amounts on the screen and then call the withdraw method on the
Account.
Then the program should print the updated balance of the account.
Enter account number: 37658351
Enter PIN: 4444
Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): 135
Number of 20-dollar bills:6
Number of 10-dollar bills:1
Number of 5-dollar bills:1
New balance: $367.75
8. Deposit change into an account
For ‘Deposit change’, the program should prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should prompt the user to enter a String representing a set of coins as shown below.
o ‘P’ represents a penny (1 cent)
o ‘N’ represents a nickel (5 cents)
o ‘D’ represents a dime (10 cents)
o ‘Q’ represents a quarter (25 cents)
o ‘H’ represents a half-dollar (50 cents)
o ‘W’ represents a whole dollar (100 cents)
If any characters are invalid coins (e.g. X), the program should print “Invalid coin: X”. Otherwise, convert the String into the appropriate number of cents to a long and call the deposit method on the Account. Then the program should print the updated balance of the account.
Enter account number: 47322673
Enter PIN: 4919
Deposit coins: QPDNNDXHW
Invalid coin: X
$2.06 in coins deposited into account
New balance: $2.06
In the above example, there are the following:
1 quarter (Q) + 2 dimes (D) + 2 nickels (N) + 1 half-dollar (H) + 1 dollar (W) + 1 penny (P)
= 2.06
The ‘X’ is an invalid coin and is not counted.
Then the program returns to the main menu.
9. Close an account
For ‘Close an account’ the program prompt the user to enter their account number and then the PIN for the account number. If the account number or PIN are invalid then then display invalid pin and prompt the user to enter the choice. If the account number is valid and the PIN matches the PIN on the account, the program should look through all of the Account objects in the Bank. If a matching Account is found, the Bank should remove that Account from its set of accounts by setting it to null
Enter account number: 47322673
Enter PIN: 4919
Account 47322673 closed
If the user tries to find the account afterwards, it should not be found:
Enter account number: 47322673

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

***********Implementation of classes***********
Each option call a method to implement the details of that transaction. That method will call additional methods to fully complete the transaction. 
The class that contains main program is called BankManager, I have utilize at least four additional classes. A class called Account, that represents a single bank account, a class called Bank, that represents the bank and stores all the accounts in the bank, a class called CoinCollector, that represents a coin collecting machine, and a class called BankUtility that provide several helper methods to be used throughout program. Details of these classes are described below:
Bank Manager Class
The BankManager class implement ‘main’ method and start the program from. The BankManager class create an instance of a Bank object when the program runs and use that instance to manage the Accounts in the bank. The BankManager class implement the following methods:
•	‘Main’ method. The main method display the menu and continually loop, performing the transactions, until the user enters 11 to exit the program. If the user enters a number from 1-10, the program should call a method that implements the functionality for that transaction.
•	A method, ‘promptForAccountNumberAndPIN’ that takes one parameter, a Bank object
that represents the bank. The method should prompt the user to enter an account number
and then try to find a matching account with that account number in the bank. If an
account cannot be found, the program should print “Account not found for account
number: 12345678” (assuming the user entered 12345678) and return null. If an account
is found, the program should then prompt the user to enter a PIN. If the PIN entered does
not match the PIN for the account, then the program should print “Invalid PIN” and
return null. If the PIN matches, then the method should return the Account object. This
method will be needed for MOST (but not all) transactions.
CoinCollector class
This class represents a machine that can count change and has one method:
•	A method called ‘parseChange’ that takes one parameter, a String that represents a set of
coins/change. The method must look at each character in the String and calculate the
amount it represents in cents as a ‘long’ and return it. The following characters represent
valid coins:
•	‘P’ represents a penny (1 cent)
•	‘N’ represents a nickel (5 cents)
•	‘D’ represents a dime (10 cents)
•	‘Q’ represents a quarter (25 cents)
•	‘H’ represents a half-dollar (50 cents)
•	‘W’ represents a whole dollar (100 cents)

Account Class
The Account class store the following attributes:
•	Account number – a randomly generated 8-digit integer that cannot start with a 0
•	Owner First Name – a String that contains the first name of the account owner
•	Owner Last Name – a String that contains the last name of the account owner
•	Social Security Number – a String (not an integer) that contains the 9 digits of the account owner’s social security number (Note: do not use real social security numbers –
use 999 or 000 as the first three digits for this program)
•	PIN – a String that represents the account owner’s 4-digit personal identification number
randomly generated upon account creation and may start with one or more zeroes
•	Balance – a number that represents the account balance in cents.
•	The account class implement the following methods:
	A method ‘deposit’ that takes one parameter - an amount to deposit into the account as a‘long’. The method then adds the amount to the account balance and returns a ‘long’representing the new account balance
	A method ‘withdraw’ that takes one parameter - an amount to withdraw from the account as a ‘long’. The method then subtracts the amount from the account balance and returns a ‘long’ representing the new account balance
	A method ‘isValidPIN’ that takes one parameter – A String that represents a PIN. The method then compares the PIN that was passed in against the PIN that is on the account.
	If the PINs match, it returns true, otherwise, it returns false.
	A method ‘toString’ that has no parameters but returns a String that contains the names and values of all of the attributes as follows. This method should NOT print out anything but can be invoked as part of a System.out.println elsewhere.

============================================================
Account Number: 79543812
Owner First Name: George
Owner Last Name: Washington
Owner SSN: XXX-XX-1776
PIN: 3759
Balance: $0.00
============================================================
Bank Class
The Bank class implement the following methods:
•	A method, ‘addAccountToBank’, that takes one parameter, an Account object, to add to
the array of accounts in the Bank. The method should iterate through all the accounts in
the array until it finds an empty/null index. It should then add the account to that index in
the array to represent a new account that was opened and return true to indicate the
account was successfully added. If there is no more room for the Bank to accept any
more accounts (i.e. there are already 100 accounts in the array). The method should print
a message saying, “No more accounts available” and should return false.
•	A method, ‘removeAccountFromBank’, that takes one parameter, an Account object, to
remove from the accounts array. The method should iterate through all the accounts in
the array and try to match the account provided to the accounts in the Bank by the
account number. If the account number of the provided account matches the account
number of the Account in the array, then that index of the array should be marked ‘null’
to indicate that the account is closed and no longer exists.
•	A method, ‘findAccount’ that takes one parameter, an int representing the account
number. The method should iterate through all the accounts in the array and try to match
the account number provided to the accounts in the Bank by the account number. If a
match is found, the Account object should be returned. If an account with the provided
account number does not exist, the method should return ‘null’ to indicate a matching
Account was not found
•	A method, ‘addMonthlyInterest’ that takes one parameter, a ‘double’ representing the percentage of the annual interest rate (e.g. if the rate is 2.5%, the value entered would be 2.5). The method should then iterate through all the accounts in the array and deposit a monthly interest payment into every account. The monthly interest for the account is calculated by taking the current balance and multiplying a monthly interest rate.
BankUtility Class
This class provide several utility methods to use throughout the program:
•	A method isNumeric to determine if a String is a number. If it is a number, it will return true, otherwise, it will return false.
•	A method ‘promptUserForString’ that takes one parameter, a String that represents a
•	prompt to print on the screen (e.g. “Enter your name”). The method should then read a
line of input from the keyboard and return as a String.
•	A method ‘promptUserForPositiveNumber’ that takes one parameter, a String that
represents a prompt to print on the screen (e.g. “Enter a number”). The method should
then read a double from the keyboard. If the number is less than or equal to 0, it should
print a message and say “Amount cannot be negative. Try again” and continue to loop.
If the number is positive, the method should return that number as a double.
•	A method ‘convertFromDollarsToCents’ that takes one parameter, a double that
represents an amount of money in dollars (e.g. 3.57) and converts to a long (e.g. 357) and
returns it.
•	A method ‘generateRandomInteger’ that takes two parameters, an integer representing
the minimum value and an integer representing the maximum value of the range to
generate a random number for and then return the number generated as an int. For
example, if you invoke generateRandomInteger(0,5), the method should return a random
number from 0-5 (including both 0 and 5).


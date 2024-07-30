#import random and math module
import random
import math
#Create class name Bank
class Bank:
	"""docstring for Bank"""
	#Create constructor for class name bank
	def __init__(self):
		self.accounts = {}
		self.MAX_ACC = 100
	#define addAccountToBank()method where we can add account max limit 100 
	def addAccountToBank(self, account):
		if len(self.accounts) >= self.MAX_ACC:
			print("Max Account Exceeded")
			return
		if len(self.accounts) > 0:
			for key, acc in self.accounts.items():
				if key == account.accountNumber:
					print("Account already existed")
					return
		self.accounts[account.accountNumber] = {
			'accountNumber': account.accountNumber,
			'ownerFirstName': account.ownerFirstName,
			'ownerLastName': account.ownerLastName,
			'socialSecurityNumber': account.socialSecurityNumber,
			'pin': account.pin,
			'balance': account.balance,
		}
	# define removeAccountFromBank()method which removes existing account
	def removeAccountFromBank(self, account):
		if len(self.accounts) > 0:
			for key, acc in self.accounts.items():
				if key == account.accountNumber:
					return self.accounts.pop(key)

	#Define findAccount()method which helps in finding existing account
	def findAccount(self, acc_no):
		if len(self.accounts) > 0:
			for key, acc in self.accounts.items():
				if key == acc_no:
					return acc
		return 'null'
	#Define changePIN()method helps with change existing pin
	def changePIN(self, acc_no, new_pin):
		for key, acc in self.accounts.items():
			if key == acc_no:
				acc["pin"] = new_pin
	
	#Define updateAccountOfBank()method helps to update accounts
	def updateAccountOfBank(self, acc_no, field, value):
		for key, acc in self.accounts.items():
			if key == acc_no:
				acc[field] = value
	
	#Define addInterest()method which add interest in available balance
	def addInterest(self, rate):
		for key, acc in self.accounts.items():
			interest = round(((rate/100)*acc["balance"])/12, 2)
			acc["balance"] = acc["balance"] + interest
			print(f"Deposited interest: ${interest} into account number:{acc['accountNumber']}, new balance: ${acc['balance']}")

#Create class name Account
class Account:
	"""docstring for Account"""
	#Define constructor method for class Account
	def __init__(self, accNo, fname, lname, ssn, pin, bal):
		self.__accountNumber = accNo
		self.__ownerFirstName = fname
		self.__ownerLastName = lname
		self.__socialSecurityNumber = ssn
		self.__pin = pin
		self.__balance = bal
	
	#Define getter and setter methods here
	def getAccountNumber(self):
		return self.__accountNumber

	def setAccountNumber(self, an):
		self.__accountNumber = an

	def getOwnerFirstName(self):
		return self.__ownerFirstName

	def setOwnerFirstName(self, fname):
		self.__ownerFirstName = fname

	def getOwnerLastName(self):
		return self.__ownerLastName

	def setOwnerLastName(self, lname):
		self.__ownerLastName = lname

	def getSocialSecurityNumber(self):
		return self.__socialSecurityNumber

	def setSocialSecurityNumber(self, ssn):
		self.__socialSecurityNumber = ssn

	def getPin(self):
		return self.__pin

	def setPin(self, pin):
		self.__pin = pin

	def getBalance(self):
		return self.__balance

	def setBalance(self, bal):
		self.__balance = bal

	accountNumber = property(getAccountNumber, setAccountNumber)
	ownerFirstName = property(getOwnerFirstName, setOwnerFirstName)
	ownerLastName = property(getOwnerLastName, setOwnerLastName)
	socialSecurityNumber = property(getSocialSecurityNumber, setSocialSecurityNumber)
	pin = property(getPin, setPin)
	balance = property(getBalance, setBalance)
	
	#Define deposit()method which adds money to account
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance
	
	#Define withdraw()method helps to withdraw money from account
	def withdraw(self, amount):
		if self.balance < amount:
			return self.balance
		self.balance = self.balance - amount
		return self.balance
	
	#Define isValidPIN()method helps to find if entered pin is valid or not. 
	def isValidPIN(self, pin):
		if len(pin) == 4 and BankUtility().isNumeric(pin):
			return True
		else:
			return False
	
	#Define toString()method
	def toString(self):
		print("Account Number: ", self.accountNumber)
		print("Owner First Name: ", self.ownerFirstName)
		print("Owner Last Name: ", self.ownerLastName)
		print("Owner SSN: ", self.socialSecurityNumber)
		print("PIN: ", self.pin)
		print("Balance: $", self.balance)

#Create class name CoinCollector
class CoinCollector:
	"""docstring for CoinCollector"""
	#Define constructor for CoinCollector
	def __init__(self):
		super().__init__()
		pass
	
	#Define parseChange()method here
	def parseChange(self, coins):
		amount = 0
		for coin in coins:
			if coin == 'P':
				amount = amount + 1
			elif coin == 'N':
				amount = amount + 5
			elif coin == 'D':
				amount = amount + 10
			elif coin == 'Q':
				amount = amount + 25
			elif coin == 'H':
				amount = amount + 50
			elif coin == 'W':
				amount = amount + 100
			else:
				print("Invalid coin: ",coin)
		amount = amount/100
		return amount
#Create class name BankUtility
class BankUtility:
	"""docstring for BankUtility"""
	def __init__(self):# define constructor for class BankUtility 
		super().__init__()
		pass
	
	#Define isNumeric()method
	def isNumeric(self, value):
		return value.isnumeric()
	
	#Define promptUserForString()method
	def promptUserForString(self, string):
		return input(string)
	
	#Define promptUserForPositiveNumber()method 
	def promptUserForPositiveNumber(self, string):
		no = int(input(string))
		while no <= 0:
			print("Amount cannot be negative. Try again")
			no = int(input(string))
		return no
	
	#Define covertFromDollarsToCents()method
	def convertFromDollarsToCents(self, dollar):
		return dollar * 100
	
	#Define generateRandomInteger()method
	def generateRandomInteger(self, min, max):
		return random.randint(min, max)

#Create class name BankManager		
class BankManager:
	"""docstring for BankManager"""
	
	#Define constructor for class BankManager
	def __init__(self):
		super().__init__()

	#Define main()method
	def main(self):
		
		bank = Bank()
		while True:
			print('What do you want to do?')
			print('1. Open an account')
			print('2. Get account information and balance')
			print('3. Change PIN')
			print('4. Deposit money in account')
			print('5. Transfer money between accounts')
			print('6. Withdraw money from account')
			print('7. ATM withdrawal')
			print('8. Deposit change')
			print('9. Close an account')
			print('10. Add monthly interest to all accounts')
			print('11. End Program')
			print('-'*50)

			choice = input("Enter your choice: ")
			if choice == '1':
				self.openAccount(bank)
				print('-'*50)
			elif choice == '2':
				self.getAccountInfoAndBalance(bank)
				print('-'*50)
			elif choice == '3':
				self.changePIN(bank)
				print('-'*50)
			elif choice == '4':
				self.deposit(bank)
				print('-'*50)
			elif choice == '5':
				self.transfer(bank)
				print('-'*50)
			elif choice == '6':
				self.withdraw(bank)
				print('-'*50)
			elif choice == '7':
				self.atmWithdrawal(bank)
				print('-'*50)
			elif choice == '8':
				self.depositChange(bank)
				print('-'*50)
			elif choice == '9':
				self.closeAccount(bank)
				print('-'*50)
			elif choice == '10':
				self.addMonthlyInterest(bank)
				print('-'*50)
			elif choice == '11':
				break
			else:
				print("Invalid choice. Try again")
	
	#Define promptForAccountNumberAndPIN()method with parameter bank.
	def promptForAccountNumberAndPIN(self, bank):
		acc_no = input("Enter an account number: ")
		acc = bank.findAccount(acc_no)
		if acc == 'null':
			print("Account not found for account number:", acc_no)
			return 'null'
		pin = input("Enter a PIN: ")
		if acc["pin"] == pin:
			return acc
		else:
			print("Invalid PIN")
			return 'null'
	
	#Define openAccount()method with parameter bank.
	def openAccount(self, bank):
		print("Open An Account")
		utility = BankUtility()
		fname = utility.promptUserForString("Enter Account Owner's First Name: ")
		lname = utility.promptUserForString("Enter Account Owner's Last Name: ")
		ssn = utility.promptUserForPositiveNumber("Enter Account Owner's SSN (9 digits): ")
		while len(str(ssn)) != 9:
			print("Social Security Number must be 9 digits")
			ssn = utility.promptUserForPositiveNumber("Enter Account Owner's SSN (9 digits): ")

		accountNumber = ''
		pin = ''
		for i in range(8):
			accountNumber = accountNumber+str(utility.generateRandomInteger(0, 9))
		ownerFirstName = fname
		ownerLastName = lname
		socialSecurityNumber = ssn
		for i in range(4):
			pin = pin+str(utility.generateRandomInteger(0, 9))
		balance = 0
		account = Account(accountNumber, ownerFirstName, ownerLastName
			, socialSecurityNumber, pin, balance)
		print('-'*50)
		print(account.toString())

		bank.addAccountToBank(account)

	#Define getAccountInfoAndBalance()method with parameter bank.
	def getAccountInfoAndBalance(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		print('-'*50)
		print(account.toString())
	
	#Define changePIN()method with parameter bank.
	def changePIN(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		new_pin = input("Enter new PIN: ")
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		while account.isValidPIN(new_pin) is False:
			print("PIN must be 4 digits, try again.")
			new_pin = input("Enter new PIN: ")
		confirm_pin = input("Enter new PIN again to confirm: ")
		while account.isValidPIN(confirm_pin) is False:
			print("PIN must be 4 digits, try again.")
			confirm_pin = input("Enter new PIN again to confirm: ")
		if new_pin != confirm_pin:
			print("PINs do not match, try again.")
			return
		else:
			bank.changePIN(acc["accountNumber"], new_pin)
			print("Pin updated")
	
	#Define deposit()method with parameter bank.
	def deposit(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		amount = float(input("Enter amount to deposit: "))
		if amount <= 0:
			print("Amount cannot be negative. Try again.")
			return
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		new_bal = account.deposit(amount)
		bank.updateAccountOfBank(account.accountNumber, 'balance', new_bal)
		print("New balance: $",new_bal)
	
	#Define withdraw()method with parameter bank.
	def withdraw(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		amount = float(input("Enter amount to withdraw: "))
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		new_bal = account.withdraw(amount)
		if new_bal == acc["balance"]:
			print("Insufficient funds in account ",account.accountNumber)
		else:
			bank.updateAccountOfBank(account.accountNumber, 'balance', new_bal)
			print("New balance: $",new_bal)

	#Define transfer()method with parameter bank.
	def transfer(self, bank):
		print("Account to Transfer from:")
		acc1 = self.promptForAccountNumberAndPIN(bank)
		if acc1 == 'null':
			return 'null'
		print("Account to Transfer to:")
		acc2 = self.promptForAccountNumberAndPIN(bank)
		if acc2 == 'null':
			return 'null'
		amount = float(input("Enter amount to transfer in dollars and cents:"))
		account1 = Account(acc1["accountNumber"], acc1["ownerFirstName"], acc1["ownerLastName"], acc1["socialSecurityNumber"], acc1["pin"], acc1["balance"])
		new_bal1 = account1.withdraw(amount)
		if new_bal1 == acc1["balance"]:
			print("Insufficient funds in account ",account1.accountNumber)
			return
		else:
			bank.updateAccountOfBank(account1.accountNumber, 'balance', new_bal1)
		account2 = Account(acc2["accountNumber"], acc2["ownerFirstName"], acc2["ownerLastName"], acc2["socialSecurityNumber"], acc2["pin"], acc2["balance"])
		new_bal2 = account2.deposit(amount)
		bank.updateAccountOfBank(account2.accountNumber, 'balance', new_bal2)
		print("Transfer Complete")
		print("New Balance in Account:"+account1.accountNumber+" is: $"+str(new_bal1))
		print("New Balance in Account:"+account2.accountNumber+" is: $"+str(new_bal2))

	#Define atmWithdrawal()method with parameter bank.
	def atmWithdrawal(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		amount = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): "))
		print(amount)
		while amount < 5 or amount > 1000 or amount % 5 != 0:
			print("Invalid Amount. Try again")
			amount = int(input("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000): "))
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		new_bal = account.withdraw(amount)
		if new_bal == acc["balance"]:
			print("Insuficient Balance")
			return
		else:
			bank.updateAccountOfBank(account.accountNumber, 'balance', new_bal)
			bill1 = math.floor(amount/20)
			bill2 = math.floor((amount%20)/10)
			bill3 = math.floor(((amount%20)%10)/5)
			print("Number of 20-dollar bills: ", bill1)
			print("Number of 10-dollar bills: ", bill2)
			print("Number of 5-dollar bills: ", bill3)
			print("New balance: $",new_bal)
	
	#Define depositChange()method with parameter bank.
	def depositChange(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		coins = input("Deposit coins: ")
		collector = CoinCollector()
		amount = collector.parseChange(coins)
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		new_bal = account.deposit(amount)
		bank.updateAccountOfBank(account.accountNumber, 'balance', new_bal)
		print(f"${amount} in coins deposited into account")
		print("New balance: $",new_bal)

	#Define closeAccount()method with parameter bank.
	def closeAccount(self, bank):
		acc = self.promptForAccountNumberAndPIN(bank)
		if acc == 'null':
			return 'null'
		account = Account(acc["accountNumber"], acc["ownerFirstName"], acc["ownerLastName"], acc["socialSecurityNumber"], acc["pin"], acc["balance"])
		bank.removeAccountFromBank(account)
		print(f"Account {account.accountNumber} closed")
	
	#Define addMonthlyInterest()method with parameter bank.
	def addMonthlyInterest(self, bank):
		rate = float(input("Enter annual interest rate percentage: "))
		bank.addInterest(rate)

#calling main function		
if __name__ == '__main__':
	
	bm = BankManager()
	bm.main()
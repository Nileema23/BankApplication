#import unittest and from bank import every methods
import unittest
from bank import *

#Create class name TestBank
class TestBank(unittest.TestCase):
	"""docstring for TestBank
	 define setUp() method which runs before each test method within test case
	"""
	def setUp(self):
		self.account1 = Account('12345678', 'John', 'Doe', '111122223', '1234', 100)
		self.account2 = Account('11111111', 'Jane', 'Doe', '111111111', '1111', 50)

	def testAddAccountToBank(self):
		bank = Bank()
		bank.addAccountToBank(self.account1)
		acc = bank.findAccount('12345678')
		self.assertEqual(acc["accountNumber"], '12345678')
		#------------------------------------------
		acc = bank.findAccount('12345678')
		self.assertEqual(acc["socialSecurityNumber"], '111122223')
		#------------------------------------------
		bank.addAccountToBank(self.account2)
		acc = bank.findAccount('11111111')
		self.assertEqual(acc['accountNumber'], '11111111')

	def testremoveAccountFromBank(self):
		bank = Bank()
		bank.addAccountToBank(self.account1)
		accno = bank.removeAccountFromBank(self.account1)
		self.assertEqual(accno["accountNumber"], '12345678')
		#---------------------------------------------------
		bank.addAccountToBank(self.account2)
		accno = bank.removeAccountFromBank(self.account2)
		self.assertEqual(accno["socialSecurityNumber"], '111111111')


	def testfindAccount(self):
		bank = Bank()
		bank.addAccountToBank(self.account2)
		acc = bank.findAccount('11111111')
		self.assertEqual(acc["accountNumber"], '11111111')
		#------------------------------------------------------
		acc = bank.findAccount('11111111')
		self.assertEqual(acc["socialSecurityNumber"], '111111111')

	def testdeposit(self):
		total = self.account1.deposit(100)
		self.assertEqual(total,200)
		#-------------------------------------
		total = self.account2.deposit(50.5)
		self.assertEqual(total,100.5)


	def testwithdraw(self):
		total = self.account1.withdraw(50)
		self.assertEqual(total,50)
	#----------------------------------
		total = self.account1.withdraw(60)
		self.assertEqual(total,50)

	def testisValidPIN(self):
		valid = self.account1.isValidPIN('1234')
		self.assertTrue(valid)
	#----------------------------------------
		valid = self.account1.isValidPIN('abde')
		self.assertFalse(valid)

	def testparseChange(self):
		Cc = CoinCollector()
		value = Cc.parseChange('WH')
		self.assertEqual(value, 1.50 )
	#-----------------------------------------
		value = Cc.parseChange('HH')
		self.assertEqual(value, 1)
	#----------------------------------------
		value = Cc.parseChange('PNDQHW')
		self.assertEqual(value, 1.91)


	def testisNumeric(self):
		bu = BankUtility()
		num = bu.isNumeric("1")
		self.assertTrue(num)
	#----------------------------
		num = bu.isNumeric("a")
		self.assertFalse(num)
	
	def testconvertFromDollarsToCents(self):
		bu = BankUtility()
		dtc = bu.convertFromDollarsToCents(10)
		self.assertEqual(dtc,1000)
	#-----------------------------
		dtc = bu.convertFromDollarsToCents(5.50)
		self.assertEqual(dtc,550)


	def testgenerateRandomInteger(self):
		bu = BankUtility()
		num = bu.generateRandomInteger(1,100)
		self.assertEqual(type(num),int)
	#-------------------------------------------
		num = bu.generateRandomInteger(1,100)
		self.assertNotEqual(num,939)


if __name__ == '__main__':
    unittest.main()

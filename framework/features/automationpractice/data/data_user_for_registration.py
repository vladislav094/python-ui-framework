from random import randint

mail_random_int = randint(1,1000)
password_random_int = randint(1,1000)

class DataUserForRegistration:

	'''Credentials'''
	EMAIL_ADDRESS = 'qweqwe123@qwe.qwe'
	PASSWORD = 'qwe123'
	RANDOM_EMAIL_ADDRESS_FOR_REGISTRATION = f'testmail{mail_random_int}@mail.com'   #Required field
	RANDOM_PASSWORD_FOR_REGISTRATION = f'pass{password_random_int}word'             #Required field

	'''Data of user'''
	FIRST_NAME = 'Ivan'     #Required field
	LAST_NAME = 'Ivanov'    #Required field
	DAY_OF_BIRTH = '09'
	MONTH_OF_BIRTH = 'August'
	YEAR_OF_BIRTH = '2020'
	COMPANY = 'IT company'
	ADDRESS_LINE_1 = 'Friendship of Peoples avenue'     #Required field
	ADDRESS_LINE_2 = 'Solidarity street'
	CITY = 'New York'   #Required field
	STATE = 'New York'  #Required field
	POSTAL_CODE = '112233'  #Required field
	COUNTRY = 'United States'   #Required field
	HOME_PHONE = '+1 112 768 44 25'
	MOBILE_PHONE = '+1 777 23 23 000'   #Required field
	ALIAS_ADDRESS = 'Lenina street'     #Required field


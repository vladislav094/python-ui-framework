from random import randint
from faker import Faker

password_random_int = randint(666666, 88888888)
fake = Faker()
random_mail = fake.email()


class DataUserForRegistration:
	'''Credentials'''
	EMAIL_ADDRESS = 'qweqwe123@qwe.qwe'
	PASSWORD = 'qwe123'
	RANDOM_EMAIL_ADDRESS_FOR_REGISTRATION = f'{random_mail}'   #Required field
	RANDOM_PASSWORD_FOR_REGISTRATION = f'pass{password_random_int}word'             #Required field

	"""Credentials after registration"""
	SAVED_PASSWORD_AFTER_REGISTRATION = RANDOM_PASSWORD_FOR_REGISTRATION
	SAVED_EMAIL_AFTER_REGISTRATION = RANDOM_EMAIL_ADDRESS_FOR_REGISTRATION

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
	POSTAL_CODE = '12345'  #Required field
	COUNTRY = 'United States'   #Required field
	HOME_PHONE = '+1 112 768 44 25'
	MOBILE_PHONE = '+1 777 23 23 000'   #Required field
	ALIAS_ADDRESS = 'Lenina street'     #Required field

	EMAIL_ADDRESS_WITHOUT_DOMAIN = 'email_without_domain@'
	EMAIL_ADDRESS_WITHOUT_AT = 'email_without_atgmail.com'
	EMAIL_ADDRESS_WITHOUT_DOT = 'email_without_dot@gmailcom'
	EMAIL_ADDRESS_WITH_SPEC_CHARACTER = 'email_with_t№$@gmailcom'


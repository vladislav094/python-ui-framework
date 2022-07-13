from selenium.webdriver.common.by import By


class AutomationPracticeSingInPage:
    EMAIL_FIELD_FOR_CREATE = (By.XPATH, '//*[@id="email_create"]')  # Required field
    EMAIL_FIELD_FOR_SIGN_IN = (By.XPATH, '//*[@id="email"]')  # Required field
    PASSWORD_FIELD_FOR_SIGN_IN = (By.XPATH, '//*[@id="passwd"]')  # Required field

    """All button"""
    SUBMIT_BUTTON_FOR_CREATE = (By.XPATH, '//*[@id="SubmitCreate"]')
    SUBMIT_BUTTON_FOR_SIGN_IN = (By.XPATH, '//*[@id="SubmitLogin"]')
    SUBMIT_BUTTON_FOR_RETRIEVE_PASSWORD = (By.XPATH, '//*[@id="form_forgotpassword"]/fieldset/p/button')
    WHEN_FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@id="login_form"]/div/p[1]/a')
    BACK_TO_LOGIN_BUTTON = (By.XPATH, '//*[@id="center_column"]/ul/li/a')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="submitAccount"]')

    """Personal information of user"""
    RADIO_BUTTON_GENDER_MR = (By.XPATH, '//*[@id="id_gender1"]')
    RADIO_BUTTON_GENDER_MRS = (By.XPATH, '//*[@id="id_gender2"]')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="customer_firstname"]')  # Required field
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="customer_lastname"]')  # Required field

    """Date of Birth Drop-down list"""
    DAY_DROP_LIST = (By.XPATH, '//*[@id="days"]')
    MONTH_DROP_LIST = (By.XPATH, '//*[@id="months"]')
    YEARS_DROP_LIST = (By.XPATH, '//*[@id="years"]')

    """Check-box"""
    NEWSLETTER_CHECK_BOX = (By.XPATH, '//*[@id="newsletter"]')
    SPECIAL_OFFERS_CHECK_BOX = (By.XPATH, '//*[@id="optin"]')

    """Address of user"""
    FIRST_NAME_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="firstname"]')  # Required field
    LAST_NAME_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="lastname"]')  # Required field
    COMPANY_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="company"]')
    ADDRESS_FIELD_LINE_1_IN_ADDRESS = (By.XPATH, '//*[@id="address1"]')  # Required field
    ADDRESS_FIELD_LINE_2_IN_ADDRESS = (By.XPATH, '//*[@id="address2"]')
    CITY_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="city"]')  # Required field
    POSTAL_CODE_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="postcode"]')  # Required field
    ADDITIONAL_INFORMATION_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="other"]')
    HOME_PHONE_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="phone"]')
    MOBILE_PHONE_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="phone_mobile"]')  # Required field
    ALIAS_ADDRESS_FIELD_IN_ADDRESS = (By.XPATH, '//*[@id="alias"]')  # Required field

    """State and Country Drop-down list"""
    STATE_DROPDOWN_LIST = (By.XPATH, '//*[@id="id_state"]')  # Required field
    COUNTRY_DROPDOWN_LIST = (By.XPATH, '//*[@id="id_country"]')  # Required field

    """Elements for assert after registration"""
    LINK_MY_ACCOUNT = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span')

    """Element for assert negative case after authorization"""
    TEXT_AUTHENTICATION_FAILED = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
    TEXT_CREATE_ACCOUNT_ERROR = (By.XPATH, '//*[@id="create_account_error"]/ol/li')
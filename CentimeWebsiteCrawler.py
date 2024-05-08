# Code to fetch all Html Dom Files of Centime
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import enum, time
import os

output_folder = 'CentimeDomFiles'
base_url = 'https://go.qa.centime.com/login'
EmailId = 'gsrinivasan@centime.com'
Password = 'Testcentime$100'

class GenericLocators:
    spinner = (By.XPATH, "//div[@style='opacity: 1; transition: opacity 225ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;']")
    login_id_locator = (By.ID, 'loginId')
    password_locator = (By.ID, 'password')
    login_button_locator = (By.ID, 'loginBtn')
    centime_logo_short_home_locator = (By.XPATH, "//button[@aria-label='centime-short']")
    centime_logo_home_locator = (By.XPATH, "//span[@title='centime']")
    manage_payables_locator = (By.XPATH, "//img[@title='Payables']/parent::div/parent::div/parent::div")
    unpaid_invoices_tab_button = (By.XPATH, "//h5[contains(text(),'Unpaid Invoices')]/parent::span/parent::button")
    supplier_panel_href = (By.XPATH, "//div[@data-props-id='companyName']")
    supplier_panel_profile_button = (By.XPATH, "//h5[contains(text(),'Profile')]/parent::span/parent::button")
    supplier_panel_profile_edit_buttons = (By.XPATH, "//button[@aria-label='Edit']")
    supplier_panel_payments_button = (By.XPATH, "//h5[contains(text(),'Payments')]/parent::span/parent::button")
    supplier_panel_payments_plus_button = (By.XPATH, "//button[@aria-label='plus']")
    supplier_panel_history_button = (By.XPATH, "//h5[contains(text(),'History')]/parent::span/parent::button")
    supplier_panel_notes_button = (By.XPATH, "//h5[contains(text(),'Notes')]/parent::span/parent::button")
    close_button = (By.XPATH, "//button[@aria-label='Close']")
    close_bare_button = (By.XPATH, "//button[@aria-label='close-bare']")
    credit_card_pfa_dropdown = (By.XPATH, "//div[@id='payFromAccountCreditCard']/parent::div")
    credit_card_pfa_dropdown_options = (By.XPATH, "//p[contains(text(), 'Credit Card')]/parent::div/parent::div/parent::li")
    centime_card_by_email_radio_button = (By.ID, 'shareOnCentimePaymentPortal')
    centime_card_by_directly_supplier_portal_radio_button = (By.ID, 'payDirectlyOnSupplierWebsite')

def clear_folder(output_folder):
    os.system(f"rm {output_folder}/*")


def get_chrome_options():
    options = Options()
    options.headless = False
    # options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')


def get_browser_driver():
    service = Service(executable_path='chromedriver/chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def loginToPortal(driver: webdriver.Chrome, EmailId, Password):
    login_element = driver.find_element(*GenericLocators.login_id_locator)
    password_element = driver.find_element(*GenericLocators.password_locator)
    loginBtn_element = driver.find_element(*GenericLocators.login_button_locator)
    login_element.send_keys(EmailId)
    password_element.send_keys(Password)
    loginBtn_element.click()

def writePageSourceToFile(driver: webdriver.Chrome, output_folder, filename):
    html_content = driver.execute_script("return document.documentElement.outerHTML;")
    # html_content = driver.page_source
    with open(output_folder+ '/' + filename + '.html', 'w', encoding='utf-8') as file:
        file.write(html_content)



def wait_for_invisibility_of_spinner(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(ec.invisibility_of_element(GenericLocators.spinner))
    except:
        pass

def Dashboard(driver: webdriver.Chrome):
    try:
        home_button_locator = driver.find_element(*GenericLocators.centime_logo_home_locator)
    except:
        home_button_locator = driver.find_element(*GenericLocators.centime_logo_short_home_locator)
    home_button_locator.click()
    wait_for_invisibility_of_spinner(driver)

def ManagePayablesPage(driver: webdriver.Chrome):
    driver.implicitly_wait(10)
    payables_image = driver.find_element(*GenericLocators.manage_payables_locator)
    action = ActionChains(driver)
    action.move_to_element(payables_image).click().perform()
    # payables_image.click()
    wait_for_invisibility_of_spinner(driver)

def UnpaidInvoicesTab(driver: webdriver.Chrome):
    unpaid_invoices_tab_button = driver.find_element(*GenericLocators.unpaid_invoices_tab_button)
    unpaid_invoices_tab_button.click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanel(driver: webdriver.Chrome):
    supplier_panel = driver.find_elements(*GenericLocators.supplier_panel_href)
    supplier_panel[0].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelAddressEditable(driver: webdriver.Chrome):
    supplier_panel_address_edit = driver.find_elements(*GenericLocators.supplier_panel_profile_edit_buttons)
    supplier_panel_address_edit[0].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPrimaryContactEditable(driver: webdriver.Chrome):
    supplier_panel_primary_contact_edit = driver.find_elements(*GenericLocators.supplier_panel_profile_edit_buttons)
    supplier_panel_primary_contact_edit[1].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelDocumentCaptureEditable(driver: webdriver.Chrome):
    supplier_panel_document_capture_edit = driver.find_elements(*GenericLocators.supplier_panel_profile_edit_buttons)
    supplier_panel_document_capture_edit[2].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelSupplierEmailCommunicationsEditable(driver: webdriver.Chrome):
    supplier_panel_suplier_email_edit = driver.find_elements(*GenericLocators.supplier_panel_profile_edit_buttons)
    supplier_panel_suplier_email_edit[3].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPayments(driver: webdriver.Chrome):
    supplier_panel_payments_button = driver.find_element(*GenericLocators.supplier_panel_payments_button)
    supplier_panel_payments_button.click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsCentimeCardByEMailEditable(driver: webdriver.Chrome):
    credit_card_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    credit_card_edit_locators[0].click()
    driver.find_element(*GenericLocators.credit_card_pfa_dropdown).click()
    driver.find_elements(*GenericLocators.credit_card_pfa_dropdown_options)[1].click()
    driver.find_element(*GenericLocators.centime_card_by_email_radio_button).click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsCentimeCardBySupplierPortalEditable(driver: webdriver.Chrome):
    credit_card_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    credit_card_edit_locators[0].click()
    driver.find_element(*GenericLocators.credit_card_pfa_dropdown).click()
    driver.find_elements(*GenericLocators.credit_card_pfa_dropdown_options)[1].click()
    driver.find_element(*GenericLocators.centime_card_by_directly_supplier_portal_radio_button).click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsCreditCardEditable(driver: webdriver.Chrome):
    credit_card_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    credit_card_edit_locators[0].click()
    driver.find_element(*GenericLocators.credit_card_pfa_dropdown).click()
    driver.find_elements(*GenericLocators.credit_card_pfa_dropdown_options)[0].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsACHEditable(driver: webdriver.Chrome):
    ach_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    ach_edit_locators[1].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsCheckEditable(driver: webdriver.Chrome):
    check_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    check_edit_locators[2].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelPaymentsOtherEditable(driver: webdriver.Chrome):
    other_edit_locators = driver.find_elements(*GenericLocators.supplier_panel_payments_plus_button)
    other_edit_locators[3].click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelHistory(driver: webdriver.Chrome):
    supplier_panel_history_locator = driver.find_element(*GenericLocators.supplier_panel_history_button)
    supplier_panel_history_locator.click()
    wait_for_invisibility_of_spinner(driver)

def SupplierSidePanelNotes(driver: webdriver.Chrome):
    supplier_panel_notes_locator = driver.find_element(*GenericLocators.supplier_panel_notes_button)
    supplier_panel_notes_locator.click()
    wait_for_invisibility_of_spinner(driver)

def ClosePrimaryPanel(driver:webdriver.Chrome):
    close_buttons = driver.find_elements(*GenericLocators.close_button)
    close_buttons[0].click()

def CloseSecondaryPanel(driver:webdriver.Chrome):
    try:
        close_buttons = driver.find_elements(*GenericLocators.close_button)
        close_buttons[1].click()
    except:
        close_buttons = driver.find_elements(*GenericLocators.close_bare_button)
        close_buttons[0].click()



path = ['Dashboard', 'ManagePayablesPage','UnpaidInvoicesTab', 'SupplierSidePanel', 'SupplierSidePanelAddressEditable','CloseSecondaryPanel',
        'SupplierSidePanelPrimaryContactEditable', 'CloseSecondaryPanel' ,'SupplierSidePanelDocumentCaptureEditable', 'CloseSecondaryPanel', 'SupplierSidePanelSupplierEmailCommunicationsEditable',
        'SupplierSidePanelPayments', 'SupplierSidePanelPaymentsCentimeCardByEMailEditable, SupplierSidePanelPaymentsCentimeCardBySupplierPortalEditable, SupplierSidePanelPaymentsCreditCardEditable',
        'CloseSecondaryPanel' ,'SupplierSidePanelPaymentsACHEditable', 'CloseSecondaryPanel','SupplierSidePanelPaymentsCheckEditable',
        'CloseSecondaryPanel', 'SupplierSidePanelPaymentsOtherEditable', 'SupplierSidePanelHistory', 'SupplierSidePanelNotes']

clear_folder(output_folder)
driver = get_browser_driver()
driver.get(base_url)
wait = WebDriverWait(driver, 10)
wait.until(ec.invisibility_of_element(GenericLocators.spinner))
time.sleep(5)
loginToPortal(driver, EmailId, Password)
writePageSourceToFile(driver, output_folder, filename='LoginPage')

for page in path:
    eval(page + '(driver)')
    time.sleep(7)
    if 'Close' not in page:
        writePageSourceToFile(driver, output_folder, filename=page)
    else:
        pass


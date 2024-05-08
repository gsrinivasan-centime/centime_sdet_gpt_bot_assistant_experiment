import graphviz

# Wrote upto supplier panel
def centime_web_portal_flow_chart():
    # Creating a Graphviz diagram to better represent the flowchart with arrows.
    dot = graphviz.Digraph(comment='Centime Web Portal Flow', format='png')
    # dot.attr(splines='false')

    # Adding nodes and edges to represent the flow of the web portal.
    dot.node('Login', 'Login Page\n(Email ID, Password)')
    dot.node('Forgot', 'Forgot Password Page\n(Email ID input)')
    dot.node('Dashboard', 'Dashboard\n(Banking, Forecasting, KPIs, Receivables, Payables, Risk & Reputation)')
    dot.node('Banking', 'Banking\nDashboard')
    dot.node('Forecasting', 'CashFlowForecast\nDashboard')
    dot.node('KPIs', 'KPIs\nDashboard')
    dot.node('Receivables', 'AR\nDashboard')
    dot.node('Payables', 'AP\nDashboard')
    dot.node('Risk & Reputation', 'RnR\nDashboard')


    # Connecting nodes with directional edges.
    dot.edge('Login', 'Dashboard', label='Login Success')
    dot.edge('Login', 'Forgot', label='Forgot Password')
    dot.edge('Dashboard', 'Banking', label='Select Banking')
    dot.edge('Dashboard', 'Forecasting', label='Select Forecasting')
    dot.edge('Dashboard', 'KPIs', label='Select KPIs')
    dot.edge('Dashboard', 'Receivables', label='Select Receivables')
    dot.edge('Dashboard', 'Payables', label='Select Payables')
    dot.edge('Dashboard', 'Risk & Reputation', label='Select Risk & Reputation')


    dot.node('Suppliers Tab', 'Suppliers Tab\n List of suppliers \nhaving atleast one \noutstanding invoice')
    dot.node('Documents Tab', 'Documents Tab')
    dot.node('Unpaid Invoices Tab', 'Unpaid invoices Tab\n List of invoices \nto be paid to suppliers')
    dot.node('Paid Invoices Tab', 'Paid invoices Tab\n List of invoices \n paid to suppliers')

    dot.edge('Payables', 'Suppliers Tab' ,label='Select Suppliers tab')
    dot.edge('Payables', 'Documents Tab' ,label='Select Documents tab')
    dot.edge('Payables', 'Unpaid Invoices Tab' ,label='Select Unpaid Invoices tab')
    dot.edge('Payables', 'Paid Invoices Tab' ,label='Select Paid Invoices tab')

    with dot.subgraph(name='Tabs') as c:
        c.attr(style='filled', color='lightgrey')
        c.node_attr.update(style='filled', color='white', shape='box')
        c.node('Suppliers Tab')
        c.node('Documents Tab')
        c.node('Unpaid Invoices Tab')
        c.node('Paid Invoices Tab')
        c.attr(label='Tabs')

    dot.node('No Action', 'No Action tab\n List of unpaid invoices\n in read only mode')
    dot.node('Edit Action', 'Edit Action tab\n List of unpaid invoices\n with status user action needed,\n In process, Scheduled, \n Ready to Pay, Awaiting approval,\n Rejected and Failed status\n in read only mode')
    dot.node('Pay Action', 'Pay Action tab\n List of unpaid invoices\n with Ready to Pay\n and \nReady to pay with an amber alert status')
    dot.node('Approve Action', 'Approve Action tab\n List of unpaid invoices\n in Awaiting approval status')
    dot.node('Reject Action', 'Reject Action tab\n List of unpaid invoices\n in Awaiting approval status')
    dot.node('Recall Action', 'Recall Action tab\n List of unpaid invoices\n in Scheduled status')
    dot.node('Mark Paid Action', 'Mark paid Action tab\n List of unpaid invoices\n with Ready to Pay status\n and \n payment method as FX Payment')


    dot.edge('Unpaid Invoices Tab', 'No Action' ,label='Select No Action tab')
    dot.edge('Unpaid Invoices Tab', 'Edit Action' ,label='Select Edit Action tab')
    dot.edge('Unpaid Invoices Tab', 'Pay Action' ,label='Select Pay Action tab')
    dot.edge('Unpaid Invoices Tab', 'Approve Action' ,label='Select Approve Action tab')
    dot.edge('Unpaid Invoices Tab', 'Reject Action' ,label='Select Reject Action tab')
    dot.edge('Unpaid Invoices Tab', 'Recall Action' ,label='Select Recall Action tab')
    dot.edge('Unpaid Invoices Tab', 'Mark Paid Action' ,label='Select Mark Paid Action tab')

    dot.node("No Action Tab Table","No Action Tab Table\nTable containing\n list of unpaid invoices with\n all fields in read only mode")
    dot.node("No Action Tab Table Supplier Column","No Action Tab Table Supplier Column\nColumn with supplier Name\n with hyperlink to supplier side panel")

    dot.node('Supplier Profile', 'Supplier Profile\n A side panel that opens on\n clicking on any supplier name\n in table \'Supplier\' column. ', shape='box')
    dot.node("Profile", "Profile\n supplier profile")
    dot.node("Payments", "Payments\nPayment methods available\n to pay invoice amounts\n to supplier")
    dot.node("History", "History\nAudit trail of \nall update activity\n carried out on supplier panel")
    dot.node("Notes", "Notes\nAny special notes\n to store related to supplier")

    dot.edge("No Action", "No Action Tab Table")
    dot.edge("No Action Tab Table", "Supplier Profile")
    dot.edge("Supplier Profile", "Profile")
    dot.edge("Supplier Profile", "Payments")
    dot.edge("Supplier Profile", "History")
    dot.edge("Supplier Profile", "Notes")

    dot.node("Address", "Address\nEditable Supplier Contact information\n Address, Phone number,\nwebsite, Type and Tax ID")
    dot.node("Primary contact", "Primary contact\nEditable Supplier Contact information\n Name, Phone Number, Email Id")
    dot.node("Document Capture", "Document Capture\nEditable Supplier setting\n Aggregate invoice lines into one Yes/No")
    dot.node("Supplier email communications", "Supplier email communications\nEditable option to send notification when payment is scheduled\n \
            Send remittance when payment is sent\n supplier prtal contact email id")


    dot.node("Supplier portal contact", "Supplier Portal secondary contact")
    dot.node("Name", "Supplier Primary contact Name")
    dot.node("Email", "Supplier Primary contact Email")

    dot.node("Enter Name","Supplier Portal Secondary contact Name")
    dot.node("Enter Email","Supplier Portal Secondary contact Email")

    dot.edge("Profile", "Address")
    dot.edge("Profile", "Primary contact")
    dot.edge("Profile", "Document Capture")
    dot.edge("Profile", "Supplier email communications")

    dot.edge("Primary contact", "Name")
    dot.edge("Primary contact", "Phone number")
    dot.edge("Primary contact", "Email")

    dot.edge("Document Capture", "Aggregate invoice lines into one Yes/No")

    dot.edge("Supplier email communications", "Send notification when payment is scheduled Yes/No")
    dot.edge("Supplier email communications", "Send remittance when payment is sent Yes/No")
    dot.edge("Supplier email communications", "Supplier portal contact")
    dot.edge("Supplier portal contact", "Enter Name")
    dot.edge("Supplier portal contact", "Enter Email")


    dot.node("Payment terms", "Payment terms\nDefault supplier payment terms obtained from QBO GL")
    dot.node("Currency", "Currency\nDefault supplier currency obtained from QBO GL")
    dot.node("Supplier Portal", "Supplier Portal\nSupplier portal web address created by centime")
    dot.node("Payment Methods","Payment Methods\nAvailable supplier payment methods\n Radio button options to select\n Credit Card, ACH, Check, Other and None")

    dot.node("Credit Card", "Credit Card\nPay using Credit Card")
    dot.node("Pay from account - Credit Card", "Pay from account (pfa)\ndropdown to select funding card accounts \neg. Credit Card, Centime Credit Card or Amex Credit Card")
    dot.node('Select pfa as Credit Card', 'Pfa as Credit Card')
    dot.node('Select pfa as Centime Credit Card or Amex Card', 'Pfa as Centime Credit Card or Amex Card')
    dot.node("Card Delivery", "Card Delivery\nRadio button options\n to share virtual card number(VCN) details\n through email or on supplier portal")
    dot.node("By Email", "By Email\n Radio button option")
    dot.node("We will pay on the supplier website", "We will pay on the supplier website\n Radio button option")
    dot.node("VCN delivery Name", "Name\nName of the person\n to whom the\n VCN details are shared")
    dot.node("VCN delivery Email", "Email\nEmailId of the person\n to whom the\n VCN details are shared")
    dot.node("Supplier website address", "Suppliers website address")
    dot.node("Payment Limit", "Payment Limit\nPayment Limit of Credit Card")
    dot.node("Surcharge", "Surcharge in %\nSurcharge amount charged \nby the Credit card company\n for transaction\n client has to pay inclusive of \nsurcharge amount while making invoice amount")


    # Payments 
    dot.edge("Payments", "Payment terms")
    dot.edge("Payments", "Currency")
    dot.edge("Payments", "Supplier Portal")
    dot.edge("Payments", "Payment Methods")

    #Credit Card
    dot.edge("Payment Methods", "Credit Card")
    dot.edge("Credit Card", "Pay from account - Credit Card")
    dot.edge("Pay from account - Credit Card", 'Select pfa as Credit Card')


    dot.edge("Pay from account - Credit Card", 'Select pfa as Centime Credit Card or Amex Card')
    dot.edge('Select pfa as Centime Credit Card or Amex Card', "Card Delivery")
    dot.edge('Select pfa as Centime Credit Card or Amex Card', "Payment Limit")
    dot.edge('Select pfa as Centime Credit Card or Amex Card', "Surcharge")
    dot.edge("Card Delivery","By Email")
    dot.edge("By Email","VCN delivery Name")
    dot.edge("By Email","VCN delivery Email")
    dot.edge("Card Delivery","We will pay on the supplier website")
    dot.edge("We will pay on the supplier website", "Supplier website address")
    dot.edge('Select pfa as Credit Card', "Payment Limit")
    dot.edge('Select pfa as Credit Card', "Surcharge")
    dot.edge("Select pfa as Credit Card", "Supplier website address")

    #ACH
    dot.node("ACH", "ACH payment method\n This method is used for\nbank to bank to money transfer")
    dot.node("Pay from account - ACH", "Pay from account\nDropdown to select funding bank account eg. Checking or Saving account")
    dot.node("Pay to Account - ACH", "Pay to Account\n Ready only message with status\nof supplier bank account validation eg. 'Valid account', 'Invalid Account' \nand 'Account Validation In Progress'")
    dot.node("Routing Number", "Supplier Bank Routing Number\nInput field for Supplier Bank Routing Number")
    dot.node("Bank Name", "Bank Name\nAfter entering Routing number,\nthe Bank name is immediately fetched and shown by centime")
    dot.node("Account Number", "Supplier Bank Account Number\nInput field for Supplier Bank Account Number")
    dot.node("Re-enter Account Number", "Supplier Bank Account Number\nInput field for Reentering Supplier Bank Account Number")
    dot.node("Group ACH Payments", "Group payments made on same payment date\nToggle switch to enable or\n disable group payments")

    dot.edge("Payment Methods", "ACH")
    dot.edge("ACH", "Pay from account - ACH")
    dot.edge("ACH", "Pay to Account - ACH")
    dot.edge("Pay to Account - ACH", "Routing Number")
    dot.edge("Pay to Account - ACH", "Bank Name")
    dot.edge("Pay to Account - ACH", "Account Number")
    dot.edge("Pay to Account - ACH", "Re-enter Account Number")
    dot.edge("ACH", "Group ACH Payments")

    #Check
    dot.node("Check", "Check payment method\n This method is used for\npaying invoice amounts through printed Checks")
    dot.node("Pay from account - Check", "Pay from account\nDropdown to select funding bank account eg. Checking or Saving account")
    dot.node("Pay to Account - Check", "Pay to Account")
    dot.node("Name on Check", "Name on Check\nInput field for Name to be printed on Check")
    dot.node("Mailing Address", "Mailing Address\nCheckbox with Input field\n if supplier prefers to recieve the \ncheck to a different mailing address")
    dot.node("Group Check Payments", "Group payments made on same payment date\nToggle switch to enable or\n disable group payments")

    dot.edge("Payment Methods", "Check")
    dot.edge("Check", "Pay from account - Check")
    dot.edge("Check", "Pay to Account - Check")
    dot.edge("Pay to Account - Check", "Name on Check")
    dot.edge("Pay to Account - Check", "Mailing Address")
    dot.edge("Check", "Group Check Payments")

    #Other
    dot.node("Other", "Other\nPayments made outside of centime\n can be marked paid using\n these payment methods")
    dot.node("Pay from account - Other", "Pay from account\nDropdown to select funding bank account eg. Amazon Savings account, Pay Pal etc.")

    dot.edge("Payment Methods", "Other")
    dot.edge("Other", "Pay from account - Other")

    #Other
    dot.node("None Specified", "None Specified\n If no accounts are fetched from GL, this option is default")
    dot.edge("Payment Methods", "None Specified")

    dot.node("Supplier History","Supplier History\n Paginated audit trail\nof all actions made in the\n supplier side panel.\nContains Date, Action and Action Description")
    dot.edge("Supplier Profile", "Supplier History")

    dot.node("Notes", "Notes\nSupplier Notes can be stored here")
    dot.node("Add Notes", "Add Notes\n Input field to add notes")
    dot.node("Notes Audit Trail", "Paginated Audit Trail of notes with date and notes")

    # dot.node()

    # Saving and showing the diagram
    output_path = 'output_flowcharts/Web_Portal_Flowchart_Diagram'
    dot.render(output_path, view=True)
    output_path



# Just started this
def centime_production_activation():
    # Production aactivation flowchart
    # Creating a Graphviz diagram to better represent the flowchart with arrows.
    dot = graphviz.Digraph(comment='Centime Web Portal PAS Flow', format='png')
    # dot.attr(splines='false')


    # Adding nodes and edges to represent the flow of the web portal.
    dot.node('Login', 'Login Page\n(Email ID, Password)')
    dot.node('Forgot', 'Forgot Password Page\n(Email ID input)')
    dot.node('Dashboard', 'Dashboard\n(Banking, Forecasting, KPIs, Receivables, Payables, Risk & Reputation)')
    dot.node('Product Application Service')



    dot.edge('Login', 'Dashboard', label='Login Success')
    dot.edge('Login', 'Forgot', label='Forgot Password')


    output_path = 'output_flowcharts/Web_Portal_PAS_Flowchart_Diagram'
    dot.render(output_path, view=True)
    output_path


# Just started
def centime_nav_bar_flow_chart():
    # Creating a Graphviz diagram to better represent the flowchart with arrows.
    dot = graphviz.Digraph(comment='Centime Web Portal NavBar Flow', format='png')
    # dot.attr(splines='false')


    # Adding nodes and edges to represent the flow of the web portal.
    dot.node('Login', 'Login Page\n(Email ID, Password)')
    dot.node('Forgot', 'Forgot Password Page\n(Email ID input)')
    dot.node('Dashboard', 'Dashboard\n(Banking, Forecasting, KPIs, Receivables, Payables, Risk & Reputation)')
    dot.node('NavBar', 'NavBar\n quick access buttons such as Centime Logo for home page, Buisness Entity selecting dropdown, \nSettings, Notifications, \nGL sync status and controls, Centime Products, \nEasy access button for navigating\n between modules such AP, AR, RnR etc')
    dot.node('Centime Logo', 'Centime Logo\n Centime logo button in nav bar')
    dot.node('Buisness Entity', 'Buisness Entity\n Buisness entity dropdown to select\n other buisness entities of client \n on selecting this entity, by default\n the dashboard of selected entity is opened')
    dot.node('Settings', 'Settings\nGear button in nav bar')
    dot.node('Notifications', 'Notifications\n Bell icon in nav bar')
    dot.node('GL Sync', 'GL Sync\n circular icon in nav bar to see\n the GL sync status and initiate manual GL sync')
    dot.node('Easy access', 'Easy access\n Flower shaped button in navbar to navigate between\n Banking, Forecasting, KPIs, Receivables, Payables, Risk & Reputation modules\n without visiting dashboard page')

    dot.edge('Login', 'Dashboard', label='Login Success')
    dot.edge('Login', 'Forgot', label='Forgot Password')
    dot.edge('Dashboard', 'NavBar')
    dot.edge('NavBar', 'Centime Logo')
    dot.edge('NavBar', 'Buisness Entity')
    dot.edge('NavBar', 'Settings')
    dot.edge('NavBar', 'Notifications')
    dot.edge('NavBar', 'GL Sync')
    dot.edge('NavBar', 'Easy access')

    dot.edge('Centime Logo', 'Dashboard', label='Click on centime logo')
    dot.edge('Buisness Entity', 'Dashboard')

    #Settings page
    dot.node('SideBar', 'Settings SIdeBar')
    dot.node('My Profile', 'My Profile\n Account User profile details')
    dot.node('Company profile', 'Company profile\n Centralized info of client')
    dot.node('Company Information', 'Company Information')
    dot.node('Users', 'Users\n Page to manage all users accounts using the current client')
    dot.node('Billing', 'Billing\n Centime account billing details')
    dot.node('Ownership and control', 'Billing\n Centime account billing details')


    dot.node('Personal details', 'Personal details\n Editable account user details \nFirst name, last name, Email and Job title')
    dot.node('Edit phone number', 'Edit phone number\n Editable section for Mobile number of user')
    dot.node('Edit password', 'Edit password\n Editable section to update password of user')
    dot.node('Edit timeout preference', 'Edit timeout preference\n Editable section to update idle time (in minutes) of user accout\n The mentioned time will ensure logout after the idle time')


    dot.edge('Settings', 'My Profile')
    dot.edge('My Profile', 'Personal details')
    dot.edge('My Profile', 'Edit phone number')
    dot.edge('My Profile', 'Edit password')
    dot.edge('My Profile', 'Edit timeout preference')



    output_path = 'output_flowcharts/Web_Portal_NavBar_Flowchart_Diagram'
    dot.render(output_path, view=True)
    output_path


centime_web_portal_flow_chart()
# centime_production_activation()
# centime_nav_bar_flow_chart()


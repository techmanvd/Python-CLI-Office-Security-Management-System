class officesecurity:
    def __init__(self):
        self.visitor_log = []
        self.security_alerts = []

    def display_menu(self):
        print("\n--- Office Security Alert ---")
        print("1. Login")
        print("2. Add Visitor")    
        print("3. View visitor log")
        print("4. Issue security alert")
        print("5. View security alerts")
        print("6. Exit. ")

    def login(self):
        print("\n--- Login ---")
        username = input("Enter username:- ")
        password = input("Enter password:- ")
        print("Login successful!!!")
    
    def add_visitor(self):
        print("\n--- Add Visitor ---")
        name = input("Enter visitor name:- ")
        purpose = input("Enter purpose to visit:- ")
        self.visitor_log.append({'name':name , 'purpose': purpose})
        print(f"Visitor '{name}' added to the log.")

    def view_visitor_log(self):
        print("\n---Visitors Log---")
        if not self.visitor_log:
            print("No visitors logged.")
        else:
            for idx,visitor in enumerate(self.visitor_log,start=1):
                print(f"{idx}.Name: {visitor['name']}, Purpose:{visitor['purpos']}")

    def issue_security_alert(self):
        print("\n---Issue Security Alert---")
        alert_message = input("Enter alert message: ")
        self.security_alerts.append(alert_message)
        print("Security alert issued.")
    
    def view_security_alerts(self):
        print("\n---Security Alerts---")
        if not self.security_alerts:
            print("No security alert issued .")
        else:
            for idx, alert in enumerate(self.security_alerts,start=1):
                print(f"{idx}.{alert}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-6): ")
            if choice == '1':
                self.login()
            elif choice == '2':
                self.add_visitor()
            elif choice == '3':
                self.view_visitor_log()
            elif choice == '4':
                self.issue_security_alert()
            elif choice == '5':
                self.view_security_alerts()
            elif choice == '6':
                print("---EXITING THE SYSTEM---")
                break
            
            else:
                print("Invalid choice,please try again.")

if __name__ == "__main__":
    app = officesecurity()
    app.run()


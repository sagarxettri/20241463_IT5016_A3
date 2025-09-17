# Start with a global requisition counter
REQUISITION_COUNTER = 1000   # This number will increase each time we create a requisition


# Define the class RequisitionSystem
class RequisitionSystem:

    all_requisitions = [] # Class variable: stores all requisitions created

    # Constructor method: called when a new requisition object is created
    def __init__(self):
        global REQUISITION_COUNTER # Tell Python we are using the global variable
        REQUISITION_COUNTER += 1  # Increase the global counter by 1
        self.requisition_id = REQUISITION_COUNTER  # Assign a unique requisition ID
        self.date = ""   # Placeholder for requisition date (empty for now)
        self.staff_id = ""   # Placeholder for staff ID (empty for now)
        self.staff_name = ""  # Placeholder for staff name (empty for now)
        self.total = 0   # Start total amount at 0
        self.status = "Pending" # Default status is "Pending"
        self.approval_reference_number = "Not available" # Approval reference is empty for now
        RequisitionSystem.all_requisitions.append(self)  # Save this requisition into the list of all requisitions

    # Method for staff to enter information
    def staff_info(self):
        self.date = input("Enter the Date Of Requisition: ")  # Ask user to type the date
        self.staff_id = input("Enter Unique Staff ID: ")   # Ask user to type staff ID
        self.staff_name = input("Enter Staff Name: ")   # Ask user to type staff name

    # Method for entering requisition details (prices of items)
    def requisitions_details(self):
        total = 0    # Start local total at 0
        while True:    # Keep asking until user types "done"
            price = input("Enter item price and when you are done type 'done': $ ")  # Ask user to enter price
            if price.lower() == "done": # If user types "done" (any case like Done/DONE)
                break   # Stop asking for prices
            try:   # Try to convert input to a number
                total += float(price)   # Add the number to total if valid
            except: # If conversion fails
                print("Invalid format. Please type a number.")  # Show error message
        self.total = total  # Save the total amount to this requisition

    # Method for auto-approval check
    def requisition_approval(self):
        if self.total < 500:  # If total cost is less than 500
            self.status = "Approved" # Approve automatically
            # Generate approval reference number = staff ID + last 3 digits of requisition ID
            self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        else:   # If total is 500 or more
            self.status = "Pending"  # Keep it pending for manager decision

    # Method for manager to respond to pending requisitions
    def respond_requisition(self):
        if self.status == "Pending":  # Only if requisition is still pending
            decision = input("Manager: Approve this requisition? yes or no: ")  # Ask manager to decide
            if decision.lower() == "yes": # If manager types "yes"
                self.status = "Approved"  # Change status to Approved
                # Generate approval reference number
                self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            elif decision.lower() == "no":    # If manager types "no"
                self.status = "Not approved"  # Change status to Not approved
            else:  # If manager types anything else
                print("Wrong format.")  # Show error message
        else: # If requisition is already approved or rejected
            print("This requisition is already " + self.status)  # Print current status

    # Method to display requisition details
    def display_requisition(self):
        print(f"Requisition ID: {self.requisition_id}")   # Show requisition ID
        print(f"Date: {self.date}")  # Show date of requisition
        print(f"Staff: {self.staff_name} ({self.staff_id})")  # Show staff name and ID
        print(f"Total: ${self.total}")  # Show total cost
        print(f"Status: {self.status}")  # Show status (Approved/Pending/Not approved)
        print(f"Approval Ref: {self.approval_reference_number}")  # Show approval reference number

    # Method to display overall statistics of all requisitions
    def requisition_statistics(self):
        total_submitted = len(RequisitionSystem.all_requisitions)  # Count how many requisitions have been made
        approved = 0   # Counter for approved requisitions
        pending = 0    # Counter for pending requisitions
        not_approved = 0   # Counter for not approved requisitions

        # Loop through all requisitions in the list
        for req in RequisitionSystem.all_requisitions:
            if req.status == "Approved":  # If requisition status is Approved
                approved += 1             # Increase approved counter
            elif req.status == "Pending":  # If requisition status is Pending
                pending += 1     # Increase pending counter
            elif req.status == "Not approved":  # If requisition status is Not approved
                not_approved += 1   # Increase not approved counter

        # Print statistics
        print("\n Requisition Statistics")  # Heading
        print(f"Total requisition submitted: {total_submitted}")  # Total number
        print(f"Requisition Approved: {approved}")   # Number approved
        print(f"Requisition Pending: {pending}")    # Number pending
        print(f"Requisition Not Approved: {not_approved}")   # Number not approved
        

# This block runs only if the program is run directly (not imported as a module)
if __name__ == "__main__":
    num_reqs = int(input("How many requisitions do you want to enter? "))  # Ask user how many requisitions

    # Loop through the number of requisitions the user wants
    for i in range(num_reqs):
        req = RequisitionSystem()   # Create a new requisition object
        print(f"\nRequisition {i+1}")   # Print requisition number for clarity
        req.staff_info()     # Ask for staff details
        req.requisitions_details()   # Ask for item prices
        req.requisition_approval()   # Check auto approval if under 500
        req.respond_requisition()    # Manager decides if still pending
        req.display_requisition()    # Show requisition details
        req.requisition_statistics()  # Show overall statistics

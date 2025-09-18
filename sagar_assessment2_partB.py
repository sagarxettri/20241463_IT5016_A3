
# GLOBAL COUNTER
# Keeps track of unique requisition IDs
'''Principle:
# K.I.S.S- Focus on making code straightforward and easy to understand.
#Avoid unnecessary complexity so that anyone reading or maintaining it can quickly grasp what’s happening.
#Simple solutions are usually more reliable and easier to manage in the long run.'''
REQUISITION_COUNTER = 1000

# REQUISITION SYSTEM CLASS
# Defines all requisition attributes and methods
'''Principles:
#Single Responsibility – Each class should focus on one thing. This keeps the code clean and easier to maintain.
#Open / Closed – code should be open for adding new features but closed for modifying existing ones.'''
class RequisitionSystem:
    all_requisitions = []  # Stores all requisitions for tracking and statistics

# NEW REQUISITION
# Initializes a new requisition with default values
# Adds it to the list of all requisitions
'''Principles:
#Single Responsibility – Each class or function should do only one thing. keeping the code focused and easier to maintain.
#D.R.Y– To Avoid duplicating logic. By centralizing ID creation in one place.'''
    def __init__(self):
        global REQUISITION_COUNTER
        REQUISITION_COUNTER += 1
        self.requisition_id = REQUISITION_COUNTER
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.total = 0
        self.status = "Pending"
        self.approval_reference_number = "Not available"
        RequisitionSystem.all_requisitions.append(self)


    # STAFF INFORMATION
    # Collects staff details: date, staff ID, and name
    '''#Principle
    # SRP: This method only collects staff details. Input logic isn’t mixed with calculations or approvals.
    # K.I.S.S: Simple input prompts make it easy to understand and use.'''
    def staff_info(self):
        self.date = input("Enter the Date Of Requisition: ")
        self.staff_id = input("Enter Unique Staff ID: ")
        self.staff_name = input("Enter Staff Name: ")


    # REQUISITION DETAILS
    # Collects item prices and calculates total
    '''# Principles:
    # SRP: Handles only item prices and computes the total; no approval or display logic.
    # K.I.S.S: Simple loop for input collection, easy to follow.
    # D.R.Y: Uses one loop to collect all item prices instead of repeating input logic multiple times.'''

    def requisitions_details(self):
        total = 0
        while True:
            price = input("Enter item price (or 'done'): $ ")
            if price.lower() == "done":
                break
            try:
                total += float(price)
            except:
                print("Invalid number.")
        self.total = total


    # AUTO-APPROVAL
    # Automatically approves requisitions with total < 500
    # Generates approval reference number if approved
    '''# Principles:
    #SRP: Only handles automatic approval logic.
    #Open / Closed: Approval rules can be changed or extended without affecting other parts of the class '''

    def requisition_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
        else:
            self.status = "Pending"


    # MANAGER RESPONSE
    # Manager approves or rejects pending requisitions
    # Updates status and approval reference
    '''# Principles:
    #SRP: Handles only manager decision-making.
    #K.I.S.S: Simple yes/no logic keeps it readable.'''

    def respond_requisition(self):
        if self.status == "Pending":
            decision = input("Manager: Approve? yes/no: ")
            if decision.lower() == "yes":
                self.status = "Approved"
                self.approval_reference_number = f"{self.staff_id}{str(self.requisition_id)[-3:]}"
            elif decision.lower() == "no":
                self.status = "Not approved"
            else:
                print("Wrong input.")
        else:
            print("Already " + self.status)


    # DISPLAY REQUISITION
    # Displays all details of a single requisition
    '''# Principles:
    #SRP: Only responsible for displaying requisition information.
    #Clean Code > Clever Code: Uses simple print statements rather than complex formatting or unnecessary logic.'''

    def display_requisition(self):
        print(f"ID: {self.requisition_id}, Date: {self.date}, Staff: {self.staff_name} ({self.staff_id})")
        print(f"Total: ${self.total}, Status: {self.status}, Approval Ref: {self.approval_reference_number}")


    # REQUISITION STATISTICS
    # Shows summary of all requisitions: total, approved, pending, not approved
    '''# Principle:
    #SRP: Only calculates and displays statistics.
    #D.R.Y: Uses a single loop to count all statuses instead of repeating similar logic for each type'''

    def requisition_statistics(self):
        total_submitted = len(RequisitionSystem.all_requisitions)
        approved = pending = not_approved = 0
        for req in RequisitionSystem.all_requisitions:
            if req.status == "Approved":
                approved += 1
            elif req.status == "Pending":
                pending += 1
            elif req.status == "Not approved":
                not_approved += 1
        print(f"\nTotal: {total_submitted}, Approved: {approved}, Pending: {pending}, Not Approved: {not_approved}")


# MAIN PROGRAM
# Controls workflow: create requisitions, collect info, approve, display, and show statistics
'''# Principles:
#Composition > Inheritance: The main workflow uses instances of RequisitionSystem instead of inheriting from it, keeping design simple.
#K.I.S.S: The workflow is clear—create requisitions, collect info, approve, display, and show statistics.
#Open / Closed: The main program can be extended (e.g., add logging or export) without modifying the class logic.'''

if __name__ == "__main__":
    num_reqs = int(input("How many requisitions? "))
    for i in range(num_reqs):
        req = RequisitionSystem()
        print(f"\nRequisition {i+1}")
        req.staff_info()           # Staff info
        req.requisitions_details()   # Item prices
        req.requisition_approval()   # Auto-approval
        req.respond_requisition()    # Manager decision
        req.display_requisition()   # Display details
        req.requisition_statistics()   # Show summary


REQUISITIONSYSTEM 

The Requisition System is a Python application that can be utilised in maintaining and tracking the staff requisitions in an organisation. 
The system allows the staff to make requisitions with details such as date, staff ID, staff name and the cost of items. 
The system automatically entails the calculation of the total cost of any requisition and decision-making. 
Whether to be auto-approved (when within a certain threshold) or managerially approved, 
managers can accept or reject pending requisitions, and the system maintains a total record of all requisitions that entail the status and approving references.



Use Cases:
Departments or small businesses need to oversee and sanction the purchase requests effectively. 
Learning objectives in learning object-oriented programming and software design principles. 
It can be expanded to larger procurement management systems or database and reporting integrations.



How the System Works
Unique Identification: Every requisition will be identified with a unique ID assigned automatically with a global counter.
Staff Input: When users are making a requisition, they provide their staff information (ID, name, date).
Prices on Items: The users give the prices on requested items and the system sums it up.
Auto-Approval: The system will approve the requisition automatically and raise an approval reference should the total be lower than a set limit.
Managerial Review: In case of a higher value requisition, a manager is free to approve or reject the request.
Display and Statistics: The system shows the detailed data of each requisition and offer.
general statistics of all submissions, approvals, pending, and unapproved requisitions.



Applied Software Design Principles.
K.I.S.S. (Keep It Simple, Stupid): To make the system readable, the system is developed based on simple, clear logic and simple methods.
D.R.Y (Don’t Repeat Yourself): Data is centralised, like the list of all requisitions and approval logic, to prevent the repetition of the code.
Single Responsibility: Every method is devoted to one task, gathering staff information, counting sums, processing approvals, or showing statistics.
Separation of Concerns: The separation of input, processing, approval, and output into functions helps in making the processes clear and maintainable.
Clean Code > Clever Code: The code is easy to understand and maintain due to meaningful names and structures that are easy to read.
Avoid Premature Optimisation: The system puts a high value on correctness and simplicity and employs simple data structures and loops as opposed to any kind of optimization that is not needed.


Example Scenario of Use
A personnel member puts their information and gives the price of items.
The system is used to compute the overall cost.
In case of a small total, the system approves the requisition automatically and issues a reference number.
When the total exceeds, the manager will be in a position to accept or decline it.
The orders of the requisition and the general statistics are presented, which assist the organisation in managing the spending and approvals effectively.

This discussion gives a clear insight into what the code does, how it works and where it can be applied.


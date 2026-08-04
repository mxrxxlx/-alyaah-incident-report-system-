reports = []
cident = []
not_priority = []
descriptions = []
evidences = []
no_status = []

while True:
    print("===== [STUDENT INCIDENT REPORT MANAGEMENT SYSTEM] =====")
    print(" ")
    print("[1] Submit a new incident report")
    print(" ")
    print("[2] View submitted incident reports")
    print(" ")
    print("[3] Update the status of an incident report")
    print(" ")
    print("[4] View report count by status")
    print(" ")
    print("[5] Exit")
    print("========================================================")


    choice = input("Enter your choice (1-5): ")


    if choice == "1":
        print("\n+---- [SUBMIT NEW REPORT] ----+")


        reporter = input("Enter reporter's name: ")


        incident_type = input("Enter incident type (Lost ID, Room issue, Lab Equipment Damage, Bullying): ")


        if incident_type != "Lost ID" and incident_type != "Room issue" and incident_type != "Lab Equipment Damage" and incident_type != "Bullying":
            print("Unsupported incident type.")
        else:
            priority = input("Enter priority level (Low, Medium, High): ")
            description = input("Enter description: ")


            if len(description) > 200:
                print("Description must not exceed 200 characters.")
            else:
                evidence = input("Enter evidence: ")


                reports.append(reporter)
                accident.append(incident_type)
                not_priority.append(priority)
                descriptions.append(description)
                evidence.append(evidence)
                no_status.append("Ongoing")


                print("\nIncident report submitted successfully!")
                print("Assigned Report ID:", len(reports))
                print("Current Status: Ongoing")


    elif choice == "2":
        print("\n+---- VIEW SUBMITTED REPORTS ----+")


        if len(reports) == 0:
            print("No incident reports submitted yet.")
        else:
            i = 0
            while i < len(reports):
                print("\nReport ID:", i + 1,"\nReporter:", reports[i],"\nIncident Type:", accident[i],"\nPriority Level:", not_priority[i],"\nDescription:", descriptions[i],"\nEvidence:", evidence[i],"\nStatus:", no_status[i])
                i += 1
    elif choice == "3":
        print("\n+---- UPDATE REPORT STATUS ----+")


        if len(reports) == 0:
            print("No reports available.")
        else:
            report_id = int(input("Enter Report ID: "))


            if report_id >= 1 and report_id <= len(reports):
                new_status = input("Enter new status (Ongoing, Resolved, Closed): ")
                no_status[report_id - 1] = new_status
                print("Status updated successfully.")
            else:
                print("Invalid Report ID.")


    elif choice == "4":
        print("\n+---- REPORT COUNT BY STATUS ----+")


        ongoing = 0
        resolved = 0
        closed = 0


        i = 0
        while i < len(no_status):
            if no_status[i] == "Ongoing":
                ongoing += 1
            elif no_status[i] == "Resolved":
                resolved += 1
            elif no_status[i] == "Closed":
                closed += 1
            i += 1
        print("Ongoing :", ongoing,"\nResolved:", resolved,"\nClosed  :", closed)


    elif choice == "5":
        print("Exiting the system... End.")
        break
    else:
        print("Invalid choice.")

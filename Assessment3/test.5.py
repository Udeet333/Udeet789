def staff_info(counter_id=10000):
    name= input("Enter your name: ")
    date= input("Enter a date: ")
    id= input("Enter your staff id: ")
    
    Id= counter_id+1

    staff_data={
    "Date": date,
    "ID": id,
    "Name": name,
    "Req_ID": Id
    }
    return staff_data

def main(staff_data):
    print(f"\n Printing Staff Information")
    print(f"Date:{staff_data['Date']}")
    print(f"Staff ID:{staff_data['ID']}")
    print(f"Staff Name:{staff_data['Name']}")
    print(f"Requisition ID:{staff_data['Req_ID']}")
staff_data=staff_info()
main(staff_data)

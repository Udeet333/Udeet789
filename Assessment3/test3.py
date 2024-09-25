def staff_info(counter_id=10000):
    staff_name= input("Enter your name: ")
    date= input("Enter a date: ")
    staff_id= input("Enter your staff id: ")
    requisition_id= counter_id+1

    staff_information={
    "Date": date,
    "ID": staff_id,
    "Name": staff_name,
    "Req_ID": requisition_id
    }
    return staff_information

def requisitions_total():
    total_amount=0.00
    while True:
        item_name= input("Enter the item name(or type 'finish' to end): ")
        if item_name.lower()== "finish":
            break
        item_price= float(input("Enter the item price(or type'finish' to end): "))
        try:
         total_amount+= item_price
        except ValueError:
         print("Please Enter a valid Number")
    print(f"The total price of items:${total_amount:.2f}")

def requisition_approval():
    total_amount=0.00
    counter_id= 10000

    while True:
        item_name= input("Enter the item name(or type 'finish' to end): ")
        if item_name.lower()== "finish":
            break
        
        try:
         item_price= float(input("Enter the item price(or type'finish' to end): ")) 
         total_amount+= item_price
        except ValueError:
         print("\nPlease Enter a valid Number")
    print(f"The total price of items is:${total_amount:.2f}")

    if total_amount < 500:
        Status = "Approved"
        requisition_id= counter_id+1
        print(f"Status:{Status}")
        print(f"Approval Reference Nmuber:{requisition_id}")
    else:
        Status ="Pending"
        requisition_id= None
   
    return Status, requisition_id,total_amount


def create_detailed_report(total_amount,staff_information,status,requisition_id):

    print("Printing Requistions:")
    print(f"Date:{staff_information['Date']} ")
    print(f"Requisition_id:{staff_information['Req_ID']} ")
    print(f"Staff ID: {staff_information['ID']}")
    print(f"Staff Name:{staff_information['Name']}")
    print(f"Total:${total_amount:.2f}")
    print(f"Status:{status}")
    print(f"Approval Refrence Number:{requisition_id}")

def main():
    staff_information = staff_info()
    total_amount,status,requisition_id = requisition_approval()
    create_detailed_report(staff_information,total_amount,status,requisition_id)

main()

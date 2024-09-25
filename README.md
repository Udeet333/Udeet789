def collect_user_data(id_counter):
    user_name=input("Please enter your name:")
    user_age=input("Please enter your age :")
    user_email=input("Please enter your email:")

    unique_id = id_counter+1
    id_counter=unique_id
    print("User information: ")
    print(f"Name: {user_name}")
    print(f"Age: {user_age}")
    print(f"Email: {user_email}")
    print(f"Unique_id: {id_counter}")

    return user_age,user_email,user_name,id_counter

def calculate_total_amount():
    total_amt=0.0
    while True:
        price_input=input("Enter the name of an item (or type 'finish' to end):")

        if price_input.lower()=='finish':
            break

        try:
            price=float(input(f"enter the price of item'{price_input}':"))
            total_amt+=price
        except ValueError:
            print("Invalid input, Please enter a value number.")

    return total_amt


def categorize_request(total_amt):
    
    if total_amt<150:
        category="Low"
        recommendation= "Proceed with stanrdard processing"
        print(recommendation)

    else:
        category = " High "
        recommendation = " Review for potential discount "
        print(recommendation,category)

    
    return category,recommendation

        
        
def create_detailed_report(user_age,user_email,user_name,id_counter,total_amt,category, recommendation):
    print("Detailed Report")
    print(f"Unique Id:{id_counter}")
    print(f"User Name:{user_name}")
    print(f"Age:{user_age}")
    print(f"Email:{user_email}")
    print(f"Total Amount:$ {total_amt: .2f}")
    print(f"Category:{category}")
    print(f"Recomendation:{recommendation}")

def main():
    id_counter=5000
    id_counter,user_name,user_age,user_email = collect_user_data(id_counter)
    total_amt=calculate_total_amount()
    category,recommendation=categorize_request(total_amt)
    create_detailed_report(user_age,user_email,user_name,id_counter,total_amt,category, recommendation)
main()





To enhance the design of the user data collection and reporting program using software design principles, consider the following suggestions:

1.Single Responsibility Principle (SRP)
Each function should have one clear responsibility. For example, you could break down some of the larger functions into      smaller, more focused ones:

- 'collect_user_data'- Only collects user data.
- 'calculate_total_amount'- Only calculates and returns the total amount.
- 'categorize_request' - Only categorizes the total amount and provides recommendations.
- 'create_detailed_report'- Only formats and outputs the report.

2.Open/Closed Principle (OCP)
Your functions should be open for extension but closed for modification. If you want to change how data is collected or reported, consider using interfaces or configuration objects that can be modified without changing the core logic.

3.DRY (Don't Repeat Yourself)
Avoid code duplication. If there are similar input prompts or print statements, consider creating utility functions to handle them. This helps maintainability and reduces the chances of errors.

4.KISS (Keep It Simple, Stupid)
Ensure your functions are not overly complex. Each function should be easy to understand and follow. If a function is too long or complex, break it down into smaller parts.

 5.Encapsulation
Group related data and functions together. You could encapsulate user data and related operations into a `User` class. This would keep related information and functionality together, making the code more organized and easier to manage.

6.Separation of Concerns
 Different concerns of the program (data collection, processing, reporting) should be separated. Consider creating           classes or modules that handle different parts of the functionality.


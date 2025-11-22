DATA_FILE = "finance_data.txt"
EXPENSE_CATEGORIES = ["Rent", "Food", "Transport", "Fun", "Bills", "Other"]
def manual_strip_text(text):
    if len(text) == 0:
        return ""
        
    bad_chars = " \n\t\r"
    
    start_index = 0
    while start_index < len(text):
        is_bad = False
        for char in bad_chars:
            if text[start_index] == char:
                is_bad = True
        
        if not is_bad:
            break 
        start_index += 1
    end_index = len(text) - 1
    while end_index >= 0:
        is_bad = False
        for char in bad_chars:
            if text[end_index] == char:
                is_bad = True
                
        if not is_bad:
            break 
        end_index -= 1
        
    if start_index > end_index:
        return ""
        
    return text[start_index : end_index + 1]

def manual_split_text(text, delimiter):
    parts_list = []
    current_word = ""
    
    for char in text:
        if char == delimiter:
            parts_list.append(current_word)
            current_word = ""
        else:
            current_word += char
    parts_list.append(current_word)
    
    return parts_list

# --- PART 1: SAVING AND LOADING DATA ---

def convert_text_to_data(line):
    clean_line = manual_strip_text(line)
    parts = manual_split_text(clean_line, '|')
    
    if len(parts) < 3 + len(EXPENSE_CATEGORIES):
        return None
        
    record = {
        "date": parts[0],
        "income": float(parts[1]),
        "total_saved": float(parts[2]),
        "expenses": {}
    }
    
    start_index = 3
    for i in range(len(EXPENSE_CATEGORIES)):
        category_name = EXPENSE_CATEGORIES[i]
        value_text = parts[start_index + i]
        record["expenses"][category_name] = float(value_text)
        
    return record

def load_data():
    default_data = {
        "income": 0.0,
        "goal_name": "General Savings",
        "goal_target": 0.0,
        "records": []
    }

    file_handle = open(DATA_FILE, "a+")
    file_handle.seek(0)
    content = file_handle.read()
    file_handle.close()
    

    if len(manual_strip_text(content)) == 0:
        return default_data

    lines = manual_split_text(content, '\n')
    
    if len(lines) < 3:
        return default_data
        

    loaded_data = {
        "goal_name": manual_strip_text(lines[0]),
        "goal_target": float(manual_strip_text(lines[1])),
        "income": float(manual_strip_text(lines[2])),
        "records": []
    }
    

    for i in range(3, len(lines)):
        line = lines[i]

        if len(manual_strip_text(line)) > 0:
            rec = convert_text_to_data(line)
            if rec is not None:
                loaded_data["records"].append(rec)
                
    return loaded_data

def save_data(data):
    file_handle = open(DATA_FILE, "w")
    
    file_handle.write(str(data["goal_name"]) + "\n")
    file_handle.write(str(data["goal_target"]) + "\n")
    file_handle.write(str(data["income"]) + "\n")

    for rec in data["records"]:
        line = rec["date"] + "|"
        line += str(rec["income"]) + "|"
        line += str(rec["total_saved"]) + "|"
        
        for cat in EXPENSE_CATEGORIES:
            val = rec["expenses"][cat]
            line += str(val) + "|"
            

        line = line[:-1] + "\n"
        file_handle.write(line)
        
    file_handle.close()
    print(" [System] Saved successfully.")

# --- PART 2: CHECKING INPUT ---

def is_number_valid(text):

    text = manual_strip_text(text)
    
    if len(text) == 0:
        return False
        
    dot_count = 0
    allowed_chars = "0123456789."
    
    for char in text:
        if char not in allowed_chars:
            return False
        if char == '.':
            dot_count += 1
            
    if dot_count > 1:
        return False
        
    return True

def get_number_input(prompt):
    while True:
        user_entry = input(prompt)
        if is_number_valid(user_entry):

            value = float(manual_strip_text(user_entry))
            if value >= 0:
                return value
            else:
                print(" -> Error: Positive numbers only.")
        else:
            print(" -> Error: Not a valid number.")

# --- PART 3: MATH AND REPORTS ---

def calculate_totals(data):
    if len(data["records"]) == 0:
        return None

    current_record = data["records"][-1]
    monthly_income = current_record["income"]
    expenses_dict = current_record["expenses"]
    
    total_spent = 0.0
    for category in expenses_dict:
        total_spent += expenses_dict[category]
        
    money_saved_this_month = monthly_income - total_spent
    
    percent_saved = 0.0
    if monthly_income > 0:
        percent_saved = (money_saved_this_month / monthly_income) * 100
        
    total_in_bank = current_record["total_saved"]
    money_left_to_save = data["goal_target"] - total_in_bank
    
    if money_left_to_save <= 0:
        status_message = "Goal Done!"
    elif money_saved_this_month <= 0:
        status_message = "Not saving money"
    else:
        months_left = int(money_left_to_save / money_saved_this_month)
        status_message = str(months_left) + " months"

    return {
        "total_spent": total_spent,
        "money_saved": money_saved_this_month,
        "percent_saved": percent_saved,
        "status_message": status_message,
        "total_in_bank": total_in_bank
    }

# --- PART 4: MAIN MENUS ---

def menu_setup_goal(data):
    print("\n--- Setup Financial Goal ---")
    data["goal_name"] = input(" Enter Goal Name: ")
    data["goal_target"] = get_number_input(" Enter Target Amount: ")
    data["income"] = get_number_input(" Enter Monthly Income: ")
    print(" -> Goal setup complete.")
    return data

def menu_add_expenses(data):
    print("\n--- Add Monthly Expenses ---")
    if data["income"] == 0:
        print(" -> Warning: Income is 0. Please setup goal first.")
        data["income"] = get_number_input(" Enter Monthly Income: ")

    date_entry = input(" Enter Date (e.g., 2023-10-01): ")
    if len(manual_strip_text(date_entry)) == 0:
        date_entry = "Unknown-Date"
    else:
        date_entry = manual_strip_text(date_entry)

    current_expenses = {}
    for cat in EXPENSE_CATEGORIES:
        amount = get_number_input(f" Enter amount for '{cat}': ")
        current_expenses[cat] = amount
        
    previous_savings = 0.0
    if len(data["records"]) > 0:
        previous_savings = data["records"][-1]["total_saved"]
        
    month_total_expense = 0.0
    for val in current_expenses.values():
        month_total_expense += val
        
    month_savings = data["income"] - month_total_expense
    new_total_saved = previous_savings + month_savings
    
    new_record = {
        "date": date_entry,
        "income": data["income"],
        "expenses": current_expenses,
        "total_saved": new_total_saved
    }
    
    data["records"].append(new_record)
    print(" -> Record added.")
    return data

def menu_view_report(data):
    results = calculate_totals(data)
    
    if results is None:
        print("\n -> No records found.")
    else:
        print("\n" + "="*30)
        print(" MONEY REPORT ".center(30))
        print("="*30)
        print(f" Goal:         {data['goal_name']}")
        print(f" Target:       {data['goal_target']}")
        print("-" * 30)
        print(f" Spent:        {results['total_spent']}")
        print(f" Saved (New):  {results['money_saved']}")
        print(f" Saved (%):    {results['percent_saved']:.2f}%")
        print("-" * 30)
        print(f" Total Saved:  {results['total_in_bank']}")
        print(f" Time Left:    {results['status_message']}")
        print("="*30)

# --- START THE PROGRAM ---

def main():
    user_data = load_data()
    
    while True:
        print("\n" + "~"*40)
        print(" FINANCE TRACKER ".center(40))
        print("~"*40)
        print(" 1. Setup Goal")
        print(" 2. Add Expenses")
        print(" 3. View Report")
        print(" 4. Save & Exit")
        
        choice = input("\n Select (1-4): ")
        choice = manual_strip_text(choice)
        
        if choice == '1':
            user_data = menu_setup_goal(user_data)
        elif choice == '2':
            user_data = menu_add_expenses(user_data)
        elif choice == '3':
            menu_view_report(user_data)
        elif choice == '4':
            save_data(user_data)
            break
        else:
            print(" -> Invalid choice.")

if __name__ == "__main__":
    main()
import csv

def generate_question_answer_pairs(csv_file):
    pairs = []

    # Open the CSV file and read data
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            provider_name = row['Provider Name']
            address = row['Address 1']
            city = row['City']
            state = row['State']
            zipcode = row['Zip']
            
            # Generate questions and answers based on available information
            questions = [
                f"What services does {provider_name} provide?",
                f"Do they offer Test to Treat services?",
                f"Which COVID-19 medications are available at {provider_name}?",
                f"Is telehealth available at {provider_name}?",
                f"Are outpatient COVID-19 medications available at {provider_name}?"
            ]
            
            answers = [
                f"{provider_name} provides pharmacies and clinics with safe and effective COVID-19 medications. These medications require a prescription from a healthcare provider.",
                "Some locations, known as Test to Treat sites, give you the option to get tested, get assessed by a healthcare provider, and receive treatment – all in one visit.",
                f"{provider_name} has reported inventory of Paxlovid (nirmatrelvir packaged with ritonavir), Lagevrio (molnupiravir), and Veklury (Remdesivir) within at least the last two months.",
                f"{provider_name} may offer telehealth services. Please contact the provider for more information.",
                "Outpatient COVID-19 medications may be available at additional locations not listed on this website."
            ]
            
            # Append question-answer pairs to the list
            for question, answer in zip(questions, answers):
                pairs.append({'question': question, 'answer': answer})

    return pairs

def write_to_csv(question_answer_pairs, output_file):
    # Define fieldnames for the CSV file
    fieldnames = ['question', 'answer']

    # Write question-answer pairs to a new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(question_answer_pairs)

# Example usage: generating question-answer pairs from CSV file and writing to a new CSV file
input_csv_file = 'preprocess/COVID-data.csv'  # Replace 'your_input_file.csv' with the path to your input CSV file
output_csv_file = 'preprocess/generated_pairs.csv'  # Path to the output CSV file
question_answer_pairs = generate_question_answer_pairs(input_csv_file)
write_to_csv(question_answer_pairs, output_csv_file)

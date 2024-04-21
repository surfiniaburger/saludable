import csv

def generate_location_question_answer_pairs(csv_file):
    pairs = []

    # Open the CSV file and read data
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Group providers by location (city, state, or ZIP code)
        location_groups = {}
        for row in reader:
            city = row['City']
            state = row['State']
            zipcode = row['Zip']
            provider_name = row['Provider Name']

            # Create location key based on available information
            location = ""
            if city:
                location += city
            if state:
                if location:
                    location += ", "
                location += state
            if zipcode:
                if location:
                    location += ", "
                location += zipcode

            # Append provider to location group
            if location not in location_groups:
                location_groups[location] = []
            location_groups[location].append(provider_name)

        # Generate question-answer pairs for each location group
        for location, providers in location_groups.items():
            question = f"What healthcare providers are available"
            if location:
                question += f" in {location}?"
            else:
                question += "?"
            answer = f"The following healthcare providers are available"
            if location:
                answer += f" in {location}:"
            else:
                answer += ":"
            answer += f" {', '.join(providers)}"
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

# Example usage: generating location-based question-answer pairs from CSV file and writing to a new CSV file
input_csv_file = 'preprocess/COVID-data.csv'
output_csv_file = 'preprocess/location_based_pairs.csv'
location_question_answer_pairs = generate_location_question_answer_pairs(input_csv_file)
write_to_csv(location_question_answer_pairs, output_csv_file)


import pandas as pd
import json

# Path to the local JSONL file
file_path = "FaVIQ/dev_20.jsonl"

# Read JSONL data from the local file
with open(file_path, 'r', encoding='utf-8') as file:
    data_lines = file.readlines()

# Parse JSONL data
rows = []
for line in data_lines:
    json_data = json.loads(line)
    claim = json_data["claim"] 
    question = json_data["question"] 
    answer = json_data["answer"]
   

    rows.append({"query": claim, "question": question, "answer": answer})

# Create a DataFrame
df = pd.DataFrame(rows)

# Save DataFrame to CSV
df.to_csv("output.csv", index=False)

print("CSV file created successfully.")

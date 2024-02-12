import pandas as pd
import json
import requests

# URL of the JSONL file
url = "https://raw.githubusercontent.com/salesforce/DialFact/master/data/valid_split.jsonl"

# Download JSONL data
response = requests.get(url)
data_lines = response.text.splitlines()

# Parse JSONL data
rows = []
for line in data_lines:
    json_data = json.loads(line)
    context = " ".join(json_data["context"]) 
    response = json_data["response"]
    wiki_link = json_data["evidence_list"][0][1]
   

    rows.append({"question": context, "answer": response, "wiki": wiki_link})

# Create a DataFrame
df = pd.DataFrame(rows)

# Save DataFrame to CSV
df.to_csv("output.csv", index=False)

print("CSV file created successfully.")

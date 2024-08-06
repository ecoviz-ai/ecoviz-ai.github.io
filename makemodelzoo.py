import pandas as pd
import os
# import shutil

# Path to the CSV file
csv_path = 'modelzoo/ModelZoo.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(csv_path)
print(df.columns)

# Base directory for the models
base_dir = './models'

# Iterate over each row in the DataFrame to create directories and files
for index, row in df.iterrows():
    model_dir = os.path.join(base_dir, row['Model Name'].replace(' ', '_'))
    os.makedirs(model_dir, exist_ok=True)
    
    # Path to Quarto document and image
    qmd_filename = os.path.join(model_dir, 'index.qmd')
    original_image_path = row['Files & media']
    image_filename = os.path.join(model_dir, f"{row['Model Name'].replace(' ', '_')}.png")
    
    # Copy the image file to the new location
    # shutil.copy(original_image_path, image_filename) # Uncomment and use the actual path if you handle image files

    # Create Quarto document content
    document = f"""
---
title: "{row['Model Name']}"
description: "{row['Description']}"
image: {row['Model Name'].replace(' ', '_')}.png
---

| Model metadata             | Value                               |
|----------------------------|------------------------------------|
| {{{{< fa cube >}}}} Tool Type | [{row['Tool Type']}]{{.tool_type .tool_type_pkglib}} |
| {{{{< fa tasks >}}}} Broad Task | {row['Broad task']} |
| {{{{< fa filter >}}}} Specific Task | {row['Specific task']} |
| {{{{< fa book >}}}} Description | {row['Description']} |
| {{{{< fa check-circle >}}}} Task Specific | {row['Task specific']} |
| {{{{< fa globe >}}}} Ecology Specific | {row['Ecology specific']} |
| {{{{< fa code >}}}} Language(s) | {row['Language(s)']} |
| {{{{< fa clock >}}}} Last Edited Time | {row['Last edited time']} |
| {{{{< fa book-open >}}}} Related Publication(s) | [{row['Related publication (with DOI)']}]({row['Related publication (with DOI)']}) |
| {{{{< fa puzzle-piece >}}}} Dependencies | {row['Dependencies (light gray for signal processing and dark gray for code/compiling, purple for viz, pink for interactivity, brown for domain-specific data processing)']} |
| {{{{< fa github >}}}} Tool URL (Github etc.) | [{row['Tool URL (Github or Link)']}]({row['Tool URL (Github or Link)']}) |
| {{{{< fa sync-alt >}}}} Last Update (time ago) | {row['Last Update (time since)']} |
| {{{{< fa balance-scale >}}}} License | {row['License']} |
| {{{{< fa user >}}}} Contact Name | {row['Contact name']} |
| {{{{< fa envelope >}}}} Contact Email | [{row['Contact email']}]({row['Contact email']}) |
| {{{{< fa phone >}}}} Contact Responsiveness | {row['Contact responsiveness']} |
| {{{{< fa hugging >}}}} HuggingFace URL | [{row['HuggingFace URL']}]({row['HuggingFace URL']}) |
| {{{{< fa cog >}}}} Reproducibility Method | {row['Reproducibility methods']} |
| {{{{< fa image >}}}} Image | ![{row['Model Name']}]({row['Model Name'].replace(' ', '_')}.png) |
"""

    # Write the Quarto document
    with open(qmd_filename, "w") as file:
        file.write(document)

    print(f"Folder and document for {row['Model Name']} created at {model_dir}.")

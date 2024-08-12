import pandas as pd
import os
# import shutil

# Path to the CSV file
csv_path = 'media/communities/communities-of-practice.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(csv_path)
print(df.columns)

# Base directory for the models
base_dir = './communities'

def transform_tags(tags):
    return [tag.strip() for tag in tags.split(',')]

# Iterate over each row in the DataFrame to create directories and files
for index, row in df.iterrows():
    community_dir = os.path.join(base_dir, row['Community Name'].replace(' ', '_'))
    community_mediadir = os.path.join(base_dir, "communities")
    os.makedirs(community_dir, exist_ok=True)
    
    # Path to Quarto document and image
    qmd_filename = os.path.join(community_dir, 'index.qmd')
    original_image_path = row['Graphics']
    image_filename = os.path.join(community_mediadir, f"{row['Community Name'].replace(' ', '')}.png")
    
    # Copy the image file to the new location
    # shutil.copy(original_image_path, image_filename) # Uncomment and use the actual path if you handle image files

    # Create Quarto document content
    document = f"""
---
title: "{row['Community Name']}"
description: "{row['Description']}"
categories: ["{row['Tags'].replace(', ', '", "')}"]
image: ../../media/communities/{row['Community Name'].replace(' ', '')}.png
---

![](../../media/communities/{row['Community Name'].replace(' ', '')}.png){{.custom_image}}

| Community Details             | Information                                                                                                     |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| {{{{< fa users >}}}} Community Name       | {row['Community Name']}                                                                                       |
| {{{{< fa book >}}}} Description           | {row['Description']}                                                                                          |
| {{{{< fa tags >}}}} Tags                  | {row['Tags']}                                                                                                 |
| {{{{< fa link >}}}} Website               | [{row['Website']}](https://{row['Website']})                                                                    |
| {{{{< fa linkedin >}}}} LinkedIn          | [{row['LinkedIn']}](https://{row['LinkedIn']})                                                                  |                                                                             |
| {{{{< fa building >}}}} Organizations     | {row['Organizations']}                                                                                        |
| {{{{< fa hand-holding-usd >}}}} Funding   | {row['Funding Organizations']}                                                                                |

"""

    # Write the Quarto document
    with open(qmd_filename, "w") as file:
        file.write(document)

    print(f"Folder and document for {row['Community Name']} created at {community_dir}.")

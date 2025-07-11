import zipfile
import os

with zipfile.ZipFile('period_03.zip', 'r') as zip_ref:
    zip_ref.extractall('period_03_data')

# Check extracted files
print(os.listdir('period_03_data'))
API Data Extractor (Python Project)
Project Description
This project is a simple API-based data extraction tool built using Python. It fetches user data
from a public API and converts the JSON response into a structured CSV file.
The project demonstrates how to work with APIs, handle JSON data, and store it in a readable
format.
---
Features
- Fetch data from a public API
- Convert JSON data to CSV format
- Handle missing values safely
- Save raw API response as JSON file
- Measure execution time
---
Technologies Used
- Python
- Requests Library
- CSV Module
- JSON Module
---
API Used
- https://jsonplaceholder.typicode.com/users
---
How to Run
1. Install required library:
pip install requests
2. Run the Python file:
python API.py
---
Output Files
- "raw_response.json" → Full API response
- "users.csv" → Processed user data
---
Sample Output (CSV Columns)
- ID
- Name
- Email
- City
- Company
---
Example Output
Data Saved Successfully!
Total Records: 10
Time Taken: <execution time>
Output File: users.csv
---
Learning Outcomes
- Understanding REST API calls
- Working with JSON data
- File handling in Python
- Data processing and transformation
---
Conclusion
This project is a beginner-friendly introduction to backend development concepts using Python
and APIs.
---
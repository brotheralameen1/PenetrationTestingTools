import requests
from bs4 import BeautifulSoup

def handle_reopened_report(report_id):
    # Retrieve the report details from HackerOne's API
    api_url = f"https://api.hackerone.com/v1/reports/{report_id}"
    response = requests.get(api_url, headers={'Authorization': 'Bearer <your_api_key>'})
    report_data = response.json()

    # Check if the report is still a duplicate
    if report_data['data']['attributes']['state'] == 'duplicate':
        print(f"Report {report_id} is still a duplicate. Please investigate further.")
        return

    # If the report is confirmed, re-assign it to the appropriate team member or escalate
    assignee_id = '<team_member_id>'  # Replace with the ID of the appropriate team member
    data = {
        'data': {
            'type': 'assignee',
            'attributes': {
                'assignee_id': assignee_id
            }
        }
    }
    response = requests.post(f"{api_url}/assignee", headers={'Authorization': 'Bearer <your_api_key>'}, json=data)

    if response.status_code == 200:
        print(f"Report {report_id} has been reassigned to team member {assignee_id}.")
    else:
        print(f"Failed to reassign report {report_id}. Error: {response.text}")

    # Update the report with any new information or changes
    report_url = report_data['data']['links']['self']
    response = requests.get(report_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract new information or changes from the report
    new_info = extract_new_info(soup)

    # Update the report with the new information
    update_data = {
        'data': {
            'type': 'report',
            'attributes': {
                'additional_info': new_info
            }
        }
    }
    response = requests.patch(report_url, json=update_data, headers={'Authorization': 'Bearer <your_api_key>'})

    if response.status_code == 200:
        print(f"Report {report_id} has been updated with new information.")
    else:
        print(f"Failed to update report {report_id}. Error: {response.text}")

def extract_new_info(soup):
    # Implement logic to extract new information or changes from the report
    # This can involve parsing the HTML structure or extracting specific elements
    # For example, you could extract the updated description or additional details
    new_info = 'Updated description: ...'
    return new_info

# Example usage
report_id = '1234'  # Replace with the ID of the reopened report
handle_reopened_report(report_id)


# Python program to read CSV file line by line
# import necessary packages
import csv
import json

data = []
weight = 1.0
pk = 255

with open('State_PKs_Score.csv') as file_obj:

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)
    # Skip header row
    next(reader_obj)

    # Iterate over each row in the csv
    # file using reader object
    for row in reader_obj:
        state_num = row[2]

        for issue in range(6, 11):

            issue_score = row[issue-2]
            # print(issue_score)
            pk += 1

            state_issue = {"model": "campaign_trail.state_issue_score", "pk": int(pk), "fields": {"state": int(state_num), "issue": int(issue), "state_issue_score": float(issue_score), "weight": float(weight)}}

            data.append(state_issue)


json_str = json.dumps(data)
json_str = json_str.replace('"', '\\"')
output_str = f'campaignTrail_temp.state_issue_score_json = JSON.parse(\"{json_str}\");'

f = open("state_issue_score_json_code.txt", "w")
f.write(output_str)
f.close()

print("State issue score json for code 2 output successfully \nSee file 'state_issue_score_json_code.txt'")


# import necessary packages
import json

data = []
issues = ["Currency", "Tariffs", "Business", "Labor", "Imperialism"]
stances = {
    "Currency": ["Fanatic Pro-Gold", "Pro-Gold", "Bland-Allison", "Moderate", "International Agreement", "Silverite", "Fanatic Silverite"],
    "Tariffs": ["Fanatic Protectionist", "Protectionist", "Leans Protectionist", "Moderate", "Leans Free Trade", "Free Trade", "Fanatic Free Trade"],
    "Business": ["Cronyism", "Non-Interventionist", "Moderate", "Leans Regulatory", "Regulatory", "Trust-Busting", "Fanatic Trust-Busting"],
    "Labor": ["Strong Crackdown", "Crackdown", "Conservative", "Moderate", "Sympathetic", "Unionized", "Strongly Unionized"],
    "Imperialism": ["Expansionist", "Imperialist", "Exceptionalist", "Leans Exceptionalist", "Leans Anti-Imperialist", "Anti-Imperialist", "Pacifist"]
}
null = None

for pk in range(6, 11):

    name = issues[pk-6]
    stance = stances[name]

    state_issue = {"model": "campaign_trail.issue", "pk": int(pk), "fields": {"name": name, "description": null, "stance_1": stance[0], "stance_desc_1": null, "stance_2": stance[1], "stance_desc_2": null, "stance_3": stance[2], "stance_desc_3": null, "stance_4": stance[3], "stance_desc_4": null, "stance_5": stance[4], "stance_desc_5": null, "stance_6": stance[5], "stance_desc_6": null, "stance_7": stance[6], "stance_desc_7": null, "election": 5}}

    print(state_issue)
    data.append(state_issue)


json_str = json.dumps(data)
json_str = json_str.replace('"', '\\"')
output_str = f'campaignTrail_temp.issues_json = JSON.parse(\"{json_str}\");'

f = open("issues_json_code.txt", "w")
f.write(output_str)
f.close()

print("Issues json for code 2 output successfully \nSee file 'issues_json_code.txt'")

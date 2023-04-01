import csv

stand = [-1, -0.5, -0.25, 0, 0.25, 0.5, 1]
currency = ["Fanatic Pro-Gold", "Pro-Gold", "Bland-Allison", "Moderate", "International Agreement", "Silverite", "Fanatic Silverite"]
tariffs = ["Fanatic Protectionist", "Protectionist", "Leans Protectionist", "Moderate", "Leans Free Trade", "Free Trade", "Fanatic Free Trade"]
business = ["Cronyism", "Non-Interventionist", "Moderate", "Leans Regulatory", "Regulatory", "Trust-Busting", "Fanatic Trust-Busting"]
labor = ["Strong Crackdown", "Crackdown", "Conservative", "Moderate", "Sympathetic", "Unionized", "Strongly Unionized"]
imperialism = ["Expansionist", "Imperialist", "Exceptionalist", "Leans Exceptionalist", "Leans Anti-Imperialist", "Anti-Imperialist", "Pacifist"]


with open('../State_PKs_Orginial.csv') as file_obj:

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)
    headers = next(reader_obj)
    # print(headers)

    with open("State_PKs_Score.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        # Iterate over each row in the csv
        # file using reader object
        for row in reader_obj:
            # print(row)
            currencyStance = row[4]
            tariffStance = row[5]
            businessStance = row[6]
            laborStance = row[7]
            imperialismStance = row[8]

            # try:
            currencyScore = stand[currency.index(currencyStance)]
            tariffsScore = stand[tariffs.index(tariffStance)]
            businessScore = stand[business.index(businessStance)]
            laborScore = stand[labor.index(laborStance)]
            imperialismScore = stand[imperialism.index(imperialismStance)]

            data = {headers[0]: row[0], headers[1]: row[1], headers[2]: row[2], headers[3]: row[3], headers[4]: currencyScore, headers[5]: tariffsScore, headers[6]: businessScore, headers[7]: laborScore, headers[8]: imperialismScore}
            # print(data)

            writer.writerow(data.values())
            # except ValueError:
            #     print(f"Error, invaild index")
            #     print(row)


print("csv with score output successfully \nSee file 'State_PKs_Score.csv'")




import requests

def Api_Url():
    try:
        with open("Api.txt", 'r') as file:
            Api_url = file.readline().strip()
            if not Api_url:
                print("File is empty")
                return None
            return Api_url

    except Exception as ex:
        print("There is an Error", ex)
        return None
     
    except FileNotFoundError:
        print("Error: File not found")
        return None
    

def FetchLive(Api_url):
    try:
        response = requests.get(Api_url)
        if response.status_code != 200:
            print("Error: ", response.status_code)
            print("Response: ", response.text)
            return None
        return response.json()
    except requests.exceptions.RequestException as ex:
        print("There is a Network error")
        print("Details: ", ex)
        return None

def PrintStatus(x):
    if not x:
        print("Nothing to Display!")
        return

    for key, value in x.items():
        if key not in ["data", "apikey"]:
            print(key, ":", value)

def MatchDetails(Api_url):
    try:
        response = requests.get(Api_url)
        if response.status_code == 200:
            data = response.json()  

            if data.get("status") == "success" and "data" in data and data["data"]:
                list = data["data"]

                for match in list:
                    print("Match:", match.get("name", "N/A"))
                    print("Status:", match.get("status", "N/A"))
                    print("Venue:", match.get("venue", "N/A"))
                    print("Date:", match.get("date", "N/A"))
                    print("-" * 30)

                    scores = match.get("score", [])
                    if scores:
                        print(" Score Details:")
                        for inning in scores:
                            print("Inning:", inning.get("inning", "N/A"))
                            print("Runs:", inning.get("r", "N/A"))
                            print("Wickets:", inning.get("w", "N/A"))
                            print("Overs:", inning.get("o", "N/A"))
                            print("  " + "-" * 53)
                    else:
                        print("No details available")
                        print("-" * 50)
            else:
                print("There are no live matches")

        else:
            print("Error, failed to fetch data. Status code:", response.status_code)
            print("Response:", response.text)

    except requests.exceptions.RequestException as ex:
        print("Network error occurred:", ex)

url = Api_Url()
print("Api url:", url)

if url:
    data = FetchLive(url)
    if data is None:
        print("Cant get any data")
    else:
        PrintStatus(data)
        MatchDetails(url)
else:
    print("There is no Api URL")

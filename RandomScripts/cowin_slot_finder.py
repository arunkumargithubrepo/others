import requests
import datetime
import json
# import pandas as pd
from time import sleep
from playsound import playsound

# Important Variables
# 0 = Search entire state, 1 = Search only a single district
method = 1

# Set state code or district code 0 to query state and district code list
state_code = 0
district_code = 571

# Set your age
age = 18

# Optional Variables
# Print extra information? (like slots not available on DD-MM-YYYY) (0=No and 1=Yes)
print_detailed = 1

# Number of days to check in advance
numdays = 3


# Check variables
def printcodes():
    for state_code in range(1, 40):
        print("State code: ", state_code)
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code))
        json_data = json.loads(response.text)
        for i in json_data["districts"]:
            print(i["district_id"], '\t', i["district_name"])
        print("\n")


if method == 0:
    if state_code == 0:
        printcodes()
    elif state_code not in range(1, 40):
        raise Exception("State code not in range: 1-40")
elif method == 1:
    if district_code == 0:
        printcodes()
else:
    raise Exception("Method option not in range (0-1)")

# Script
# Find today's date
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]


def checkdistrict(dist_id):
    global print_detailed
    global age
    none_found = 1
    slots_age = 0
    while slots_age == 0:
        for INP_DATE in date_str:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/" \
                  "calendarByDistrict?district_id={}&date={}".format(dist_id, INP_DATE)
            response = requests.get(url)
            if response.ok:
                slots_age = 0
                resp_json = response.json()
                # print(json.dumps(resp_json, indent = 1))
                if resp_json["centers"]:
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if (session["min_age_limit"] <= age) and (session["available_capacity"] > 0):
                                slots_age = 1
                                none_found = 0
                                print()
                                print("\t", INP_DATE)
                                print("\t", center["name"])
                                print("\t Pincode:", center["pincode"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if session["vaccine"] != '':
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\t Paid: ", center["fee_type"])
                                playsound('TF013.WAV')

            if print_detailed == 1:
                if slots_age == 0:
                    print("\tNo available slots on {} for your age".format(INP_DATE))

        print("-" * 50)

    if none_found == 1:
        print("\t-\tNONE.")


def createdistrictdictionary(state_id):
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_id))
    json_data = json.loads(response.text)
    dct = {}
    for i in json_data["districts"]:
        dct.update({i["district_id"]: i["district_name"]})
    return dct


# Execute
if method == 1:
    checkdistrict(district_code)

if method == 0:
    dct = createdistrictdictionary(state_code)
    for i in dct.keys():
        print("\n", i, dct[i], end="")
        checkdistrict(i)

print("\nSEARCH COMPLETE.")
sleep(10000)

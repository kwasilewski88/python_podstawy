import json
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    for dane in data["imdata"]:
        for key, values in dane.items():
            for key_, values_ in values.items():

                for key__, values__ in values_.items():
                    if key__ == "dn":
                        dn = values__
                    if key__ == "speed":
                        speed = values__
                    if key__ == "descr":
                        descr = values__
                    if key__ == "mtu":
                            mtu = values__

                print(dn, speed, descr, mtu)

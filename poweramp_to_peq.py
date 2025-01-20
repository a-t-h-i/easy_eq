import json, os

def convert_to_peq(settings):
    filename = f"""converted_files/{settings["name"].replace(" ", "_")}.txt"""
    preamp = settings["preamp"]
    bands = settings["bands"]
    filters = []
    freqs = []
    band_types = { 0: "LPQ", 1: "HPQ", 2: "BP", 3: "PK", 4: "LS", 5: "HS"}
    output = f"Preamp: {preamp}"

    for band in bands:
        freqs.append(band["frequency"])
        filters.append({"freq": band["frequency"], 
                        "q_factor": round(float(band["q"]),2), 
                        "gain": round(float(band["gain"]),2), 
                        "type": band_types[band["type"]]})

    freqs.sort()

    for i in range(len(freqs)):
        output += f"""\nFilter {i+1}: ON {filters[i]["type"]} Fc {filters[i]["freq"]}Hz Gain {filters[i]["gain"]} Q {filters[i]["q_factor"]}"""
    
    #Save to txt
    with open(filename, 'w') as file:
        file.write(output)

def poweramp_to_peq(file_path):

    files = os.listdir(file_path)

    for eq_file in files:
        with open(f"{file_path}/{eq_file}", 'r') as eq_profile:
            data = json.load(eq_profile)
            convert_to_peq(data)
    

poweramp_to_peq('poweramp_files')



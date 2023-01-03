import json

f = open("database/metadata_final.json",)

data = json.load(f)

f.close()



for i in range (5000):
    with open(f"database/NFT metadata/{i}", "w") as file:
        metadata = json.dumps(data[i], indent=4)
        file.write(metadata)
        file.close()

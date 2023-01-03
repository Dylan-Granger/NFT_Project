import json
import random
from create_image import *




backgrounds = ["Blue Swirl", "Blue", "Green", "Light Pink", "Peach", "Purple Swirl", "Purple", "Red", "Turqouise", "Yellow"] #10
background_weights = [2, 15, 16, 7, 5, 1.5, 14.5, 12, 13, 14]

fur_colour = ["Baby Blue", "Black", "Blue Camo", "Brown", "Gold", "Green", "Orange", "Purple", "Red Camo", "Red", "Silver"] #11
fur_colour_weights = [8, 20, 4.5, 17, 0.75, 12.25, 10, 9.5, 3.5, 13, 1.5]

earrings = ["Diamond Studs", "Double Gold Stud", "Gold Cross", "Gold Double Mini Hoops (Helix)", "Gold Double Mini Hoops", "Gold Mini Hoops", "Industrial", "Pearl Studs", "Ruby Studs", "Silver Mini Hoops", "Single Gold Stud"] #11
earring_weights = [1, 8, 4, 9, 9.5, 10, 7, 20, 1.5, 18, 12]

outfits = ["Bellhop Uniform", "Dress Shirt", "ETH Chain", "Greek Robe", "Hoodie", "Kobe Jersey", "Kung Fu Robe", "Maid Suit", "Panda Tag Chain", "Police Uniform", "Suit", "Tied Sweater", "Turtleneck with Pearls", "Varsity Jacket", "Vest With Dress Shirt"] #15
outfit_weights = [6, 8.5, 4, 5, 14, 0.75, 1.25, 9, 10, 10.5, 6.5, 11, 3, 3.5, 7]

eyes = ["3D Glasses", "Aviators", "Black Eye", "ETH", "Hearts", "Kaws", "Laser Eyes", "Marijuana Eyes", "Murakami", "Sharingan", "Standard", "Stoned", "Tinted Glasses", "Yin Yang"] #14
eye_weights = [5, 8, 5.5, 7, 9, 9.5, 1, 6.5, 1.5, 2.5, 19, 12, 10, 3.5]

hats = ["Banana Peel", "Beanie", "Bellhop Hat", "Bucket Hat", "Devil Horns", "Dropped Ice Cream Cone", "Greek Crown", "Halo", "Maid Hairband", "Ninja Headband", "Police Hat", "Sailor Hat", "Sushi", "Unicorn", "Wizard Hat"] #15
hat_weights = [5.5, 8.5, 6, 9.5, 4, 3.5, 5, 1.5, 7, 4.5, 10, 12, 14, 6.5, 2.5]

mouth = ["Blunt", "Diamond Grillz", "Eating Bamboo 2", "Eating Bamboo", "Gold Grillz", "Jaw Dropped", "Party Popper", "Scared", "Smile", "Smirk", "Tongue Out", "Eating Noodles", "Yuck", "Zipper"] #14
mouth_weights = [4, 0.75, 8, 6, 1.25, 11.5, 5, 7, 11, 14, 12, 8, 6.5, 5]


Total_NFTs = 5000
NFTs_created = []

traits = [["Background", backgrounds, background_weights], ["Fur Colour", fur_colour, fur_colour_weights], ["Earrings", earrings, earring_weights], ["Outfit", outfits, outfit_weights],
["Eyes", eyes, eye_weights], ["Hats", hats, hat_weights], ["Mouth", mouth, mouth_weights]]

def create_trait_metadata():
    base_metadata = {
        'attributes': []
    }
    for i in range (len(traits)):
        trait = {
            'trait-type': traits[i][0],
            'value': random.choices(traits[i][1], traits[i][2])[0]
        }
        base_metadata['attributes'].append(trait)

    if base_metadata in NFTs_created:
        return create_trait_metadata()
    else:
        NFTs_created.append(base_metadata)

def create_signature(sig_num):
    values = ['Astronaut Panda', 'Cowboy Panda', 'Ninja Panda', 'Scuba Panda', 'Zombie Panda']
    base_metadata = {
        'attributes': []
    }
    attributes = {
        "trait-type": "Trademark Series",
        "value": values[sig_num]
    }
    base_metadata['attributes'].append(attributes)
    
    NFTs_created.append(base_metadata)

signatures = [372, 1185, 2314, 3936, 4882]

# the real deal 


if __name__ == "__main__":
    counter = 0
    counter2 = 1
    for i in range (Total_NFTs):
        if i in signatures:
            create_signature(counter)
            counter += 1
        else:
            create_trait_metadata()
    for i in range (len(NFTs_created)):
        if i in signatures:
            image = get_signature_image(counter2)
            counter2 += 1
        else:
            image = create_NFT_image(NFTs_created[i])
        image_bytes = image_to_byte_array(image)
        response = upload_to_IPFS(image_bytes)
        NFTs_created[i]['name'] = f'Posh Pandas #{i}'
        NFTs_created[i]['image'] = f'ipfs://{response}'
        NFTs_created[i]['description'] = "Posh Pandas is a project built on the Ethereum Blockchain containing a collection of 5000 uniquely generated Pandas. Holding a Panda isn't just for the great artwork but it brings you into a community filled with positivity and passion. Everyone wants to be posh, so start your journey with the experienced Posh Pandas! poshpandas.ca"
        NFTs_created[i]['external_url'] = "https://www.poshpandas.ca/"
    traits_final = json.dumps(NFTs_created, indent=4)
    with open('database/metadata_final.json', 'w') as file:
        file.write(traits_final)
        file.close





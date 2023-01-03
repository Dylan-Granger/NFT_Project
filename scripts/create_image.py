from PIL import Image
import requests
import io
from dotenv import load_dotenv
import os


# Gets API keys from .env file

load_dotenv()
Pinata_api_key = os.getenv("PINATA_PUB")
Pinata_secret_key = os.getenv("PINATA_PRIV")

header = {'pinata_api_key': Pinata_api_key, 'pinata_secret_api_key': Pinata_secret_key, 'acceptedFiles': ".json"}

Backgrounds_files = {
    "Blue Swirl": 'b1', 
    "Blue": 'b2',
    "Green": 'b3',
    "Light Pink": 'b4',
    "Peach": 'b5',
    "Purple Swirl": 'b6',
    "Purple": 'b7',
    "Red": "b8",
    "Turqouise": "b9",
    "Yellow": "b10"
}

furfiles = {
    "Baby Blue": "fur1",
    "Black": "fur2",
    "Blue Camo": "fur3",
    "Brown": "fur4",
    "Gold": "fur5",
    "Green": "fur6",
    "Orange": "fur7",
    "Purple": "fur8",
    "Red Camo": "fur9",
    "Red": "fur10",
    "Silver": "fur11"
}

eyefiles = {
    "3D Glasses": "eye1",
     "Aviators": "eye2",
     "Black Eye": "eye3",
     "ETH": "eye4",
     "Hearts": "eye5",
     "Kaws": "eye6",
     "Laser Eyes": "eye7",
     "Marijuana Eyes": "eye8",
     "Murakami": "eye9",
     "Sharingan": "eye10",
     "Standard": "eye11",
     "Stoned": "eye12",
     "Tinted Glasses": "eye13",
     "Yin Yang": "eye14"
}

outfitfiles = {
    "Bellhop Uniform": "out1",
    "Dress Shirt": "out2",
    "ETH Chain": "out3",
    "Greek Robe": "out4",
    "Hoodie": "out5",
    "Kobe Jersey": "out6",
    "Kung Fu Robe": "out7",
    "Maid Suit": "out8",
    "Panda Tag Chain": "out9",
    "Police Uniform": "out10",
    "Suit": "out11",
    "Tied Sweater": "out12",
    "Turtleneck with Pearls": "out13",
    "Varsity Jacket": "out14",
    "Vest With Dress Shirt": "out15"
}

hatfiles = {
    "Banana Peel": "hat1",
    "Beanie": "hat2",
    "Bellhop Hat": "hat3",
    "Bucket Hat": "hat4",
    "Devil Horns": "hat5",
    "Dropped Ice Cream Cone": "hat6",
    "Greek Crown": "hat7",
    "Halo": "hat8",
    "Maid Hairband": "hat9",
    "Ninja Headband": "hat10",
    "Police Hat": "hat11",
    "Sailor Hat": "hat12",
    "Sushi": "hat13",
    "Unicorn": "hat14",
    "Wizard Hat": "hat15"
}

mouthfiles = {
    "Blunt": "mou1",
    "Diamond Grillz": "mou2",
    "Eating Bamboo 2": "mou3",
    "Eating Bamboo": "mou4",
    "Gold Grillz": "mou5",
    "Jaw Dropped": "mou6",
    "Party Popper": "mou7",
    "Scared": "mou8",
    "Smile": "mou9",
    "Smirk": "mou10",
    "Tongue Out": "mou11",
    "Eating Noodles": "mou12",
    "Yuck": "mou13",
    "Zipper": "mou14" 
}

earringfiles = {
    "Diamond Studs": "ear1",
    "Double Gold Stud": "ear2",
    "Gold Cross": "ear3",
    "Gold Double Mini Hoops (Helix)": "ear4",
    "Gold Double Mini Hoops": "ear5",
    "Gold Mini Hoops": "ear6",
    "Industrial": "ear7",
    "Pearl Studs": "ear8",
    "Ruby Studs": "ear9",
    "Silver Mini Hoops": "ear10",
    "Single Gold Stud": "ear11"
}

def get_signature_image(signature_number):
    im1 = Image.open(f"NFT_traits/Final1to1/{signature_number}.png").convert("RGBA")
    im1.thumbnail((500, 500))

    return im1

def create_NFT_image(traits):
    '''
    create_NFT_image(Dict) => PIL.Image
    Creates the NFT's image based on the 7 traits it is passed
    '''

    #Opens all base images in the NFT being made

    im1 = Image.open(f"NFT_traits/Background/{Backgrounds_files[traits['attributes'][0]['value']]}.png").convert('RGBA')
    im2 = Image.open(f"NFT_traits/Fur/{furfiles[traits['attributes'][1]['value']]}.png").convert('RGBA')
    im3 = Image.open(f"NFT_traits/Earrings/{earringfiles[traits['attributes'][2]['value']]}.png").convert('RGBA')
    im4 = Image.open(f"NFT_traits/Outfit/{outfitfiles[traits['attributes'][3]['value']]}.png").convert('RGBA')
    im5 = Image.open(f"NFT_traits/Eyes/{eyefiles[traits['attributes'][4]['value']]}.png").convert('RGBA')
    im6 = Image.open(f"NFT_traits/Hat/{hatfiles[traits['attributes'][5]['value']]}.png").convert('RGBA')
    im7 = Image.open(f"NFT_traits/Mouth/{mouthfiles[traits['attributes'][6]['value']]}.png").convert('RGBA')

    #Combines all images to create final NFT image

    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)

    com6.thumbnail((500, 500))

    return com6

def image_to_byte_array(image:Image):
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format='png')
  imgByteArr = imgByteArr.getvalue()
  
  return imgByteArr

def upload_to_IPFS(file):
    files = {
        'file': file
    }
    response = requests.post('https://api.pinata.cloud/pinning/pinFileToIPFS', headers=header, files=files)
    if response.status_code == 200:
        return response.json()['IpfsHash']
    else:
        return f'ERROR: {response.text}'

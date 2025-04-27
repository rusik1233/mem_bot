import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"


def random_meme():
    meme_jpg = ['images/meme1.jpg','images/meme2.jpeg','images/meme3.jpeg','images/meme4.jpeg']
    return random.choice(meme_jpg)
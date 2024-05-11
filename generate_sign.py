import random
from ecpy.curves import WeierstrassCurve, Point


order = 21888242871839275222246405745257275088548364400416034343698204186575808495617

curve = {
        'name':      "bn254",
        'type':      "weierstrass",
        'size':      254,
        'field':     21888242871839275222246405745257275088696311157297823662689037894645226208583,
        'generator': (1, 2),
        'order':     order,
        'cofactor':  1,
        'a':         0,
        'b':         3,

    }


cv = WeierstrassCurve(curve)
G_1 = Point(1,2, cv)
G_2 = Point(11289777278598793225085907404653984148857981139181946850122111571098664312074, 4216647052951083135303109263368671021502984236462818053005360266128784521345, cv)

# Ring setup
ring_len = 8
members = [random.randint(1, order - 1)*G_1 for _ in range(ring_len - 1)]
my_secret = random.randint(1, order - 1)
my_public = my_secret*G_1

def generate():
    
    # Inserting myself into ring
    my_pos = random.randint(0, ring_len - 1)
    members.insert(my_pos, my_public)
    image = my_secret*(-G_1 +G_2)
    
    # Generating random pre-ring
    sign_members = [random.randint(1, order - 1) for _ in range(ring_len)]
    
    ring_1 = 0*G_1
    for i in range(ring_len):
        ring_1 += sign_members[i] * members[i]
        
    ring_2 = 0*G_1
    for i in range(ring_len):
        ring_2 += sign_members[i] * (members[i] + image)
    
    
    image_sign = random.randint(0, order - 1)
    image_sign_x = (image_sign*(-G_1 + G_2)).x

    # Cancualting final ring random value
    # Can be used any random function
    ring_x = (ring_1.x + ring_2.x + image_sign_x) % order
    
    # Generating signatures
    prev_x = sign_members[my_pos]
    sign_members[my_pos] += ring_x - sum(sign_members)
    sign_members[my_pos] %= order
    
    
    sign_1 = my_secret*(prev_x - sign_members[my_pos]) % order
    sign_2 = (image_sign - my_secret*sign_1) % order
    
    # sum(sign_members) % order == ring_x
    # image = -x*G_1 + x*G_2
    
    
    return {
        "members": members,
        "sign_members": sign_members,
        "image": image,
        "sign_1": sign_1,
        "sign_2": sign_2
    }

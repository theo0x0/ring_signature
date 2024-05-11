from generate_sign import G_1, G_2, order, generate, ring_len


ring_signature = generate()
sign_members = ring_signature['sign_members']
members = ring_signature['members']
image = ring_signature['image']
sign_1 = ring_signature['sign_1']
sign_2 = ring_signature['sign_2']

def verify_sign():
    

    ring_1 = sign_1*G_1
    for i in range(ring_len):
        ring_1 += sign_members[i] * members[i]
        
    ring_2 = sign_1*G_2
    for i in range(ring_len):
        ring_2 += sign_members[i] * (members[i] + image)
    
    image_sign = sign_1*image + sign_2*(-G_1 + G_2)
    
    ring_x = (ring_1.x + ring_2.x + image_sign.x) % order
    print(sum(sign_members) % order == ring_x)
    
verify_sign()

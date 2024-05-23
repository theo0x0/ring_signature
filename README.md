

# Ring signature

Used libraries: [EcPy](https://pypi.org/project/ECPy/)

Curve: bn254, base points: (1, 2) and [G_2](https://github.com/theo0x0/bn_254_gen)


## Usage 
Run `python3 verify_sign.py`

Random generated ring members and user key.

generate_sign.py generates a dict to verify

verify_sign.py verifies a dict, generated by generate()

## Specs
Size: n + 2 scalars, 1 EC point (user's key image), members' keys

Verify operations: 2*n + 4 ec_mul, 3*n + 3 ec_add


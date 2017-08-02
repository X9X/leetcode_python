d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(d)

def test(**args):
    for k in args:
        print args[k]

test(**d)

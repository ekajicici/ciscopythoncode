# dictionary
# KEYS : VALUE
veritas_uni ={
    "name": "veritas uni abuja",
    "date": 2002,
    "faculties": ["NAS", "SOC SCI", "HLT SCI", "LAW"],
    "studnet": 10000,
    "dept": {
        "NAS": ["CIT", "CHE", "MCB"],
        "SOC SCI": ["POL SCI", "ECO", "PEA & COM"],
    },
    1: "OUR WINNING SIDE"
}
print(veritas_uni)

# accessing a lsit
z = veritas_uni["faculties"]
print(z)
for i in veritas_uni["faculties"]:
    print(i)
if i == "NAS":
     print("this is my faculty")
else:
    print("this is not my faculty")
    print(i)

# getting keys.keys()
x = veritas_uni.keys()
print(x)
# dict value
z = veritas_uni.values()
print(z)
# mutability
veritas_uni["name"] = "VERITAS UNIVERSITY BWARI ABUJA".lower()
veritas_uni.update({"date": 2008})
print(veritas_uni)
veritas_uni["faculties"][0] = "natural and applied science"
print(veritas_uni.items())

# removing item
#veritas_uni.pop("")

# looping
for x in veritas_uni:
    print("the keys :", x)

# using keys to get values
print("these are value")
for j in veritas_uni:
    print(veritas_uni[j])
for z in veritas_uni.values():
    print(z)
#for y, p in veritas_uni.item():
# print(y, ":", p)

# copying a dict
nig_uni = veritas_uni.copy()
print(nig_uni)

# populating a dictionary
csc105 = {}
for l in range(6):
    x_keys = input("enter the keys")
    y_val = input("enter the value")
    csc105.update({
        x_keys: y_val
    })
for m, k in csc105.items():
    print(m, k)
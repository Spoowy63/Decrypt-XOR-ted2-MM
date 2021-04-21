import re

# Change those two to your own numbers, make sure they are different from each other!
# Make sure you puth for both a 19 numbers long number, else it will fuck up.
# If you change these, also open Utils.h & change them there too with the same values you have here.
cryptBaseOne = 1959173450275472825
cryptBaseTwo = 8264919756289164628

def decrypt_offset(offset):
    return str(hex(((int(hex(int(offset)), 16) ^ cryptBaseTwo) - cryptBaseOne)))

# Translation of this pattern:
# Encrypted offset contain numbers --> [0-9]
# Only want encrypted offsets and not some random one digit number --> {6,30}
# Must end with: ',' or '}' or ')' --> [,})]
    # Last encrypted offset in switch will end with '}'
    # multiple encrypted offsets in array is ','
    # getRealOffset ends with ')'
pattern = re.compile(r'([0-9]{6,30})[,})]')

def find_encrypted_offsets_in_file():
    with open("Tweak.xm", "rt") as file:
        data = file.read()
        matches = pattern.finditer(data)
        hasPrintedCredits = False

        for match in matches:
            # Just cause it's cool to print things :kappa:
            if not hasPrintedCredits:
                print("="*43)
                print("OFFSET ENCRYPTION TOOL MADE BY JOEYJURJENS")
                print("OFFSET DECRYPTION TOOL MADE BY Spoowy63")
                print("="*43)
                hasPrintedCredits = True

            offsetString = match.group(1)
            print("Offset found: %s " % offsetString)
            print("Decrypting offset now...")           
            data = data.replace(offsetString, decrypt_offset(offsetString))
            print("New Offset: %s" % decrypt_offset(offsetString))

        # Write the new data to the file.
        write_new_data_to_file(data)            


def write_new_data_to_file(data):
    with open("Tweak.xm", "wt") as file:
        file.write(data)
        file.close()

# Find the offsets in tweak.xm
find_encrypted_offsets_in_file()

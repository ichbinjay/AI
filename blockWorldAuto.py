blocks = ("a", "b", "c", "d", "e")
rules = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}
# it means that before key occurs, all the values in the list must occur

def is_valid(sequence, arg_block):
    # check if the rules for the block are satisfied
    sequence.append(arg_block)
    for item in rules[arg_block]:
        if item not in sequence:
            sequence.pop()
            return False
        if sequence.index(item) > sequence.index(arg_block):
            sequence.pop()
            return False
    return True

def main():
    sequences = genrate_sequences()
    for sequence in sequences:
        print("\n",sequence)
        choice = sequence[0]
        del sequence[0]
        if choice in blocks:
            if is_valid(sequence, choice):
                print("Sequence after adding {} is {}".format(choice, sequence))
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")
        choice = sequence[1]
    print("The blocks in order are:")
    print(sequence)


main()

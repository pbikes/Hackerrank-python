def mutate_string(string, position, character):
    return string[:position] + "k" + string[position + 1:]


print(mutate_string("abracadabra", 5, "k"))

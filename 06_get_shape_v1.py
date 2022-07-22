'''
component 6 v1 - setting up string check function
'''


def string_check(choice, options):
    for var_list in options:

        # if the snack is in one of the lists, return the full response
        if choice in var_list:

            # get full name of snack and put it
            # in title case it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# Main routine


# Valid answers for yes and no
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# ask user if they are ready to pick a shape
check_shape = "invalid choice"
while check_shape == "invalid choice":
    want_shape = input("Ready to pick a shape?").lower()
    check_shape = string_check(want_shape, yes_no)
    if want_shape not in "yes_no":
        print("Please enter yes or no.")
    elif want_shape == "no" or want_shape == "n":
        break


print(check_shape)

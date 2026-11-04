import validation as v

def input_positive_integer(input_msg):
    while True:
        try:
            num = int(input(input_msg).strip())
            if v.is_positive_integer_number(num):
                return num
            print("Please enter only a positive integer number!") 
        except ValueError:
            print("Please enter only a number!")


def input_not_negative_integer(input_msg):
    while True:
        try:
            num = int(input(input_msg).strip())
            if v.is_not_negative_integer_number(num):
                return num
            print("Please enter only a not negative integer number!") 
        except ValueError:
            print("Please enter only a number!")


def input_not_empty_string(input_msg):
    while True:
        str = input(input_msg).strip()
        if v.is_non_empty_string(str):
            return str
        print("Please enter only a not-empty stirng!") 

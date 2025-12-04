import math

def is_valid_1(s: str) -> bool:
    
    if len(s) % 2 > 0:
        return True

    mid = 0 + len(s) // 2

    left_half, right_half = s[:mid], s[mid:]

    return left_half != right_half
    

def format_input(input: str) -> list[str]:
    input_arr = input.split(",")
    input_arr = [
        pair.split("-") for pair in input_arr
    ]
    final_input = []
    for one, two in input_arr:
        for i in range(int(one),int(two)+1):
            final_input.append(str(i))

    return final_input


def part_1(input: str) -> int:
    res = 0

    input_arr = format_input(input)
    #print(input_arr)
    
    for num in input_arr:
        if not is_valid_1(num):
            #print("invalid num: ", num)
            res += int(num)

    return res

def part_2(input: str) -> int:
    res = 0

    input_arr = format_input(input)
    #print(input_arr)
    
    for num in input_arr:
        if not is_valid_2(num):
            #print("invalid num: ", num)
            res += int(num)

    return res

# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
def is_valid_2(s: str) -> bool:
    len_s = len(s)

    # get a changing slice size, that is at max the size of half the array
    for block_size in range(1,math.ceil((len(s)+1)/2)):
        if len_s % block_size > 0:
            continue

        # Set the value all blocks must equal to be invalid
        must_be = s[0:block_size]
        l,r = block_size, block_size*2
        while r <= len_s:

            # if non-equal block found, must be valid, so break and continue
            # with a larger block size
            if s[l:r] != must_be:
                break

            l, r = r, r+block_size

        # TIL while else can be used and is called
        # only if the inner while loop finishes
        else:
            return False

    return True

def day_2():
    input = "4487-9581,755745207-755766099,954895848-955063124,4358832-4497315,15-47,1-12,9198808-9258771,657981-762275,6256098346-6256303872,142-282,13092529-13179528,96201296-96341879,19767340-19916378,2809036-2830862,335850-499986,172437-315144,764434-793133,910543-1082670,2142179-2279203,6649545-6713098,6464587849-6464677024,858399-904491,1328-4021,72798-159206,89777719-90005812,91891792-91938279,314-963,48-130,527903-594370,24240-60212"
    #input="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    #print(part_1(input))
    print(part_2(input))
    #print(is_valid_2("824824824"))
    

    #print(is_valid_1("true"))

if __name__ == "__main__":
    day_2()

def main():
    """Main function"""
    print(sum_1_to_n(100))

def sum_1_to_n(n):
    """Sum from 1 to the given n"""
    sum = 0
    i = 0
    while (i <= n):
        sum += i
        i += 1
        return sum

main()

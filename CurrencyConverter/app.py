def main():
    print("This program converts US dollars to Turkish Liras")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    turkish_lira = convert_to_tl(dollars)
    print("That is", turkish_lira, " turkish liras.")

convert_to_tl = lambda dollars: dollars * 26.98

main()
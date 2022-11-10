class Main:
    def main(self):
        num_of_squares = int(input("Enter the number of magic squares to find: "))

        amount_found = 0
        sum_so_far = 0
        last_added_digit = 0
        total_nums_added = 0

        n = 0
        while amount_found != num_of_squares:
            n += 1

            square_of_n = n**2
            while sum_so_far < square_of_n:
                last_added_digit += 1
                total_nums_added += 1
                sum_so_far += last_added_digit

            if sum_so_far == square_of_n:
                amount_found += 1
                print(f"#{amount_found} {square_of_n} (1 to {total_nums_added})")


from time import perf_counter

start = perf_counter()
Main().main()
end = perf_counter()

print(f"Program finished executing in {end - start} seconds.")

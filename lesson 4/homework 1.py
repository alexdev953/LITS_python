n = int(input('Enter number: '))
if n <= 1000:
    print(f"oct{'bin':>15}{'hex':>15}{'dec':>15}")
    print(f"{n:o}{n:>15b}{n:>15x}{n:>15}")
else:
    print('Enter number less than 1000!')
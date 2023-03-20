"""
function calculate_bonu(sale):
    if sale >= 1000:
        bonu = sale * BONU_RATE_HIGHT
    else:
        bonu = sale * BONU_RATE_LOW
    return bonu

get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""

BONU_RATE_LOW = 0.1
BONU_RATE_HIGHT = 0.15


def calculate_bonu(sale):
    if sale >= 1000:
        bonu = sale * BONU_RATE_HIGHT
    else:
        bonu = sale * BONU_RATE_LOW

    return bonu


def test():
    bonu = calculate_bonu(500)
    print(bonu)

    bonu = calculate_bonu(2000)
    print(bonu)

    bonu = calculate_bonu(1000)
    print(bonu)


def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonu = calculate_bonu(sales)
        print(f"Bonu: {bonu}")
        sales = float(input("Enter sales: $"))


test()
main()

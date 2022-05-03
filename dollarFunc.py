
def dollar(x):
    return "$ {:,.2f}" .format(float(x))

def main():
    saleAmount = 11375
    taxAmount = 1215.784
    amount = '235844.1952'
    print(dollar(saleAmount), dollar(taxAmount), dollar(amount))

if __name__ == "__main__":
    main()

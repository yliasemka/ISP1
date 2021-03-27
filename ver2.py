import logging

logging.basicConfig(level=logging.INFO)


def eratosphene(number):
    array = [True] * number
    array[0] = array[1] = False
    for k in range(2, number):
        if array[k]:
            for m in range(2 * k, number, k):
                array[m] = False
    for k in range(number):
        if array[k]:
            logging.info(f"{k}" + "-" + "s")
        else:
            logging.info(f"{k}" + "-" + "c")
    return


def main():
    while True:
        try:
            number = int(input("input your  number: "))
            break
        except ValueError:
            logging.info("Invalid type! Please try again")
    eratosphene(number)
    return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Oops,bay:")

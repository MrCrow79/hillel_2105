from utils.logger_utils import logger


def fibonaci(num):
    """
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
    10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229
    :return:
    """
    logger.info(f'Call fibonachi with {num}')

    if num in (1, 2):
        logger.info(f'Execution fibonachi with {num}, return 1')
        return 1

    first = fibonaci(num - 1)
    second = fibonaci(num - 2)
    result = first + second
    logger.info(f'Execution fibonachi with {num}, return {result}')
    return result


print(fibonaci(10))
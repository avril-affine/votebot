from selenium import webdriver
import sys
import time
import random
import math


def vote():
    driver = webdriver.Chrome("./chromedriver")

    url = ("http://www.surveygizmo.com/s3/2485907/"
           "Readers-Choice-Best-Indie-Video-of-2015")
    driver.get(url)
    random_sleep(4, 6)

    query = ("document.querySelectorAll("
             "'div.sg-question-options label')[6].click();")
    driver.execute_script(query)
    random_sleep(2, 4)

    submit = ("document.querySelector("
              "'input[name=sGizmoSubmitButton]').click();")
    driver.execute_script(submit)
    random_sleep(2, 4)

    driver.delete_all_cookies()
    driver.quit()


def random_sleep(a, b):
    t = random.uniform(a, b)
    time.sleep(t)


def print_status(n):
    mod = int(math.log(n, 10))
    if n % (10 ** mod) == 0:
        print '%d votes submitted' % n


def main():
    if len(sys.argv) == 1:
        n = 1
    elif len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print 'Error: Invalid number of arguments'
        return

    for i in xrange(n):
        vote()
        print_status(i + 1)
        random_sleep(10, 20)


if __name__ == '__main__':
    main()

from celery import Celery
from time import sleep

app = Celery('get-started', brocker='amqp://', backend='rpc://')


@app.task
def add(x, y):
    sleep(5)
    return x + y


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
    return results


@app.task
def gen_prime_2(x):
    prime_numbers = []
    for i in range(2, x+1):
        for prime_number in prime_numbers:
            if i % prime_number == 0:
                break
        else:
            prime_numbers.append(i)

    return prime_numbers


@app.task
def is_prime(x):
    for i in range(2,x):
        if (x % i) == 0:
            return False
    return True
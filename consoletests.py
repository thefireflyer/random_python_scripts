#print("hello", end="")
#print("\b\b\b\b\b\btest")
import time
sleep_time = 0.05
print("loading...   ", end="")

def print_processing_indicator(num):
    for i in range(num):
        print("\b\\", end="")
        #time.sleep(sleep_time)
        print("\b|", end="")
        #time.sleep(sleep_time)
        print("\b/", end="")
        #time.sleep(sleep_time)
        print("\b-", end="")
        #time.sleep(sleep_time)
        print("\b\\", end="")
        #time.sleep(sleep_time)
        print("\b|", end="")
        #time.sleep(sleep_time)
        #print("\b ᓚᘏᗢ", end="\b\b\b")
        #time.sleep(sleep_time)

def reset_line(num):
    for i in range(num):
        print("\b", end="")


print_processing_indicator(20000)
reset_line(13)
print("loading complete ✔")


print("starting server...   ", end="")
print_processing_indicator(20000)
reset_line(21)
print("server up and running ✔")


print("generating data:   ", end="")
for i in range(100):
    print(".", end="")
    time.sleep(0.1)

reset_line(120)
print("data generation complete ✔                                                                                                                            \n")


input("")
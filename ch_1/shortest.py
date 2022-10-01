# This program calls shortest again and again and again and forver.
# So this would crash.
# This case is called stackoverflow.

def shortest():
    shortest()


shortest()

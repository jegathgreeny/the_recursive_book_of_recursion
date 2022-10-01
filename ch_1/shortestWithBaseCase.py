def ShortestWithBaseCase(makeRecusiveCall):
    print(f'ShortestWithBaseCase({makeRecusiveCall})')
    if not makeRecusiveCall:
        # BASE CASE
        print("Returning from base case")
        return
    else:
        # RECURSIVE CASE
        ShortestWithBaseCase(False)
        print("Returning from recursive case")
        return

print('Calling with False')
ShortestWithBaseCase(False)
print()
print('Calling with True')
ShortestWithBaseCase(True)

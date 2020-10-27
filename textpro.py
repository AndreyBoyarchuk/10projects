

results = []
while True:
    user_input = input("Say something: ").strip()
    if user_input =="\end":
        break
    else:
        results.append( user_input )
        print(user_input)
    print('check point')
print(results)

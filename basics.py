import datetime
print(datetime.datetime.today())
mynow=datetime.datetime.now()
first_list=[89.89, 489,89]
print(first_list)
print(list(range(1,10)))
print(list(range(1,10,2)))

typicalList=["can_be_string", "can be integer", 2,"or float", 5.5]
complexList=["can_be_string", "can be integer", [4, 5, 6], 2,"or float", 5.5]
basic_sample= [2,2,7,9,45,45,78,69,78,68]
mysum = sum(basic_sample)

length= len(basic_sample)
mean=mysum/length
print("This is mean:",mean)
print(max(basic_sample))
second_sample = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
count_10 =second_sample.count(10)

print(count_10,count_10)
userName="LoserName"
print(userName.lower())

dictionary_example = {"Mary": 6.10, "Anya": 7}
print(dictionary_example.values())

#tuples

tuple_sample = (9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9)

basic_sample.remove(2)
print(basic_sample)

#Meesing with list

monday_temperatures=[91,8.8,7.56,55]
monday_temperatures.append(8.1)
print(monday_temperatures)
var1=monday_temperatures.index(91)
print(var1)
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)
len(monday_temperatures)
print(len(monday_temperatures))
print(monday_temperatures[1:3])
print(monday_temperatures[1:]) # to the last item
print(monday_temperatures[-1])
print(monday_temperatures[-2:])
vara=['hello',1,2,3]
vara2=vara[0][2]
print(vara2,"Prints second letter of first Item")
print(vara[0][-1],"prints last letter")
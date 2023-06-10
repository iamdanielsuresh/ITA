import re
log = "July 31 07:52:58 computer bad_process[12345]: ERROR"
#i need to get the id

regex = r"\[(\d+)\]"
result= re.search(regex, log)
print(result[1])
result1 = re.search(regex, "A completely diffrent string that also has numbers [3242]")
print(result1[1])
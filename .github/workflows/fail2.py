import re


text_file = open("abc1.txt", "r")
str = text_file.read()

str1 = "has exceeded threshold limit for messages. Please take action!"
str2 = "There might be problem with WAS servers"
str3 = "Issue Has Occurred for Allowed Retrial Times"
str4 = "Following Queues are not reducing"
str5 = "Following Buses might be down"


if re.search(str1,str):
             print(str1)
elif re.search(str2,str):
               print(str2)
elif re.search(str3,str):
               print(str3)
elif re.search(str4,str):
               print(str4)
elif re.search(str5,str):
               print(str5)
else:
               print('No Match')
          
text_file.close()

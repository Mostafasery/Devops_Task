with open("users.txt") as f:
    content_list = f.readlines()




content_list[1]

list_length = len(content_list)
lines=[]
for i in range(list_length):
    splitt=content_list[i].split(" ")
    lines.append(splitt)




for i in range(len(lines)):
    if "@" in (lines[i][-2]):
        mail_domain=lines[i][-2].split("@")
        if ".com" in (mail_domain[1]) :
            try:
                if (int(lines[i][-1]) %2) ==0:
                    print("The ID" + " "+lines[i][-1]+ " of email"+" " + lines[i][-2]+ " is even number")
                if (int(lines[i][-1]) %2) !=0:
                    print("The ID" + " "+lines[i][-1]+ " of email"+" " + lines[i][-2]+ " is odd number")
            except:
                continue
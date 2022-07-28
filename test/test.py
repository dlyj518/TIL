participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

kkdk = []
for i in participants:
    if i in kkdk: kkdk.remove(i)
    else: kkdk.append(i)
print(kkdk[0])
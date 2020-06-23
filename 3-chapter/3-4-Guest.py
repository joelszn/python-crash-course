guestlist = ['drake','the rock','grandpa']
for i in guestlist:
    print(f"{i} you're invited to my dinner.")

guestlist[1] = 'mom'
for i in guestlist:
    print(f"\n{i} you're invited to my dinner.")

# 3-6 More guest
guestlist.insert(0, 'ray')
guestlist.insert(2, 'roman')
guestlist.append('will')
for i in guestlist:
    print(f"\n{i} you're invited to my dinner.")

# 3-7 shrinking guest list
for i in range(4):
    print(len(guestlist))


    removed_name  = guestlist.pop()

    print(f"apologies you can't go anymore, {removed_name}")
print(guestlist)

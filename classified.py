# Program deletes after being run

from os import remove
from time import sleep


sleep(0.5)
print("What you are about to read is highly classified...")
sleep(1.5)

print("and I'm going to pause for a moment to let it sink in...")
sleep(5.5)

sentence = ("Sorry, my bad. ", "You're not Tom Cruise. ")
for i in sentence:
	print(i, end="")
	sleep(2)

print("So therefore...")
sleep(2)

print("This message will delete in:")

for second in range(5, 0, -1):
    print(second)
    sleep(1)
remove(__file__)

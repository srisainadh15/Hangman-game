import random
s = "There once was a boy who grew bored while watching over the village sheep. He wanted to make things more exciting. So, he yelled out that he saw a wolf chasing the sheep. All the villagers came running to drive the wolf away. However, they saw no wolf. The boy was amused, but the villagers were not. They told him not to do it again. Shortly after, he repeated this antic. The villagers came running again, only to find that he was lying. Later that day, the boy really sees a wolf sneaking amongst the flock. He jumped up and called out for help. But no one came this time because they thought he was still joking around. At sunset, the villagers looked for the boy. He had not returned with their sheep. They found him crying. He told them that there really was a wolf, and the entire flock was gone. An old man came to comfort him and told him that nobody would believe a liar even when they are being honest"
l = s.split()
choice_list = random.choice(l)
n = len(choice_list)
dp = ['_']*len(choice_list)
print(dp)
lives = 6
completed_alphabet = []
k = 0
s = list(set(choice_list))
while dp.count('_') != 0:
    x = input('guess alphabet  ;')
    if x not in completed_alphabet:
        completed_alphabet.append(x)
    else:
        print("already checked \n")
        print(completed_alphabet)
        continue
    if x not in s:
        k = k+1
    if k == 6:
        break
    for i in range(len(choice_list)):
        if choice_list[i] == x:
            dp[i] = x
    print(dp)
if dp.count('_') == 0:
    print(dp)
else:
    print('out of lives')
    print('The word is   :',choice_list)
print("hangman is      \n")
if k == 6:
    print('    0   ')
    print(R"   /|\ ")
    print(R"   / \  ")
elif k == 5 :
    print('   0   ')
    print(R" /|\  ")
    print("  /   ")
elif k == 4 :
    print('   0   ')
    print(R" /|\  ")
elif k==3 :
    print('   0   ')
    print(R" /|   ")
elif k==2 :
    print('   0   ')
    print('   |   ')
elif k==1 :
    print('  0  ')
else:
    print('   ')
















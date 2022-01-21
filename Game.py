import random

def main():
    rps = input ('Choose beteweewn rock (1), paper (2)  or scissors (3)\n')


    if rps == ('1'):
        print ('You chose rock\n ')
    if rps == ('2'):
        print ('You chose paper\n')
    if rps == ('3'):
        print ('You chose scissors\n')

    print ('Rock...')
    print ('paper...')
    print ('scissors!\n')

    rand = (random.randint(1,3))

    '''Win Statements'''
    if rand  == (1) and rps == ('3'):
        print ('I chose rock.\nI win')
    if rand  == (2) and rps == ('1'):
        print ('I chose paper.\nI win')
    if rand  == (3) and rps == ('2'):
        print ('I chose scissors.\nI win')

    '''User Win Statemenats'''
    if rand  == (1) and rps == ('2'):
        print ('I chose rock.\nYou win')
    if rand  == (2) and rps == ('3'):
        print ('I chose paper.\nYou win')
    if rand  == (3) and rps == ('1'):
        print ('I chose scissors.\nYou win')

    '''Draw Statemenats'''
    if rand  == (1) and rps == ('1'):
        print ('I chose rock.\nWe drew')
    if rand  == (2) and rps == ('2'):
        print ('I chose paper.\nWe drew')
    if rand  == (3) and rps == ('3'):
        print ('I chose scissors.\nWe drew')

while True:
    main()
    if input("\nRepeat the program? (Y/N)").strip().upper() != 'Y':
        break



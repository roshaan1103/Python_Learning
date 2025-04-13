#This is a simple word guessing game

secret_word='Roshaan'
guess=''
max_count=3
cur_count=0
limit_reached=False

while guess != secret_word and not(limit_reached) :
    if cur_count < max_count :
        guess=input('Enter your guess" ')
        cur_count += 1
    else:
        limit_reached=True
            

if limit_reached :
    print('Out of chances, You loose!')
else:
    print('YOU WIN!!')
        
 


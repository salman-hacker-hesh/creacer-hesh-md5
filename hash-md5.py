from os import system
import pyfiglet
import hashlib
system('clear')

def bnr():
  result = pyfiglet.figlet_format('hash cracer', font = 'big')
  print(result)
  print('-----------------------------------------')
  
bnr()
print('\n')
print('Telegram : https://t.me/dark_rat_py')
print('\n')
print('hash md5 = f9c24b8f961d48841a9838cca5274d8d')
print('\n')
hash = input('Enter your hash : ')
pas = input('Enter file password list : ')
file = open(pas,'r').readlines()

for i in file:
  wp = hashlib.md5(i.strip().encode()).hexdigest()
  if hash == wp :
    print(f'password is your : {i.strip()}')
    break
else : 
  print('password is not')
  exit()

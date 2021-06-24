 import os
 os.system('printf "\033[3;32m" ')
 mm=input('Entre name The LisT : ')
 os.system('clear')
 os.system('printf "\033[3;36m"')
 os.system('figlet Good - list')
 print('By : moajb ((momo PS))')
 print('-'*29)
 file=open(mm,'w')
 oo=set([])
 pop=set([])
 cc=1
  while True :
      b=input('Entre {} : '.format(kk))
      if b=='exit' :
          print('\033[3;36m')
          file.close()
          qq=open(mm, 'r' )
          jj=len(qq.readlines())
          os.system('printf "\033[3;31m"')
          print('-'*60)
          print('>> {} Passwords in ---> {} '.format(ll, mm))
          print('-'*60)
          break ;
      oo.add(b)
      for i in oo:
          if len(i) >= 6 and i not in pop :
              pop.add(i)
              file.write(i)
              file.write('\n')
          c=b+i
          q=i+b
          if len(c) >= 6 :
              file.write(c)
              file.write('\n')
          if c != d and len(d) >= 6:
          file.write(d)
          file.write('\n')

       
      cc=int(cc)+1
      print('-'*40)

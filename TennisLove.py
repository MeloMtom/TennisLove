# -*- coding: utf-8 -*-
"""
Author: Melo Mtombeni
Program to keep tennis scores while playing
"""
import numpy as np

print("***Welcome to Tennis Love!***\n")

P1 = input("Please enter name of Player 1\n")      
P2 = input("Please enter name of Player 2\n")
Nmatchs = int(input("How many matches are you playing?\n"))        
Nsets = int(input("How many sets are you playing?\n"))         
Ngames = int(input("How many games are you playing?\n"))
print("\nLet the games begin!\nFirst Game: Love All!\n",P1,': Love\n',P2,': Love\n')

#-------------------------------------------------------------------
P1Score = [0,0,0,0]            #Score throughout a match [rally, games, sets, matches]
P2Score = [0,0,0,0]

P1in = P1[0]        #short input initial during the game
P2in = P2[0]
#--------------------------------------------------------------
matchs = 0
sets = 0
games = 0
rally = 7
#--------------------------------------------------------------
def term(s):           
    s1 = [0,1,2,3,4]    
    s2 = ['Love','15','30','40','game']
    for i in s1:    
        if int(s) == s1[i]:
            return s2[i] 
#--------------------------------------------------------------
for m in range(Nmatchs):
	print("Now playing match:",m+1)
	for s in range(Nsets):
		print('Now playing set:',s+1)
		for g in range(Ngames):
			r=0
			while P1Score[0]!=4 and  P2Score[0]!=4:
				print("Who Scored?",P1[0],'for',P1,'and',P2[0],'for',P2)
				score = input('')
				if(score == P1in):
					P1Score[0] += 1
					print("Match",m+1,"Set",s+1,"Game",g+1,"Rally",r+1,": Score is now:\n",P1,':',term(P1Score[0]),"\n",P2,":",term(P2Score[0]),'\n')
				elif(score==P2in):
					P2Score[0] += 1
					print("Match",m+1,"Set",s+1,"Game",g+1,"Rally",r+1,": Score is now:\n",P1,':',term(P1Score[0]),"\n",P2,":",term(P2Score[0]),'\n')
				else:
					print("Wrong input")
				r+=1
			
			if(P1Score[0]==4):     #When game is won break
				P1Score[0]=0				#Reset rally scores for both players
				P2Score[0]=0
				P1Score[1]+=1
				print(P1,"wins Game:",g+1,'\t')
				print("Score is now:")
				print(" ","\t:\tRally\tGame\tSet\tMatch")
				print(P1,"\t:\t",P1Score[0],'\t',P1Score[1],'\t',P1Score[2],'\t',P1Score[3])
				print(P2,"\t:\t",P2Score[0],'\t',P2Score[1],'\t',P2Score[2],'\t',P2Score[3])
				print()
			elif(P2Score[0]==4):
				P1Score[0]=0
				P2Score[0]=0
				P2Score[1]+=1
				print(P2,"wins Game:",g+1,'\t')
				print("Score is now:")
				print(" ","\t:\tRally\tGame\tSet\tMatch")
				print(P1,"\t:\t",P1Score[0],'\t',P1Score[1],'\t',P1Score[2],'\t',P1Score[3])
				print(P2,"\t:\t",P2Score[0],'\t',P2Score[1],'\t',P2Score[2],'\t',P2Score[3])
				print()
			else:
				continue
	
		#reinitiate the variables
		
		if P1Score[1]>P2Score[1]:
			P1Score[2]+=1
			print(P1,"has won set:",s+1,'!\n')
			P1Score[1]=0
			P2Score[1]=0
			games = 0
			g=0
		elif(P2Score[1]>P1Score[1]):
			P2Score[2]+=1
			print(P2,"has won set:",s+1,'!\n')
			P1Score[1]=0
			P2Score[1]=0
			games = 0
			g=0
		elif(P1Score[1]==P2Score[1]):
			print(P1,"ties with",P2,'!\n')
			print("Now playing SUDDEN DEATH!")
			print("Who Scored?",P1[0],'for',P1,'and',P2[0],'for',P2)
			score = input('')
			if(score == P1in):
					P1Score[2] += 1
					print(P1,"wins the set!")
			elif(score == P2in):
					P2Score[2]+=1
					print(P2,"wins the set!")
			P1Score[1]=0
			P2Score[1]=0
			games = 0
			g=0
		#Check to contiue with the score keeping program
		cont = input("Continue with the next Game?(y/n) ")
		if cont=='y' or cont=='Y' or cont=='yes':
			games+=1
			P2Score[0]=0
			print("\nLet the games begin!")
			print("Match:",m+1,"out of",Nmatchs)
			print("Set:",s+1,'out of',Nsets)
			print(" ","\t:\tRally\tGame\tSet\tMatch")
			print(P1,"\t:\t",P1Score[0],'\t',P1Score[1],'\t',P1Score[2],'\t',P1Score[3])
			print(P2,"\t:\t",P2Score[0],'\t',P2Score[1],'\t',P2Score[2],'\t',P2Score[3])
			print()
			continue
		elif(cont=='n' or cont=='N' or cont=='no'):
			print("***Thanks for playing Tennis Love!***")
			break
		else:
			print("Wrong input")
		
		s+=1
	if P1Score[2]>P2Score[2]:
			P1Score[3]+=1
			print("Game. Set. Match.")
			print(P1,"is victorious!\n")
			P1Score[2]=0
			P2Score[2]=0
			games = 0
			g=0
	elif(P2Score[2]>P1Score[2]):
			P2Score[3]+=1
			print("Game. Set. Match.")
			print(P2,"is victorious\n")
			P1Score[2]=0
			P2Score[2]=0
			games = 0
			g=0
	elif(P1Score[2]==P2Score[2]):
			print("Game. Set. Match.")
			print(P1,"ties with",P2,'!\n')
			P1Score[2]=0
			P2Score[2]=0
			games = 0
			g=0	
	m+=1
	print(" ","\t:\tRally\tGame\tSet\tMatch")
	print(P1,"\t:\t",P1Score[0],'\t',P1Score[1],'\t',P1Score[2],'\t',P1Score[3])
	print(P2,"\t:\t",P2Score[0],'\t',P2Score[1],'\t',P2Score[2],'\t',P2Score[3])
	print()
	print("***Thanks for playing Tennis Love!***")

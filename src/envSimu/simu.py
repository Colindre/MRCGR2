from tkinter import *
from robot import Robot
import time
import random
from robot import angleVecteur

#Création fenetre 
Largeur =400
Hauteur= 200
root=Tk()
canvas = Canvas(root,width=Largeur,height=Largeur,background ="white")
canvas.pack(fill="both",expand=True)


#Création robot 
robot1 = Robot(200,0,40,20)
#Création cercle représentant le robot
rbt = canvas.create_oval(robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20,width=2,fill="red") 
vecteur =(0,0)
verif = True

#Deplacement bas
def action_depl():	

	"""dx=random.uniform(-5.0,5.0)
	dy=random.uniform(-5.0,5.0)
	vecteur= (dx,dy)""" 
	
	global vecteur
	global verif 
	vecteur=(0,1)
	while(verif):
		robot1.deplacement(vecteur)
		canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)
		canvas.after(25,action_depl)
		return
			
#Deplacement droite
def action_depld():	
	"""dx=random.uniform(0.0,10.0)
	dy=random.uniform(0.0,10.0)
	vecteur= (dx,dy)"""
	
	global vecteur
	global verif
	vecteur = (1,0)
	while(verif):
		robot1.deplacement(vecteur)
		canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)
		canvas.after(25,action_depld)	
		return

#Deplacement haut
def action_deplh():	
	"""dx=random.uniform(0.0,10.0)
	dy=random.uniform(0.0,10.0)
	vecteur= (dx,dy)"""
	
	global vecteur
	global verif
	vecteur = (0,-1)
	while(verif):
		robot1.deplacement(vecteur)
		canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)
		canvas.after(25,action_deplh)	
		return

#Deplacement gauche
def action_deplg():	
	"""dx=random.uniform(0.0,10.0)
	dy=random.uniform(0.0,10.0)
	vecteur= (dx,dy)"""
	
	global vecteur
	global verif
	vecteur = (-1,0)
	while(verif):
		robot1.deplacement(vecteur)
		canvas.coords(rbt,robot1.posx,robot1.posy,robot1.posx+20,robot1.posy+20)
		canvas.after(25,action_deplg)	
		return


def verifF():
	global verif
	verif =False
	return 

def verifT():
	global verif
	verif =True
	return

#BOUTON

bouton_1 = Button(root,text="Deplacement bas",width=20, command=action_depl)
bouton_1.pack(pady=10)

bouton_2= Button(root,text="Deplacement droite",width=20, command=action_depld)
bouton_2.pack(pady=10)

bouton_3= Button(root,text="Deplacement haut",width=20, command=action_deplh)
bouton_3.pack(pady=10)

bouton_4= Button(root,text="Deplacement gauche",width=20, command=action_deplg)
bouton_4.pack(pady=10)

bouton_5= Button(root,text="Arret",width=20, command=verifF)
bouton_5.pack(side=RIGHT,pady=10)

bouton_6= Button(root,text="Replay",width=20, command=verifT)
bouton_6.pack(side=LEFT, pady=10)
bouton_quit = Button(root,text="quitte",width=20, command=root.quit)
bouton_quit.pack(side=BOTTOM, pady=10)


root.mainloop()

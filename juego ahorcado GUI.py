
from tkinter import *

class Interfaz():
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title(('Juego Ahorcado'))
		self.ventana.resizable(0,0)
		self.ventana.iconbitmap('icono.ico')

		self.frame1=Frame(self.ventana, bg='#845C32')
		self.frame1.pack()

		#Variables
		self.peli=''
		self.peli_=''
		self.vidas=6
		self.letras_erroneas=''
		self.letras_correctas=''
		self.path_imagenes=('0.png','1.png','2.png','3.png','4.png','5.png','6.png')

		#Labels
		self.label_titulo=Label(self.frame1, text='JUEGO DEL AHORCADO', font=('carnivalee freakshow',40)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_titulo.grid(row=0, padx=10, pady=10)

		self.label_peli=Label(self.frame1, text='Pelicula', font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_peli.grid(row=1, pady=10)

		self.pelicula=StringVar()
		self.entry_peli=Entry(self.frame1, textvariable=self.pelicula, width=40, font=('avenir',15)
			, fg='black', justify='center')
		self.entry_peli.grid(row=2, pady=10)

		self.boton_confirmacion=Button(self.frame1,text='Confirmar', width=10
			, font=('carnivalee freakshow',14), fg='white', bg='#1F0F00'
			, command= lambda: self.funcion_confirmar())
		self.boton_confirmacion.grid(row=3, pady=10)

		self.label_letra=Label(self.frame1, text='Introduce una letra',font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_letra.grid(row=4, pady=10)

		self.letras=StringVar()
		self.entry_letra=Entry(self.frame1, textvariable=self.letras, width=8, font=('avenir',15)
			, fg='black', justify='center', state='disable')
		self.entry_letra.grid(row=5, pady=10)

		self.boton_probar=Button(self.frame1, text='Probar', width=10
			, font=('carnivalee freakshow',14), fg='white', bg='#1F0F00'
			,  state='disable', command= lambda: self.funcion_probar())
		self.boton_probar.grid(row=6, pady=10)

		self.label_erroneas=Label(self.frame1, text='Letras erroneas', font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_erroneas.grid(row=7, pady=10)

		self.label_mostrar_erroneas=Label(self.frame1, width=10, font=('avenir',15)
			, fg='black', bg='#A58F78', relief='raised', justify='center')
		self.label_mostrar_erroneas.grid(row=8, pady=10)

		self.label_vidas=Label(self.frame1, text='Vidas', font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_vidas.grid(row=9, pady=10)

		self.label_mostrar_vidas=Label(self.frame1, width=3, text=self.vidas, font=('carnivalee freakshow',20)
			, fg='black', bg='#A58F78', relief='raised', justify='center')
		self.label_mostrar_vidas.grid(row=10, pady=10)

		self.imagen=PhotoImage(file=self.path_imagenes[self.vidas])
		self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)

		self.boton_retry=Button(self.frame1, text='Retry', width=10
			, font=('carnivalee freakshow',14), fg='white', bg='#1F0F00'
			, command= lambda: self.funcion_retry())
		self.boton_retry.grid(row=12, pady=10)

		self.popup_explicacion()


	#-----------POPUP-------------
	#popup explicación
	def popup_explicacion(self):
		popup =Tk()
		popup.resizable(0,0)
		popup.config(bg='#845C32')

		label=Label(popup, text='Escribe una película, sin que te vean, y dale al botón confirmar.\nAhora, tu contrincante deberá introducir una letra y pulsar probar.\nTiene 6 vidas.\n¿Acabará ahorcado?'
			, font=('avenir',20), fg='#190D00', bg='#4F2C06', relief='raised')
		label.pack(side="top", fill="both", pady=10)

		boton_close=Button(popup, text="Comienza a jugar", width=20, font=('carnivalee freakshow',14)
			, fg='white', bg='#1F0F00', pady=10, command = popup.destroy)
		boton_close.pack()


	#popup ganaste o perdiste
	def popup(self, msg):
		popup =Tk()
		popup.geometry('500x200')
		popup.resizable(0,0)
		popup.config(bg='#845C32')

		label=Label(popup, text=msg, font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		label.pack(side="top", fill="both", pady=10)

		label_peli=Label(popup, text=f'La peli era: {self.peli}', font=('carnivalee freakshow',20)
			, fg='black', bg='#A58F78', relief='raised', justify='center')
		label_peli.pack(side="top", fill="both", pady=10)

		boton_close=Button(popup, text="Volver a Jugar", width=15, font=('carnivalee freakshow',14)
			, fg='white', bg='#1F0F00', pady=10, command = popup.destroy)
		boton_close.pack()

		self.funcion_retry()

		popup.mainloop()


	#------------FUNCIONES---------

	#boton_confirmacion
	def funcion_confirmar(self):
		self.peli=self.pelicula.get().upper()

		reemplazar=(('Á','A'),('É','E'),('Í','I'),('Ó','O'),('Ú','U'))
		for i,j in reemplazar:
			self.peli=self.peli.replace(i,j)

		for i in self.peli:
			if i==' ':
				self.peli_=self.peli_+'  '
			else:
				self.peli_=self.peli_+'_ '

		self.pelicula.set(self.peli_)
		self.entry_peli.config(state='disable')
		self.boton_confirmacion.config(state='disable')
		self.entry_letra.config(state='normal')
		self.boton_probar.config(state='normal')

	#boton_probar
	def funcion_probar(self):
		if self.vidas>0:
			peli_2=''
			letra=self.letras.get().upper()
			if letra not in self.peli:
				if letra not in self.letras_erroneas:
					self.vidas-=1
					self.letras_erroneas+=letra+' '
					self.imagen=PhotoImage(file=self.path_imagenes[self.vidas])
					self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)

				if self.vidas==0:
					self.entry_letra.config(state='disable')
					self.boton_probar.config(state='disable')
					self.popup('¡PERDISTE!')
				else:
					self.label_mostrar_vidas['text'] = self.vidas
					self.label_mostrar_erroneas['text']= self.letras_erroneas
					self.pelicula.set(self.peli_)
			else:
				if letra not in self.letras_correctas:
					self.letras_correctas+=letra
				for i in self.peli:
					if i==' ':
						peli_2=peli_2+'  '
					elif i in self.letras_correctas:
						peli_2=peli_2+i
					else:
						peli_2=peli_2+'_ '
				self.peli_=peli_2
			self.letras.set('')
			self.pelicula.set(self.peli_)

			if self.peli==self.peli_:
				self.entry_letra.config(state='disable')
				self.boton_probar.config(state='disable')
				self.popup('¡GANASTE!')

	#función para reiniciar los valores
	def funcion_retry(self):
		self.peli=''
		self.peli_=''
		self.vidas=6
		self.letras_erroneas=''
		self.letras_correctas=''
		self.entry_letra.config(state='disable')
		self.letras.set('')
		self.entry_peli.config(state='normal')
		self.pelicula.set('')
		self.label_mostrar_vidas['text']=6
		self.label_mostrar_erroneas['text']=''
		self.boton_confirmacion.config(state='normal')
		self.boton_probar.config(state='disable')
		self.imagen=PhotoImage(file=self.path_imagenes[self.vidas])
		self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)


ventana=Tk()
juego=Interfaz(ventana)
ventana.mainloop()
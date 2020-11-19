
from tkinter import *
from tkinter import messagebox

class Interfaz():
	def __init__(self,ventana):
		self.ventana=ventana
		self.ventana.title(('Juego Ahorcado'))
		self.ventana.resizable(0,0)
		self.ventana.iconbitmap('imagenes/icono.ico')
		self.ventana.config(bg='#845C32',cursor='man')
		self.ventana.attributes("-fullscreen", True)
		self.ventana.bind('<Escape>', lambda i : self.message_salir_escape(i))

		#frame

		self.frame1=Frame(self.ventana, bg='#845C32')
		self.frame1.pack(expand=1, anchor='center')

		#Barra menu

		barra_menu=Menu(self.ventana)

		menu_inicio=Menu(barra_menu, tearoff=0)
		menu_inicio.add_command(label='Nueva partida', command= lambda: self.funcion_retry())
		menu_inicio.add_command(label='Editar película', command= lambda: self.funcion_editar_pelicula())
		menu_inicio.add_separator()
		menu_inicio.add_command(label='Salir', command= lambda: self.message_salir())
		barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

		menu_ayuda=Menu(barra_menu, tearoff=0)
		menu_ayuda.add_command(label='Instrucciones', command= lambda: self.popup_explicacion())
		menu_ayuda.add_command(label='Acerca de...', command= lambda: self.message_acerca_de())
		barra_menu.add_cascade(label='Ayuda', menu=menu_ayuda)

		barra_menu.add_cascade(label='Salir',command= lambda: self.message_salir())

		self.ventana.config(menu=barra_menu)

		#Variables

		self.peli=''
		self.peli_=''
		self.vidas=6
		self.letras_erroneas=''
		self.letras_correctas=''

		#Labels

		self.label_titulo=Label(self.frame1, text='JUEGO DEL AHORCADO', font=('carnivalee freakshow',40)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_titulo.grid(row=0, padx=10, pady=10)

		self.label_peli=Label(self.frame1, text='Pelicula', font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_peli.grid(row=1, pady=10)

		self.pelicula=StringVar()
		self.entry_peli=Entry(self.frame1, textvariable=self.pelicula, width=100, font=('avenir',15)
			, fg='black', justify='center',bd=2, relief='sunken')
		self.entry_peli.grid(row=2, pady=10, padx=10)

		self.boton_confirmacion=Button(self.frame1,text='Confirmar', width=10
			, font=('carnivalee freakshow',14), fg='white', bg='#1F0F00'
			, command= lambda: self.funcion_confirmar())
		self.boton_confirmacion.grid(row=3, pady=10)

		self.label_letra=Label(self.frame1, text='Introduce una letra',font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		self.label_letra.grid(row=4, pady=10)

		self.letras=StringVar()
		self.entry_letra=Entry(self.frame1, textvariable=self.letras, width=8, font=('avenir',15)
			, fg='black', justify='center', state='disable', bd=2, relief='sunken')
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

		self.imagen=PhotoImage(file=('imagenes/6.png'))
		self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)

		self.boton_retry=Button(self.frame1, text='Retry', width=10
			, font=('carnivalee freakshow',14), fg='white', bg='#1F0F00'
			, command= lambda: self.funcion_retry())
		self.boton_retry.grid(row=12, pady=10)


	#-----------POPUP-------------

	#popup explicación
	def popup_explicacion(self):
		popup =Toplevel(self.ventana)
		popup.title(('Info'))
		popup.resizable(0,0)
		popup.config(bg='#845C32')
		popup.iconbitmap('imagenes/icono.ico')
		popup.transient(self.ventana)

		label_titulo=Label(popup, text='INSTRUCCIONES', font=('carnivalee freakshow',30)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		label_titulo.pack(side="top", fill="both", pady=10)

		label=Label(popup, text='El juego consiste en adivinar el título de la película, pudiendo probar\n'
			'letras para ver si estas se encuentran en el título.\n'
			'\n'
			'¿Cómo se juega?\n'
			'\n'
			'JUGADOR 1:\n'
			'Escribe la película. ¡Qué no te vean!\n'
			'Pulsa el botón CONFIRMAR. La película se esconderá.\n'
			'Si el otro jugador no consigué adivinar la película serás el vencedor.\n'
			'\n'
			'JUGADOR 2:\n'
			'Escribe una letra que creas que se encuentra en el título de la \n'
			'película y pulsa el botón PROBAR.'
			'Si esta se encuentra en el título, \n'
			'se desvelerá, sino, perderás una vida.\n'
			'¡OJO! Sólo puedes escribir una letra cada vez.\n'
			'Si desvelas la película antes de perder todas las vidas serás el vencedor.\n'
			'\n'
			'¿Terminarás ahorcado?\n'
			, font=('avenir',14), fg='#190D00', bg='#A58F78', relief='raised', justify='left')
		label.pack(side="top", fill="both", pady=10, padx=10)

		boton_close=Button(popup, text="Comienza a jugar", width=20, font=('carnivalee freakshow',14)
			, fg='white', bg='#1F0F00', pady=10, command = popup.destroy)
		boton_close.pack()


	#popup ganaste o perdiste
	def popup_resultado(self, msg):
		popup =Toplevel(self.ventana, bg='#845C32')
		popup.title(msg)
		popup.resizable(0,0)
		popup.config(bg='#845C32')
		popup.iconbitmap('imagenes/icono.ico')
		popup.transient(self.ventana)
		popup.minsize(500,260)

		label=Label(popup, text=msg, font=('carnivalee freakshow',40)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		label.pack(side="top", fill="both", pady=10, padx=5)

		label=Label(popup, text='La pelicula era:', font=('carnivalee freakshow',20)
			, fg='#190D00', bg='#4F2C06', relief='raised')
		label.pack(side="top",  pady=10, padx=5)

		label_peli=Label(popup, text=self.peli, font=('carnivalee freakshow',20)
			, fg='black', bg='#A58F78', relief='raised', justify='center')
		label_peli.pack(side="top", fill="both", pady=10, padx=15)

		boton_close=Button(popup, text="Volver a Jugar", width=15, font=('carnivalee freakshow',14)
			, fg='white', bg='#1F0F00', pady=10, command = lambda: popup.destroy())
		boton_close.pack()

		self.funcion_retry()

		popup.mainloop()


	#------------FUNCIONES---------

	#boton_confirmacion
	def funcion_confirmar(self):
		self.peli=self.pelicula.get().upper()

		en_blanco=0
		for i in self.peli:
			if i==' ':
				en_blanco+=1

		if len(self.peli)!=en_blanco:
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
		else:
			self.message_peli_en_blanco()
			self.pelicula.set('')

	#boton_probar
	def funcion_probar(self):
		if self.vidas>0:
			peli_2=''
			letra=self.letras.get().upper()

			if letra=='':
				self.message_letra_en_blanco()

			else:
				en_blanco=0
				for i in letra:
					if i==' ':
						en_blanco+=1

				if len(letra)!=en_blanco:				
					if letra!=' ':
						if len(letra)!=1:
							self.message_una_letra()
							self.letras.set('')

						else:
							reemplazar=(('Á','A'),('É','E'),('Í','I'),('Ó','O'),('Ú','U'))
							for i,j in reemplazar:
								letra=letra.replace(i,j)

							if letra not in self.peli:
								if letra not in self.letras_erroneas:
									self.vidas-=1
									self.letras_erroneas+=letra+' '
									self.imagen=PhotoImage(file=('imagenes/'+str(self.vidas)+'.png'))
									self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)

								if self.vidas==0:
									self.entry_letra.config(state='disable')
									self.boton_probar.config(state='disable')
									self.popup_resultado('¡PERDISTE!')
								else:
									self.label_mostrar_vidas['text'] = self.vidas
									self.label_mostrar_erroneas['text']= self.letras_erroneas
									self.pelicula.set(self.peli_)
									
							else:
								if letra not in self.letras_correctas:
									self.letras_correctas+=letra
								for i in self.peli:
									if i==' ':
										peli_2=peli_2+' '
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
								self.popup_resultado('¡GANASTE!')

				else:
					self.message_letra_espacios()
					self.letras.set('')

	#función para descubri película
	def funcion_editar_pelicula(self):
		self.entry_peli.config(state='normal')
		self.pelicula.set(self.peli)
		self.peli_=''
		self.boton_confirmacion.config(state='normal')
		self.entry_letra.config(state='disable')
		self.boton_probar.config(state='disable')

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
		self.imagen=PhotoImage(file=('imagenes/6.png'))
		self.label_imagen=Label(self.frame1, image=self.imagen).grid(row=11, pady=10)


	#funcion mensaje salir con escape
	def message_salir_escape(self,label):
		valor=messagebox.askquestion('Salir', '¿Estás seguro?')
		if valor=='yes':
			self.ventana.destroy()

	#función mensaje salir
	def message_salir(self):
		valor=messagebox.askquestion('Salir', '¿Estás seguro?')
		if valor=='yes':
			self.ventana.destroy()

	#función mensaje Acerca de...
	def message_acerca_de(self):
		messagebox.showinfo('Juego del Ahorcado', 'Juego del Ahorcado elaborado por Luis Blanco.')

	#función mensaje una letra
	def message_una_letra(self):
		messagebox.showerror('Error', '¡¡No tan rápido cowboy!!\nSólo puedes introducir una letra cada vez.')

	#función mensaje peli en blanco
	def message_peli_en_blanco(self):
		messagebox.showerror('Error', '¡¡No tan rápido cowboy!!\nIntroduce un nombre de película.')

	#función mensaje letra en blanco
	def message_letra_en_blanco(self):
		messagebox.showerror('Error', '¡¡No tan rápido cowboy!!\nIntroduce una letra.')

	#función mensaje letra en blanco
	def message_letra_espacios(self):
		messagebox.showerror('Error', '¡¡No tan rápido cowboy!!\nLos espacios ya sabes donde están. ¡Prueba letras!')

if __name__=='__main__':
	ventana=Tk()
	juego=Interfaz(ventana)
	ventana.mainloop()
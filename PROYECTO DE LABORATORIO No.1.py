#PROYECTO DE LABORATORIO No.1 - Pamela Sanabria y Melissa Juárez
import turtle
o1=0
to3=-15

#Imprimira el cuerpo de la persona   
def Humano(x,y):
    t=turtle.Turtle()
    t.speed(1000)
    t.hideturtle()
    t.pensize(3)
    t.setheading(0)
    t.teleport(x,y)
    t.color("burlywood1")
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    t.color("black")
    t.circle(45)
    #Dibujar Ojos
    t.teleport(x-15,y+43)
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.teleport(x+15,y+43)
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    #Dibujar boca
    t.teleport(x-12,y+30)
    t.color("black")
    t.setheading(-90)
    t.circle(12,180)
    t.setheading(0)
    #Dibujar cuerpo
    t.teleport(x-45,y)
    t.color("DarkOrange")
    t.begin_fill()
    for i in range(4):
        d = 45*2 if i%2 == 0 else 100
        t.forward(d)
        t.right(90)
    t.end_fill()
    t.color("black")
    for i in range(4):
        d = 45*2 if i%2 == 0 else 100
        t.forward(d)
        t.right(90)
    t.teleport(x-43,y-100)
    t.color("DarkBlue")
    t.begin_fill()
    for i in range(4):
        d = 38 if i%2 == 0 else 90
        t.forward(d)
        t.right(90)
    t.end_fill()
    t.color("black")
    for i in range(4):
        d = 38 if i%2 == 0 else 90
        t.forward(d)
        t.right(90)
    t.teleport(x+4,y-100)
    t.color("DarkBlue")
    t.begin_fill()
    for i in range(4):
        d = 38 if i%2 == 0 else 90
        t.forward(d)
        t.right(90)
    t.end_fill()
    t.color("black")
    for i in range(4):
        d = 38 if i%2 == 0 else 90
        t.forward(d)
        t.right(90)
    #Dibujar los brazos
    t.teleport(x+45,y)
    t.color("burlywood1")
    t.begin_fill()
    for i in range(4):
        d = 20 if i%2 == 0 else 80
        t.forward(d)
        t.right(90)
    t.end_fill()
    t.color("black")
    for i in range(4):
        d = 20 if i%2 == 0 else 80
        t.forward(d)
        t.right(90)
    t.teleport(x-45-20,y)
    t.color("burlywood1")
    t.begin_fill()
    for i in range(4):
        d = 20 if i%2 == 0 else 80
        t.forward(d)
        t.right(90)
    t.end_fill()
    t.color("black")
    for i in range(4):
        d = 20 if i%2 == 0 else 80
        t.forward(d)
        t.right(90)

#Imprimira un arbol
def Arbol(c1,c2,tamaño = 20,color = "green"):
    t=turtle.Turtle()
    t.speed(1000)
    t.hideturtle()
    t.teleport(c1,c2)
    t.color("brown")
    t.setheading(90)
    t.pensize(tamaño*0.6)
    t.forward(tamaño)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(tamaño)
    t.end_fill()        

#Imprimira el recuadro de fondo
def Back():
    #libreria turtle 
    turtle.setup(width=1100,height=900, startx=0, starty=0)
    back = turtle.Turtle() 
    back.speed(0)
    back.teleport(-450, 360)
    back.color("black")
    for i in range(2): 
        back.forward(900) 
        back.right(90) 
        back.forward(660) 
        back.right(90) 
    y=330
    for i in range(2): 
        back.teleport(-450, y)
        back.forward(900) 
        y=-160
    back.hideturtle()

#Imprimira el cielo
def cielo():
    # Configuración inicial de la pantalla de Turtle 
    turtle.speed(0)
    turtle.teleport(-449, 329)
    turtle.color("skyblue")
    turtle.fillcolor("skyblue")
    turtle.begin_fill()
    for i in range(2): 
        turtle.forward(898) 
        turtle.right(90) 
        turtle.forward(488) 
        turtle.right(90) 
    turtle.end_fill()
    
    # Dibujar el sol
    turtle.penup()
    turtle.goto(200, 200)
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.hideturtle()

#Imprimira el cesped
def Grama():
    grama = turtle.Turtle()
    grama.speed(0)
    grama.teleport(-449,-9)
    grama.color('green')
    grama.fillcolor('green')
    grama.begin_fill()
    for i in range(2):
        grama.forward(898)
        grama.right(90)
        grama.forward(150)
        grama.right(90)
    grama.end_fill()
    grama.hideturtle()

#Imprimira oruga
def Oruga(or1,or2):
    o1=0 
    x=0
    x1=0
    a=0
    oruga=turtle.Turtle()
    oruga.speed(0)
    oruga.color("black")
    oruga.fillcolor(color)
    oruga.begin_fill()
    oruga.teleport(0+or1,0+or2)
    for i in range(6):
        oruga.teleport(-10+or1+x1,-10+or2)
        for i in range(3):
            oruga.forward(15)
            oruga.left(120)
        x1+=25
    for i in range(6):
        oruga.teleport(0+o1+or1,0+or2)
        oruga.circle(20)
        o1+=25
        if x==5:
            oruga.teleport(0+o1+or1,25+or2) 
            oruga.circle(20)
        x+=1   
    oruga.left(80)
    for i in range(2):
        oruga.teleport(150+a+or1,65+or2)
        oruga.forward(45)
        a+=10
    oruga.end_fill()
    oruga.teleport(160+or1,45+or2)
    oruga.fillcolor("black")
    oruga.begin_fill()
    oruga.circle(4)
    oruga.end_fill()
    oruga.hideturtle()

#Imprimira un corazón
def corazon(cor1,cor2):
    corazon = turtle.Turtle()
    corazon.speed(0)
    corazon.hideturtle()
    corazon.teleport(cor1,cor2)
    corazon.color("black")
    corazon.fillcolor("red")
    corazon.begin_fill()
    corazon.left(140)
    corazon.forward(50) 
    corazon.circle(-25, 200)  
    corazon.setheading(60)
    corazon.circle(-25, 200)  
    corazon.forward(50)  
    corazon.end_fill()
    corazon.hideturtle()

#Imprimira Flor
def Flor(f1,f2):
    f = turtle.Turtle()
    f.speed(0)  
    f.teleport(f1,f2)
    f.color("LightPink")  
    f.begin_fill()  
    for i in range(7):
        for i in range(2):
            f.circle(20, 70)  
            f.left(110) 
        f.left(51.43)       
    f.end_fill() 
    f.hideturtle()

#Imprimira nubes
def Nube(nu1,nu2):
    n = turtle.Turtle()
    n.speed(0)  
    n.color("cyan")  
    n.fillcolor("white")
    n.begin_fill()             
    for i in range(3):
        n.teleport(nu1+i*70,nu2)
        n.circle(50)
    n.end_fill() 
    n.hideturtle()


def Escena1():
    Back()
    cielo()
    Nube(-350,200)
    Nube(-100,215)
    Grama()
    Flor(-300,-50)
    Flor(-200,-60)
    Flor(-40,-100)
    Flor(-100,-80)
    Flor(-400,-55)
    Flor(-258,-100)
    Flor(-380,-100)
    Flor(300,-50)
    Flor(200,-60)
    Flor(40,-100)
    Flor(100,-80)
    Flor(400,-55)
    Flor(258,-100)
    Flor(380,-100)
    Oruga(200,-135)
    Humano(-100,50)



def Escena2():
    Back()
    cielo()
    Nube(-350,200)
    Nube(-100,215)
    Grama()
    Flor(-300,-50)
    Flor(-200,-60)
    Flor(-40,-100)
    Flor(-100,-80)
    Flor(-400,-55)
    Flor(-258,-100)
    Flor(-380,-100)
    for i in range(8): Arbol(-350+i*100,10,70,"GreenYellow")
    Humano(-100,50)
    Oruga(0,-135)


def Escena3():
    Back()
    cielo()
    Grama()
    for i in range(1): Arbol(300+i*100,-10,100, color)
    for i in range(8): Arbol(-350+i*100,-10,70,"GreenYellow")
    Humano(-80,50)
    Oruga(0, -135)

def Escena4():
    Back()
    cielo()
    Grama()
    for i in range(8): Arbol(-350+i*100,-10,70,"OliveDrab4")
    for i in range(1): Arbol(300+i*100,-100,100, color)
    Oruga(-100,-135)
    Humano(200,50)

def Escena5():
    Back()
    cielo()
    Nube(-350,200)
    Nube(-100,215)
    Grama()
    Flor(-300,-50)
    Flor(-200,-60)
    Flor(-40,-100)
    Flor(-100,-80)
    Flor(-400,-55)
    Flor(-258,-100)
    Flor(-380,-100)
    Flor(300,-50)
    Flor(200,-60)
    Flor(40,-100)
    Flor(100,-80)
    Flor(400,-55)
    Flor(258,-100)
    Flor(380,-100)
    corazon(50, 150)
    Humano(80,50)
    Oruga(-80, -135)

#Se le pedira los datos a la personas
print("El Encuentro en el Bosque Encantado")
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
n1=0
#Mientras la variable n1 sea 0 
while n1==0:
    #Se imprimira las posibilidades de los colores   
    print("Estos son los colores que puede utlizar: ")
    print("R = Rojo")
    print("A = Amarillo")
    print("M = Morado")
    print("P = Rosado")
    print("V = Verde claro")
    #Se lee el dato ingresado
    colorin = input('¿Opción a elegir? - ').lower()
    if colorin== 'r':
        color = 'red'
        n1=1
    elif colorin=='a':
        color = 'yellow'
        n1=1
    elif colorin=='m':
        color = 'DarkOrchid1'       
        n1=1
    elif colorin=='p':
        color = 'DeepPink'
        n1=1
    elif colorin=='v':
        color = 'lightgreen'
        n1=1
    else:
        print("El color elegido no esta en las opciones, repita")
        print()

n=0
while n==0:
    print()
    print("Elija una escena a visualizar")
    print("1 = Escena 1 'El descubrimiento'")
    print("2 = Escena 2 'La aventura en el bosque'")
    print("3 = Escena 3 'El árbol encantado'")
    print("4 = Escena 4 'El deseo'")
    print("5 = Escena 5 'La magia del bosque'")
    print("6 = Salir del ciclo")
    escena = int(input('¿Opción a elegir? - '))
    if escena == 1:
        turtle.clearscreen()
        Escena1()
        turtle.speed(0)
        turtle.title("El Encuentro en el Bosque Encantado")
        turtle.color('black')
        turtle.teleport(-445,335)
        turtle.write(f"El descubrimiento",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-185)
        turtle.write(f"Un soleado día de primavera, Tomás un niño de {edad} años, estaba jugando en su jardín cuando una",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-205)
        turtle.write(f"oruga de su color favorito capturó su atención. Fascinado por su belleza, decidió seguir",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-225)
        turtle.write(f"cuidadosamente a la pequeña criatura mientras se deslizaba entre las plantas y las flores.",move=False,font=("Arial",15,"normal"))
    elif escena == 2:
        turtle.clearscreen()
        Escena2()
        turtle.speed(0)
        turtle.title("El Encuentro en el Bosque Encantado")
        turtle.color('black')
        turtle.teleport(-445,335)
        turtle.write(f"La aventura en el bosque",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-185)
        turtle.write(f"La oruga llamada {nombre} llevó a Tomás a través de un agujero en la cerca del jardín y lo guió",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-205)
        turtle.write(f"hacia un bosque cercano que parecía envuelto en un misterio.Con cada paso, el bosque se volvía",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-225)
        turtle.write(f"más espeso y más silencioso, pero Tomás seguía decidido a seguir a su nueva amiga.",move=False,font=("Arial",15,"normal"))
    elif escena == 3:
        turtle.clearscreen()
        Escena3()
        turtle.speed(0)
        turtle.title("El Encuentro en el Bosque Encantado")
        turtle.color('black')
        turtle.teleport(-445,335)
        turtle.write(f"El árbol encantado",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-185)
        turtle.write(f"Después de un largo camino, llegaron a un campo en el bosque donde se alzaba un árbol majestuoso",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-205)
        turtle.write(f"y antiguo, cuyas ramas parecían susurrar secretos ancestrales. La oruga le explicó a",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-230)
        turtle.write(f"Tomás que este era el Árbol de los Deseos, que tenía el poder de conceder los anhelos",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-250)
        turtle.write(f"más profundos de aquellos lo suficientemente valientes para encontrarlo.",move=False,font=("Arial",15,"normal"))
    elif escena == 4:
        turtle.clearscreen()
        Escena4()
        turtle.speed(0)
        turtle.title("El Encuentro en el Bosque Encantado")
        turtle.color('black')
        turtle.teleport(-445,335)
        turtle.write(f"El deseo",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-190)
        turtle.write(f"Con el corazón lleno de esperanza, Tomás se acercó al árbol y formuló su deseo con voz temblorosa,",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-210)
        turtle.write(f"quería que su abuelita enferma se recuperara y volviera a estar sana y feliz como antes. La oruga",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-230)
        turtle.write(f"llamada {nombre}, se ofreció a ser la mensajera entre Tomás y el arbol encantado",move=False,font=("Arial",15,"normal"))
        
    elif escena == 5:
        turtle.clearscreen()
        Escena5()
        turtle.speed(0)
        turtle.title("La magia del bosque")
        turtle.color('black')
        turtle.teleport(-445,335)
        turtle.write(f"La magia del bosque",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-190)
        turtle.write(f"Al día siguiente, Tomás se despertó con la noticia de que su abuelita se sentía mucho mejor.",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-210)
        turtle.write(f"Asombrado y agradecido, corrió al jardín y encontró a la oruga {nombre} esperándolo entre las flores.",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-230)
        turtle.write(f"Juntos, celebraron el milagro que habían presenciado y se prometieron ser amigos para siempre,",move=False,font=("Arial",15,"normal"))
        turtle.teleport(-447,-250)
        turtle.write(f"recordando siempre el poder de la naturaleza y la magia del bosque.",move=False,font=("Arial",15,"normal"))
    elif escena == 6:
        turtle.bye()
        print('Gracias por su atención :)')
        n=1
    else:
         print('El no. de escena no está definido, vuelva a intentar')

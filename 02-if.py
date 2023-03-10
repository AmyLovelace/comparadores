edad = 15

if edad > 65: #las evaluaciones se hacen de arriba hacia abajo la primera condicion que se evalua en 
    print ("puedes ver la pelicula con super descuento")#el print tiene que NECESARIAMENTE ESTAR ANIDADO en if o else 

elif edad >54 :
    print ("puede ver la pelicula con descuento")
elif edad > 17 :
    print("puedes ver la pelicula")

else:
   
    print("no puedes entrar")
print ("Listo")
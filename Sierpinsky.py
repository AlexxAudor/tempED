import turtle

def dibujarTriangulo(puntos,color,triangulo):
    triangulo.fillcolor(color)
    triangulo.up()
    triangulo.goto(puntos[0][0],puntos[0][1])
    triangulo.down()
    triangulo.begin_fill()
    triangulo.goto(puntos[1][0],puntos[1][1])
    triangulo.goto(puntos[2][0],puntos[2][1])
    triangulo.goto(puntos[0][0],puntos[0][1])
    triangulo.end_fill()

def obtenerMitad(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(puntos,grado,triangulo):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    dibujarTriangulo(puntos,colormap[grado],triangulo)
    if grado > 0:
        sierpinski([puntos[0],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, triangulo)
        sierpinski([puntos[1],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[1], puntos[2])],
                   grado-1, triangulo)
        sierpinski([puntos[2],
                        obtenerMitad(puntos[2], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, triangulo)

def main():
   triangulo = turtle.Turtle()
   miVentana = turtle.Screen()
   misPuntos = [[-100,-50],[0,100],[100,-50]]
   sierpinski(misPuntos,3,triangulo)
   miVentana.exitonclick()

main()
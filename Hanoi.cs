using System;
using System.Collections.Generic;
using System.Text;

namespace Torres_de_Hanoi
{
class Hanoi
{
int pasos = 0;
static void Main(string[] args)
{
Hanoi h = new Hanoi();
char TorreInicial='A';
char TorreAuxiliar='B';
char TorreFinal='C';
int n;
String a;

Console.WriteLine("Número de discos: ");
a = Console.ReadLine();
n = int.Parse(a);

Console.WriteLine("\nLos movimientos a realizar son: \n");
h.hanoi(n,TorreInicial,TorreAuxiliar,TorreFinal);
Console.WriteLine("\nEl número total de pasos es: " + h.pasos + "\n");
Console.ReadLine();
}

void hanoi(int n, char c, char a, char f)
{

if(n==1)
{
Console.WriteLine(c + " -> " + f);
pasos++;
}


else
{
pasos++;
hanoi(n-1,c,f,a);
Console.WriteLine(c + " -> " + f);
hanoi(n-1,a,c,f);
}


}

}

}
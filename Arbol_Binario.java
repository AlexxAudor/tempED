public class Arbol_Binario {

    Nodo Raiz;

    public Arbol_Binario(){
        Raiz= null;
    }

    public void insertar_Valor(int i){
        Nodo nodo = new Nodo(i);


        if(Raiz == null){
            Raiz = nodo;
        }else{
            Nodo aux = Raiz;
            while(aux != null){
                nodo.raizPadre = aux;
                if(nodo.dato >= aux.dato){
                    aux = aux.der;
                }else{
                    aux = aux.izq;
                }
            }
            if(nodo.dato < nodo.raizPadre.dato){
                nodo.raizPadre.izq = nodo;
            }else{
                nodo.raizPadre.der = nodo;
            }
        }

    }

    public void Mostrar_Arbol(Nodo nodo_raiz, int cont){
        if(nodo_raiz == null){
            return;
        }else{
            Mostrar_Arbol(nodo_raiz.der, cont+1);
            for(int i = 0; i < cont; i++){
                System.out.print("   ");
            }
            System.out.println(nodo_raiz.dato);
            Mostrar_Arbol(nodo_raiz.izq, cont+1);
        }
    }

    private class Nodo{
        public Nodo raizPadre;
        public int dato;
        public Nodo der;
        public Nodo izq;

        public Nodo(int indice){
            dato = indice;
            der = null;
            izq = null;
            raizPadre = null;
        }
    }

    public static void main(String[] args){
        Arbol_Binario Arbol = new Arbol_Binario();

        Arbol.insertar_Valor(3);
        Arbol.insertar_Valor(8);
        Arbol.insertar_Valor(4);
        Arbol.insertar_Valor(5);
        Arbol.insertar_Valor(1);
        Arbol.insertar_Valor(10);
        Arbol.insertar_Valor(20);
        Arbol.insertar_Valor(30);
        Arbol.insertar_Valor(40);
    
        Arbol.Mostrar_Arbol(Arbol.Raiz,0);
    }
}
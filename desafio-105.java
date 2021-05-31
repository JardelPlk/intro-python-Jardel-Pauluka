/*#DESAFIO!!!
#1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
#2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para #percorrer a lista ateh encontrar o primeiro multiplo de 5.
#OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.*/

import java.util.ArrayList;

public class Main {
	
    public static ArrayList<Integer> criarLista() {
        ArrayList<Integer> listaPares = criarLista(0, new ArrayList<Integer>());
        return listaPares;
    }

    public static ArrayList<Integer> criarLista(int valor, ArrayList<Integer> listaPares) {
        if (listaPares.size() < 1000) {
            listaPares.add(valor);
            listaPares = criarLista(valor + 2, listaPares);
        } else {
            return listaPares;
        }

        return listaPares;
    }

	public static void main(String[] args) {

		ArrayList<Integer> listaPares = criarLista();

        System.out.println("Tamanho da lista de números pares: " + listaPares.size());

        listaPares = new ArrayList<Integer>();
        for (int indice = 0; indice < 99999999; indice++) {
            listaPares.add(indice);
        }

        for (int numero : listaPares) {
            if (numero % 5 == 0 && numero != 0 && numero != 5) {
                System.out.println("Primeiro valor que é divisivel por 5 encontrado foi o " + numero);
                break;
            }
        }
	}

}
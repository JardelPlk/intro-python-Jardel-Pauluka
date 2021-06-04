/*#DESAFIO!!!
#1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
#2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999. Depois crie um loop para #percorrer a lista ateh encontrar o primeiro multiplo de 5.
#OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.*/

import java.util.ArrayList;

public class Main {

    public static ArrayList<Double> criarLista() {
        ArrayList<Double> listaPares = criarLista(0.0, new ArrayList<Double>());
        return listaPares;
    }

    public static ArrayList<Double> criarLista(Double valor, ArrayList<Double> listaPares) {
        if (listaPares.size() < 1000) {
            listaPares.add(valor);
            listaPares = criarLista(valor + 2, listaPares);
        } else {
            return listaPares;
        }

        return listaPares;
    }

	public static void main(String[] args) {

		ArrayList<Double> listaPares = criarLista();

        System.out.println("Tamanho da lista de números pares: " + listaPares.size());

        listaPares = new ArrayList<Double>();
        for (Double indice = 0.0; indice < 99999999999999999999999999.0; indice++) {
            listaPares.add(indice);
        }

        for (Double numero : listaPares) {
            if (numero % 5 == 0 && numero != 0 && numero != 5) {
                System.out.println("Primeiro valor que é divisivel por 5 encontrado foi o " + numero);
                break;
            }
        }
	}

}

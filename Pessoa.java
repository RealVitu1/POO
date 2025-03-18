public class Pessoa {
    private String nome;
    private int idade;
    private String origem;
    private String genero;
    private String cor;
    private String profissao;


public Pessoa(String nome, int idade, String origem, String genero, String cor, String profissao){
    this.nome = nome;
    this.idade = idade;
    this.origem = origem;
    this.genero = genero;
    this.cor = cor;
    this.profissao = profissao;

}

public String Apresentar(){
    return "Me chamo " +nome+ ", tenho " +idade+ "anos e sou " +profissao+".";

}

public static void main(String[] args) {
    Pessoa pessoa = new Pessoa("Victor", 21, "Brasil", "Masculino", "Pardo", "engenheiro");
    System.out.println(pessoa.Apresentar());
}
    
}

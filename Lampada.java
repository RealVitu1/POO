public class Lampada {
    // Atributos
    String marca;
    String tipo; 
    boolean isRunning;
    int brilho;
    
    // Método construtor
    public Lampada(String marca, String tipo, int brilho) {
        this.marca = marca;
        this.tipo = tipo;
        this.isRunning = false;
        this.brilho = brilho;
    }

    // Ligando a lâmpada
    public void ligar() {
        if (!isRunning) {
            isRunning = true;
            System.out.println("A lâmpada está ligada, brilho: " + brilho + " lúmens");
        } else {
            System.out.println("A lâmpada já está ligada.");
        }
    }

    // Desligando a lâmpada
    public void desligar() {
        if (isRunning) {
            isRunning = false;
            System.out.println("A lâmpada está desligada.");
        } else {
            System.out.println("A lâmpada já está desligada.");
        }
    }

    // Ajustando o brilho
    public void ajustarBrilho(int novoBrilho) {
        if (isRunning) {
            this.brilho = novoBrilho;
            System.out.println("O brilho da lâmpada foi ajustado para " + brilho + " lúmens");
        } else {
            System.out.println("A lâmpada está desligada, precisa ligar primeiro.");
        }
    }

    public static void main(String[] args) {
        Lampada lampada = new Lampada("Philips", "LED", 800);
        System.out.println("A lâmpada foi criada: " + lampada.tipo);

        lampada.ajustarBrilho(600); 
        lampada.ligar();            
        lampada.ajustarBrilho(600); 
        lampada.ajustarBrilho(1000); 
        lampada.desligar();         
        lampada.ajustarBrilho(500); 
    }
}
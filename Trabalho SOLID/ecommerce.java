

public class Produto {
    Big Preco;
    String tamanho;
    String cor;
    int quantidade;
    String marca;
};


public class Sapato extends Produto {
    public getAlgumaCoisa(){
        // Método não faz nada
    };
};

public class BlusaDeMoletom implements Blusa {

};

public class BlusaDoisLados implements Blusa {

};


// Dependency Inversion Principle

public class Conexao {

    DriverDBInterface dbDriver;

    String stringConexao = "Conn";

    public Conexao(dbDriver) {
        this.dbDriver = dbDriver;
    };

};
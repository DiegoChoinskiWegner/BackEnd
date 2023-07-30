package Livraria.src.entidades.constante;

public enum QtdMaterias {
    
    DUAS(02),
    CINCO(05),
    DEZ(10),
    VINTE(20);

    private double fator;

    QtdMaterias(double fator){
        this.fator = fator / 100;
    }

    public double getFator(){
        return fator;
    }
}

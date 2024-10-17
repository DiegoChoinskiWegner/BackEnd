class Calculator {
    constructor(victory, lose, balance, rank) { 
        this.victory = victory;
        this.lose = lose;
        this.balance = balance;
        this.rank = rank;
    
    }

    rankUp(balance) {
        if (balance <= 10){
            return this.rank = "Ferro";
        } else if (balance >10 && balance <= 20){
            return this.rank = "Bronze";
        }else if (balance > 20 && balance <= 50){
            return this.rank = "Prata";
        }else if (balance > 50 && balance <= 80){
            return this.rank = "Ouro";
        }else if (balance > 80 && balance <= 90){
            return this.rank = "Diamante";
        }else if (balance > 90 && balance <= 100){
            return this.rank = "Lendário";
        }else if (balance > 100){
            return this.rank = "Imortal";
        }
    }
}

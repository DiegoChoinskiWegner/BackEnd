//create a interface named heroTypes

class Warrior{
    constructor(){
        this.strengh = 10;
        this.inteligence = 3;
        this.agility = 4;
        this.defense = 9; 
    }
}

class Mage{
    constructor(){
        this.strengh = 8;
        this.inteligence = 10;
        this.agility = 5;
        this.defense = 3; 
    }
}

class Archer{
    constructor(){
        this.strengh = 8;
        this.inteligence = 7;
        this.agility = 9;
        this.defense = 2; 
    }
}

export { Warrior, Mage , Archer};

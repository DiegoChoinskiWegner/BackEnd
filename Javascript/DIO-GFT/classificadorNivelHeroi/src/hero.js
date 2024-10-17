//import { Warrior, Mage, Archer } from "./heroTypes"; // Assuming heroTypes defines Warrior, Mage, Archer classes

class Warrior{
  constructor(){
      this.strength = 10;
      this.intelligence = 3;
      this.agility = 4;
      this.defense = 9; 
  }

  //cria os getters
  getStrength(){
      return this.strength;
  }

  getIntelligence(){
      return this.intelligence;
  }

  getAgility(){
      return this.agility;
  }

  getDefense(){
      return this.defense;
  }

}

class Mage{
  constructor(){
      this.strength = 8;
      this.intelligence = 10;
      this.agility = 5;
      this.defense = 3; 
  }

      //cria os getters
  getStrength(){
      return this.strength;
  }

  getIntelligence(){
      return this.intelligence;
  }

  getAgility(){
      return this.agility;
  }

  getDefense(){
      return this.defense;
  }

}

class Archer{
  constructor(){
      this.strength = 8;
      this.intelligence = 7;
      this.agility = 9;
      this.defense = 2; 
  }

      //cria os getters
  getStrength(){
      return this.strength;
  }

  getIntelligence(){
      return this.intelligence;
  }

  getAgility(){
      return this.agility;
  }

  getDefense(){
      return this.defense;
  }

}

class Hero {
    constructor(name, level, rank, experience, heroClass) { 
        this.name = name;
        this.level = level;
        this.rank = rank;
        this.experience = experience;
    
        // Check if heroClass is a valid type (Warrior, Mage, Archer)
        if (!(heroClass instanceof Warrior || heroClass instanceof Mage || heroClass instanceof Archer)) {
          throw new Error("Invalid hero class provided!");
        }
    
        // Directly assign stats from the heroClass object
        this.strength = heroClass.strength;
        this.intelligence = heroClass.intelligence;
        this.agility = heroClass.agility;
        this.defense = heroClass.defense;
        this.heroClass = heroClass; // Store the entire heroClass object for potential future use
    }

    // Método para calcular a experiência necessária para o próximo nível
    experienciaNecessaria() {
        while (this.level <= 10){
            return this.level * 100;
        }
        while (this.level > 10 && this.level <= 25){
            return this.level * 115;
        }
        while (this.level > 25 && this.level <= 50){
            return this.level * 130;
        }
        while (this.level > 50){
            return this.level * 150;
        }
    }

    ganharExperiencia(exp) {
        this.experiencia += exp;
        while (this.experiencia >= this.experienciaNecessaria()) {
            this.experiencia -= this.experienciaNecessaria();
            this.levelUp();
        }
        this.salvar(); // Atualiza o herói no sessionStorage
    }

    levelUp() {
        this.level++;
        console.log(`${this.nome} subiu para o nível ${this.level}!`);
    }

    rankUp(level) {
        if (level >= 4){
            this.rank = "Ferro";
        } else if (level >= 9){
            this.rank = "Bronze";
        }else if (level >= 15){
            this.rank = "Prata";
        }else if (level >= 22){
            this.rank = "Ouro";
        }else if (level >= 30){
            this.rank = "Diamante";
        }else if (level >= 40){
            this.rank = "Esmeralda";
        }else if (level >= 50){
            this.rank = "Imortal";
        }
    }

    saveHero() {
        sessionStorage.setItem('hero', JSON.stringify(this));
    }

    // Método para carregar o herói do sessionStorage
    static carregar() {
        const dados = sessionStorage.getItem('hero');
        if (dados) {
            const { nome, level, experiencia } = JSON.parse(dados);
            //return new Heroi(nome, level, experiencia);
        }
        return null;
    }

    showHero() {
        console.log(`Hero name: ${this.name}, Level: ${this.level}`);
        console.log(`Type: ${this.heroClass.constructor.name}`); // Use constructor.name for class name
        console.log(`Strength: ${this.strength}`);
        console.log(`Intelligence: ${this.intelligence}`);
        console.log(`Agility: ${this.agility}`);
        console.log(`Defense: ${this.defense}`);
        console.log(`Experience: ${this.experience}`);
    }
}

export default Hero;
export { Warrior, Mage, Archer };
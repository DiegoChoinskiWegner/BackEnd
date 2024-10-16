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
  constructor(name, level, heroClass) { 
    this.name = name;
    this.level = level;

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

  showHero() {
    console.log(`Hero name: ${this.name}, Level: ${this.level}`);
    console.log(`Type: ${this.heroClass.constructor.name}`); // Use constructor.name for class name
    console.log(`Strength: ${this.strength}`);
    console.log(`Intelligence: ${this.intelligence}`);
    console.log(`Agility: ${this.agility}`);
    console.log(`Defense: ${this.defense}`);
  }
}

export default Hero;
export { Warrior, Mage, Archer };
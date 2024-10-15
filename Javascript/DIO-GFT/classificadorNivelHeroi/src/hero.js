import heroTypes from "./heroTypes";

class Hero{
    //create a constructor
    constructor(name, level, heroTypes){
        this.name = name;
        this.type = heroTypes;
        this.level = level;

        // Get stats based on hero type
        const stats = getHeroStats(heroType);
        this.strength = stats.strength;
        this.intelligence = stats.intelligence;
        this.agility = stats.agility;
        this.defense = stats.defense;
    }

    // Create a method to show the hero's information
    showHero() {
        console.log(`Hero name: ${this.name}, Level: ${this.level}`);
        console.log(`Type: ${this.type}`);
        console.log(`Strength: ${this.strength}`);
        console.log(`Intelligence: ${this.intelligence}`);
        console.log(`Agility: ${this.agility}`);
        console.log(`Defense: ${this.defense}`);
    }
}

//export the class Hero
export default Hero;


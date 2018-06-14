

function random_number(min, max) {
    return min + Math.random()*(max-min)
}


class Entity {
    constructor(){
        this.health = 100
        this.defense = 0.8
        this.attack = 1.2
        this.mana = 10
        this.energy = 10
        this.regen = 1 // amount of energy and mana given per turn

        // this.guard = 0

        this.moves = [{
            name: 'punch',
            damage: [5, 9],
        },{
            name: 'slap',
            damage: [3, 7],
        },{
            name: 'heal',
            heal: [7, 11],
        },{
            name: 'guard',
            plusDefense: [0.1, 0.2]
        }]

    }
    // health - ((defense-guard)*attack) if guard is used turn prior

    calculate_attack(move) {
        return random_number(move.damage[0], move.damage[1])*this.attack
    }
    // takes no energy or mana

    calculate_guard(move){
        return this.defense - random_number(move.plusDefense[0], move.plusDefense[1])
    }
    calculate_heal(move){
        return this.health + random_number(move.heal[0], move.heal[1] )}
}
//     takeTurn() {
//             this.monsterAttacks()
//             this.checkWin()
// }

// class Player extends Entity {
//     constructor (){
//         super();
//     }
//
// }
// class Monster extends Entity {
//     constructor (){
//         super();
//     }
// }

new Vue({
    el: '#app',
    data: {
        player: new Entity(),
        monster: new Entity(),
        gameIsRunning: false,
        rounds: 0,
        turns: [],
    },
    methods: {
        startGame: function () {
            this.gameIsRunning = true;
            //this.player.health = 100;
            // this.monster.health = 100;
            this.player.health = 100;
            this.monster.heatlh = 100 + (this.rounds * 0.10)

        },
        // used
        attack: function () {
            var damage = this.calculateDamage(3, 10)
            this.monster.health -= damage;
            this.turns.unshift({
                isPlayer: true,
                text: 'Player hits Monster for ' + damage
            });
            this.takeTurn()
        },

        //dont think i need this any more
        specialAttack: function () {
            var damage = this.calculateDamage(10, 20);
            this.monster.health -= damage
            this.turns.unshift({
                isPlayer: true,
                text: 'Player hits Monster savagely for ' + damage
            });
            this.takeTurn()
        },
        //used above

        heal: function () {
            if (this.player.Health <= 90) {
                this.player.Health += 10;
            } else {
                this.player.health = 100;
            }
            // this.player.health += 10;
            this.turns.unshift({
                isPlayer: true,
                text: 'Player heals for 10'
            });
            this.takeTurn()
        },
         // not going to use giving up is for cowards
        giveUp: function () {
            this.gameIsRunning = false;
        },

        monsterAttacks: function () {
            var damage = this.calculateDamage(5, 12)
            this.player.health -= damage;
            this.turns.unshift({
                isPlayer: false,
                text: 'Monster hits player for ' + damage
            });
        },

        takeTurn: function() {
            this.monsterAttacks()
            this.checkWin()
        },

        calculateDamage: function (min, max) {
            return min + Math.random()*(max-min)
            //return Math.max(Math.floor(Math.random() * max) + 1, min);
        },

        checkWin: function () {
            if (this.monster.health <= 0) {
                if (confirm('You won! New Game?')) {
                    this.rounds += 1
                    this.startGame();
                } else {
                    this.gameIsRunning = false;
                }
                return true;
            } else if (this.player.health <= 0) {
                if (confirm('You Lost! New Game?')) {
                    this.startGame();
                } else {
                    this.gameIsRunning = false;
                }
                return true;
            }
            return false;
        }
    }
});
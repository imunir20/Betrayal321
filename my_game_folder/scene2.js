
class Scene2 extends Phaser.Scene{
	constructor(){
		super("playGame");
	}

	init(){

	}

	preload(){
		this.load.image('createGame', 'assets/createGame.png');
		this.load.image('joinGame', 'assets/joinGame.png');
	}

	create() {
		this.add.text(20, 20, "Playing game", {font: "25px Arial", fill: "yellow"});	
		this.add.image(400,100, 'createGame');
		this.add.image(400,300, 'joinGame');
	}
}
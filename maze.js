var playerX = 1;
var playerY = 1;
var bulletX = -20;
var bulletY = 300;
var speed = 5;

// function intersect(s1_x, s1_y, s2_x, s2_y) {
//   	r = 40  
//   	if ((s1_x > s2_x - r) && (s1_x < s2_x + r) && (s1_y > s2_y - r) && (s1_y < s2_y + r)) {
//     	return 1
//     }
//   	else{
//     	return 0
//   	}
// }


function setup() {
	createCanvas(600,600);
}
function draw(){
	background(0);

	//Player
	fill(255, 255, 255)
	rect(playerX, playerY, 50, 50);

	//MOVEMENT
	if (keyIsDown(87)) {
		playerY = playerY - 3;
	}
	if (keyIsDown(83)) {
		playerY = playerY + 3;
	}
	if(keyIsDown(65)) {
		playerX = playerX - 3;
	}
	if(keyIsDown(68)) {
		playerX = playerX + 3;
	}
	
	//Creates walls
	if (playerX <= 0) {
		playerX = 0;
	}
	if (playerX >=550) {
		playerX = 550;
	}
	if (playerY <= 0) {
		playerY = 0;
	}
	if (playerY >= 550) {
		playerY = 550;
	}
	
	//Finish line/box
	fill(0, 255, 0);
	rect(518, 518, 80, 80);

	//Bullet
	fill(255, 0, 0);
	ellipse(bulletX, bulletY, 20, 20);
	bulletX = bulletX + speed
	//Bullet bounces back and forth
	if (bulletX >= 600){
		speed = -5
	}
	if (bulletX <= 0){
		speed = 5
	}
	//Hit Collision 
	
	// if intersect(bulletX, bulletY, playerX playerY){
	// 	alert("yay")
	// }



}


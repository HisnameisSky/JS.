function setup(){
  createCanvas(400,400);
  background(30);
}

function draw(){
  fill(mouseX % 255, mouseY % 255, 200, 150);
  noStroke();
  circle(mouseX, mouseY);
}

//
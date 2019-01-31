// Soojin Choi
// SoftDev2 pd08
// K00 -- I See a Red Door...
// 2019-01-30

var c = document.getElementById('slate');
//console.log(c);
var ctx = c.getContext("2d");

var clearCanvas = function(){
  //var c = document.getElementById('slate');
  //console.log(c);
  //var ctx = c.getContext("2d");
  ctx.clearRect(0,0,600,600);
};

var drawRect = function(e){

  // console.log(e);
  var corX = e.offsetX - 25;
  var corY = e.offsetY - 25;

  ctx.fillRect(corX, corY, 50, 50);

};

var drawCircle = function(e){

  //console.log(e);
  var corX = e["layerX"] + 25;
  var corY = e["layerY"] + 25;

  ctx.beginPath()
  ctx.ellipse(corX, corY, 25, 25, Math.PI / 4, 0, Math.PI);
  ctx.stroke();

};

var draw = function(e){

  var type = document.getElementById('type');
  if (type.innerHTML == " squares! "){
    drawRect(e);
  }
  else{
    drawCircle(e);
  }

};

var toggle = function(){

  var type = document.getElementById('type');
  console.log(type.innerHTML)
  if (type.innerHTML == " squares! "){
    type.innerHTML = " dots! ";
    //curr = drawCircle;
  }
  else{
    type.innerHTML = " squares! ";
    //curr = drawRect;
  }
};

var button = document.getElementById("clear");
button.addEventListener('click', clearCanvas);

var tbutton = document.getElementById("toggle");
tbutton.addEventListener('click', toggle);

c.addEventListener('click', draw);

//Team Dango Vincent Chi, Soojin Choi
//SoftDev2 pd7
//K #04 -- What is it saving the screen from?
//2019-02-07 (Due)

var requestID ;
var c = document.getElementById('playground');
var ctx = c.getContext('2d');
var dvdButton = document.getElementById("dvd");
var clear = function (e) {
    console.log("clearing");
    ctx.clearRect(0, 0, c.width, c.height);
};

var dvdLogoSetup = function() {

    window.cancelAnimationFrame(requestID);
    var rectWidth = 100;
    var rectHeight = 50;

    var rectX = Math.floor(Math.random() * (c.width-rectWidth));
    var rectY = Math.floor(Math.random() * (c.height-rectHeight));

    var xvel = 1;
    var yvel = 1;

    //var logo = new Image();
    //logo src = "logo_dvd.jpg"
	//ctx.drawImage(?);
	ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
	
	var dvdLogo = function() {

		clear();
		
	    if (rectX + rectWidth == c.width ){
			xvel = xvel * -1;
	    }
	    if (rectX == 0){
			xvel = xvel * -1;
	    }
	    if (rectY + rectHeight == c.height ){
			yvel = yvel * -1;
	    }
	    if (rectY == 0){
			yvel = yvel * -1;
	    }
		
		rectX += xvel;
		rectY += yvel;
	    
		ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
		
		requestID = window.requestAnimationFrame(dvdLogo);
	}
	dvdLogo()

}
dvdButton.addEventListener('click', dvdLogoSetup);
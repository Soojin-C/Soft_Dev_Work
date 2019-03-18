# Soft_Dev_Work

#### 00_canvas
* Creates rectangles and circles (broken atm... 01_canvas has better fxnality)
* Toggle button to switch between shapes
* Clear function
* = = = = = = = = = = = = = = = = = = = = = = 
* fillRect(x, y, w, l)
* fillStyle(color)
* beginPath()
* stroke()
* strokeStyle()
* clearRect()
* fillText()
* ellipse()

#### 01_canvas
00_canvas + 
* Improved draw fxn
* = = = = = = = = = = = = = = = = = = = = = = 
* e.preventDefault()
* ctx.beginPath()
* e.offsetX()
* e.offsetY()

#### 02_canvas
01_canvas + 
* Connects the dots created with a line
* = = = = = = = = = = = = = = = = = = = = = = 
* ctx.moveTo(x, y);
* ctx.lineTo(X, Y);

#### 03_canvas-anim
* Animates a growing/shrinking dot in a canvas
* Animation starts when the button is pressed
* Animation stops when the stop button is pressed
* = = = = = = = = = = = = = = = = = = = = = = 
* window.requestAnimationFrame(callback);
* window.cancelAnimationFrame(id);

#### 04_canvas-anim
03_canvas-anim + 
* Animates a dvd logo that bounces on the side walls
* = = = = = = = = = = = = = = = = = = = = = = 
* ctx.arc(c.width / 2, c.height / 2, radius, 0, 2 *Math.PI);
* var logo = new Image()
* logo.src = "<image path>"

#### 06_mongo
* Connecting to an already existing mongo db and getting information.
* = = = = = = = = = = = = = = = = = = = = = = 
* connection = pymongo.MongoClient(SERVER_ADDR)
* db = connection.<db name>
* collection = db.<collection name>
* collection.find({"key" : <target>})
* {"$and" : [{<This>} , {<That>}]}

#### 07_canvas-anim
* 
* = = = = = = = = = = = = = = = = = = = = = = 
* 
#### 08_canvas-anim
* 
* = = = = = = = = = = = = = = = = = = = = = = 
* 

#### 09_canvas-anim
* 
* = = = = = = = = = = = = = = = = = = = = = = 
* 

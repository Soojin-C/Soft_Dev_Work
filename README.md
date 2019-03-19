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
* Using pymongo
* = = = = = = = = = = = = = = = = = = = = = = 
* connection = pymongo.MongoClient(SERVER_ADDR)
* db = connection.<db name>
* collection = db.<collection name>
* collection.find({"key" : <target>})
* {"$and" : [{<This>} , {<That>}]}

#### 07_mongo
* Taking json data and placing it into a db created through python
* = = = = = = = = = = = = = = = = = = = = = = 
* collection.insert(json.load(<json>))

#### 08_mongosite
* A flask app frontend to take in an ip and use data 

#### 09_svg
* Connect the dots with an svg instead
* Clearing functionality
* = = = = = = = = = = = = = = = = = = = = = = 
* var circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
* circle.setAttribute({'fill','cx','cy','r'}, <val>)
* var connect = document.createElementNS('http://www.w3.org/2000/svg', 'line');
* connect.setAttribute({'x1', 'x2', 'y1', 'y2', 'stroke'}, val)
* e.offsetX, e.offsetY --> Works;
* pic.appendChild(circle);
* pic.removeChild()
* pic.firstChild
  
#### 10_svg
* First Click, creates a circle
* Second Click and purple --> colorChange
* Second Click and yellow --> moved to a random location, turned purple
* = = = = = = = = = = = = = = = = = = = = = = 
* e.stopPropagation();
* e.target;
* <item>.getAttribute("name")
  
#### 11_svg
* Kind of not working 24/7
* move -> Animates all the circles to moving a constant velocity.
* clear -> clears
* ? -> left half color changes
* Create any attribute for an svg child(ex: xvel, yvel)
* = = = = = = = = = = = = = = = = = = = = = = 
* current = pic.firstElementChild
* current.nextSibling

#### 12_svg
* 00 -> basic html with hardcoded div elements
* 01 -> basic html with d3 to use js to create the same effect as 00 without hardcoding it

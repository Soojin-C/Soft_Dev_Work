var selection = d3.select("body");

//Grouping Elements
d3.selectAll("h2");

d3.selectAll("tr").selectAll("td");
d3.selectAll("tr").selectAll("td").selectAll("span");

//Non-Grouping Elements
d3.selectAll("section");
d3.selectAll("section").append("p");

//<== Parentnode is still document

//Null Elements
//...are ignored
d3.selectAll("section").select("aside");

//Bound to Data
//stored in the DOM rather than the selection
//assigned to the __data__ property
// -- gets data by
// joined groups - selection.data
// individ elements - selection.datum
// inherited by parent

//document.body.__data__ = 42;
//d3.select("body").datum(42);
d3.select("body").datum(42).append("h1");

//Data
//represented as a function of parent data
var numbers = [4, 5, 18, 23, 42];
var letters = [
  {name: "A", frequency: .08167},
  {name: "B", frequency: .01492},
  {name: "C", frequency: .02780},
  {name: "D", frequency: .04253},
  {name: "E", frequency: .12702}
];
var matrix = [
  [ 0,  1,  2,  3],
  [ 4,  5,  6,  7],
  [ 8,  9, 10, 11],
  [12, 13, 14, 15]
];

//Key to Enlightment
//assign keys to both the datum and element.
//if they match, the datum gets assigned to the element

d3.selectAll("div").data(numbers);

function name(d) {
  return d.name;
}
d3.selectAll("div").data(letters, name);

//Enter, Update and Exit
// update - a match
// enter  - no match of element for datum
// exit   - no match for datum for a given element

//var div = d3.selectAll("div").data(vowels, name);

//div.exit();
//div.enter();

var scatter_data = [[0.3,1302],[0.3,1510],[0.31,1641],[0.31,1555],[0.32,1468],[0.32,1202]]
//Data about the weight and price of diamonds
//https://www2.stetson.edu/~jrasp/data.htm

//d3.tsv("data.tsv", type, function(error, data) {
//  x.domain([0, d3.max(data, function(d) { return d.value; })]);

var svg = d3.select("body")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);
var space = 0;
var dots = svg.selectAll("dots")
              .data(scatter_data)
              .enter()
              .append("circle")
              .attr("cx", function(d) {
                return 30 + ((d[0] - 0.3) * 9000 )
              })
              .attr("cy", function(d){
                return 500 - ((d[1] -1290))
              })
              .attr("r", 5)
              .attr("fill", "black");

var label = svg.selectAll("label")
              .data(scatter_data)
              .enter()
              .append("text")
              .attr("x", function(d) {
                return 30 + ((d[0] - 0.3) * 9000 )
              })
              .attr("y", function(d){
                return 500 - ((d[1] -1290)) - 10
              })
              .attr("fill", "blue")
              .text(function(d){
                return d[0] + " , " + d[1]
              });

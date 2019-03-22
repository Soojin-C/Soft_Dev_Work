var scatter_data = [[0,0],[2,3],[4,5],[6,7],[7,8]]
//d3.tsv("data.tsv", type, function(error, data) {
//  x.domain([0, d3.max(data, function(d) { return d.value; })]);

var svg = d3.select("body")
            .append("svg")
            .attr("width", 500)
            .attr("height", 500);

var dots = svg.selectAll("dots")
              .data(scatter_data)
              .enter()
              .append("circle")
              .attr("cx", function(d) {
                return (d[0] * 50) + 5
              })
              .attr("cy", function(d){
                return (500 - (d[1] * 50)) - 5
              })
              .attr("r", 5)
              .attr("fill", "black");

var label = svg.selectAll("label")
              .data(scatter_data)
              .enter()
              .append("text")
              .attr("x", function(d) {
                return (d[0] * 50) + 1
              })
              .attr("y", function(d){
                return (500 - (d[1] * 50)) - 11
              })
              .attr("fill", "blue")
              .text(function(d){
                return d[0] + " , " + d[1]
              });

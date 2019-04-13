// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 500;

// Define the chart's margins as an object
var margin = {
  top: 60,
  right: 60,
  bottom: 100,
  left: 100
};


// Define dimensions of the chart area
var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

// Select body, append SVG area to it, and set its dimensions
var svg = d3.select("scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append a group area, then set its margins
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

d3.csv("/assets/data/data.csv").then(function(data) {

    console.log(data);

    poverty = [];
    healthcare = [];
    abbr = [];
    age = [];

    Object.entries(data).forEach(
        ([i, x]) => {
        poverty.push(+x.poverty);
        healthcare.push(+x.healthcare);
        abbr.push(x.abbr);
        age.push(+x.age);
    });

    age.pop();
    poverty.pop();
    healthcare.pop();
    abbr.pop();

    console.log(abbr);

    var xLinearScale = d3.scaleLinear()
        .domain(d3.extent(poverty))
        .range([0, chartWidth]);

    var yLinearScale = d3.scaleLinear()
        .domain(d3.extent(healthcare))
        .range([chartHeight, 0]);


    var svg = d3.select("#scatter")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

    var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);


    var bottomAxis = chartGroup.append("g")
    .attr("id", "bottomAxis")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(d3.axisBottom(xLinearScale));

    var leftAxis = chartGroup.append("g")
    .attr("id", "leftAxis")
    .call(d3.axisLeft(yLinearScale));


    var circlesGroup = chartGroup.selectAll("circle")
    .data(poverty)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d))
    .attr("cy", (d, i) => yLinearScale(healthcare[i]))
    .attr("r", svgHeight/50)
    .attr("fill", "steelBlue");

    console.log(circlesGroup._groups[0][0]);


    var textGroup = chartGroup.selectAll("text")
    .data(poverty)
    .enter()
    .append("text")
    .attr("x", d => xLinearScale(d) - svgHeight/60)
    .attr("y", (d, i) => yLinearScale(healthcare[i]) + svgHeight/100)
    .attr("font-family", "arial")
    .attr("font-weight", "bold")
    .attr("font-size", svgHeight/50 + "px")
    .attr("fill", "white")
    .text((d, i) => abbr[i]);

    console.log(textGroup);

    var povertyLabel = chartGroup.append("text")
                                .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + margin.top - 25})`)
                                .attr("text-anchor", "middle")
                                .attr("font-size", "16px")
                                .attr("fill", "black")
                                .attr("id", "povertylabel")
                                .text("Poverty");

    // var ageLabel = chartGroup.append("text")
    //                             .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + margin.top})`)
    //                             .attr("text-anchor", "middle")
    //                             .attr("font-size", "16px")
    //                             .attr("fill", "black")
    //                             .attr("id", "agelabel")
    //                             .text("Age");

    // var incomeLabel = chartGroup.append("text")
    //                             .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + margin.top + 25})`)
    //                             .attr("text-anchor", "middle")
    //                             .attr("font-size", "16px")
    //                             .attr("fill", "black")
    //                             .attr("id", "incomelabel")
    //                             .text("Income");

    var healthcareLabel = chartGroup.append("text")
                                .attr("transform", `rotate(-90) translate(${-chartHeight / 2}, -25)`)
                                .attr("text-anchor", "middle")
                                .attr("font-size", "16px")
                                .attr("fill", "black")
                                .attr("id", "healthcarelabel")
                                .text("Healthcare");

    // var smokesLabel = chartGroup.append("text")
    //                             .attr("transform", `rotate(-90) translate(${-chartHeight / 2}, -50)`)
    //                             .attr("text-anchor", "middle")
    //                             .attr("font-size", "16px")
    //                             .attr("fill", "black")
    //                             .attr("id", "smokeslabel")
    //                             .text("Smokes");

    // var obeseLabel = chartGroup.append("text")
    //                             .attr("transform", `rotate(-90) translate(${-chartHeight / 2}, -75)`)
    //                             .attr("text-anchor", "middle")
    //                             .attr("font-size", "16px")
    //                             .attr("fill", "black")
    //                             .attr("id", "obeselabel")
    //                             .text("Obese");


//     ageLabel.on("click", function() {

//         if (d3.select("#agelabel").attr("font-weight") == "bold"){
//             console.log("it's bold");
//             return;

//         }

//         d3.select("#agepoverty").attr("font-weight", "normal");
//         d3.select("#ageincome").attr("font-weight", "normal");
//         d3.select("#agelabel").attr("font-weight", "bold");

//         var xLinearScale = d3.scaleLinear()
//         .domain(d3.extent(age))
//         .range([0, chartWidth]);

//         d3.selectAll("circle")
//         .transition()
//         .attr("cx", (d, i) => xLinearScale(age[i]))

//         d3.selectAll("text")
//         .transition()
//         .attr("x", (d, i) => xLinearScale(age[i]))

//         delete bottomAxis;
//         delete leftAxis;

//         d3.select("#bottomAxis").remove();
//         d3.select("#leftAxis").remove();

//         var bottomAxis = chartGroup.append("g")
//         .attr("transform", `translate(0, ${chartHeight})`)
//         .call(d3.axisBottom(xLinearScale));
//       ``
//         var leftAxis = chartGroup.append("g")
//         .call(d3.axisLeft(yLinearScale));

//     });
});


// //   // Configure a line function which will plot the x and y coordinates using our scales
// //   var drawLine = d3.line()
// //     .x(data => xTimeScale(data.date))
// //     .y(data => yLinearScale(data.force));

// //   // Append an SVG path and plot its points using the line function
// //   chartGroup.append("path")
// //     // The drawLine function returns the instructions for creating the line for forceData
// //     .attr("d", drawLine(forceData))
// //     .classed("line", true);

// //   // Append an SVG group element to the chartGroup, create the left axis inside of it
// //   chartGroup.append("g")
// //     .classed("axis", true)
// //     .call(leftAxis);

// //   // Append an SVG group element to the chartGroup, create the bottom axis inside of it
// //   // Translate the bottom axis to the bottom of the page
// //   chartGroup.append("g")
// //     .classed("axis", true)
// //     .attr("transform", `translate(0, ${chartHeight})`)
// //     .call(bottomAxis);
// });

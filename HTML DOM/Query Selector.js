HTML DOM querySelector() Method: https://www.w3schools.com/jsref/met_document_queryselector.asp

// Query Selector
document.querySelector("#demo").innerHTML = "Hello World!" // Change the text of an element with id="demo"

document.querySelector("p") // Get the first tag <p> element in the document
document.querySelector("p.example") // Get the first <p> element in the document with class="example"
document.querySelector("div > p") // Get the first <p> element in the document where the parent is a <div> element
document.querySelector("a[target]") // Get the first <a> element in the document that has a "target" attribute


HTML DOM querySelectorAll() Method: https://www.w3schools.com/jsref/met_document_queryselectorall.asp
// Query Selector All
var x = document.querySelectorAll(".example"); // All elements in the document with class="example"
var x = document.querySelectorAll("a[target]"); // All <a> elements in the document that have a "target" attribute
var x = document.querySelectorAll("h2, div, span"); // All <h2>, <div> and <span> elements in the document


var x = document.querySelectorAll("p"); // Get all <p> elements in the document
x[0].style.backgroundColor = "red"; // Set the background color of the first <p> element


var x = document.querySelectorAll("p.example"); // Get all <p> elements in the document with class="example"
x[0].style.backgroundColor = "red"; // Set the background color of the first <p> element with class="example" (index 0)
// Name the var anything, then have it SELECT the html button ELEMENT.
// Now we have a convenient var that points to the element.

var btn = document.getElementById("btn")
// Now let's set up an event listener for when the button gets clicked.

// The EVENT that we're listing for is the "click" event...

// and what do we want to actually HAPPEN, when it gets clicked?
// Instead of calling a SPECIFIC function, let's just open an ANONYMOUS function here...

// and within the BODY of the anonymous function, we can just copy and paste our previously written AJAX call...


btn.addEventListener("click")



var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json')
ourRequest.onload = function() {
    var ourData = JSON.parse(ourRequest.responseText)
    console.log(ourData[0])
};
ourRequest.send();

// Let's add an event listener for the blue html button, so we will only run our AJAX call when the button is triggered.





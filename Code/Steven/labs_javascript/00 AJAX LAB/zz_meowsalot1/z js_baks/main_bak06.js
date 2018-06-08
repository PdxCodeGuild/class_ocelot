var animalContainer = document.getElementByID("animal-info");

var btn = document.getElementById("btn");

btn.addEventListener("click", function() {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json');

    // (This is our AJAX call)
    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData)
    };
    ourRequest.send();
});

// Let's create a function whose SOLE PURPOSE is to add html to the page.

// Withing the 'signature' for our custom HTML function (between the parens)...
// ... we can make a variable, & call it anything we like, let's call it 'data'...


function renderHTML(data) {
//    The job of this function is to add html to the page, more SPECIFICALLY, to add html to the empty div element 'id="animal-info".

//    So UP AT THE TOP OF THE PAGE, we create a variable ('animalContainer') that POINTS to the empty div...
//    ... and then down here, within our renderHTML function, we can TARGET that empty div by using the VARIABLE that we assigned up above ('animalContainer')...

//    ...then we can use a METHOD that's available to ALL DOM ELEMENTS, it's called "insertAdjacentHTML...

    animalContainer.insertAdjacentHTML('beforeend', 'testing 123')

}
// NOTE: returns error: TypeError: document.getElementByID is not a function[Learn More] on line 23. I'm going to bak & remove all comments...

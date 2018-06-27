// var pageCounter = 1;
var quoteContainer = document.getElementById("quote-info");
var btn = document.getElementById("btn");

// CLICK THE MOUSE TO SEND A DATA REQUEST
btn.addEventListener("click", function () {
    var ourRequest = new XMLHttpRequest();
    // ourRequest.open('GET', 'https://favqs.com/api/qotd');
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json');
    ourRequest.onload = function () {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData);
        console.log(ourData)
    };
    ourRequest.send();
    // pageCounter++;
    // if (pageCounter > 3) {
    //     btn.classList.add("hide-me");
    // }
});

// PUT CERTAIN PARTS OF RECEIVED JSON ON THE PAGE
function renderHTML(data) {
    console.log(data)
    var htmlString = "howdy";

    // htmlString += "<p>" + data.body

    // LOOP THROUGH MULTIPLE OBJECTS
    // for (i = 0; i < data.length; i++) {
    //     htmlString += "<p> I believe it was " + data[i].author + " is a " + data[i].species + " that likes to eat ";

    // // Loop through the foods he LIKES, and put them in the DOM
    //     for (ii = 0; ii < data[i].foods.likes.length; ii++) {
    //         if (ii == 0) {
    //             htmlString += data[i].foods.likes[ii];
    //         } else {
    //             htmlString += ' and ' + data[i].foods.likes[ii]
    //         }
    //     }
    //
    // // Loop through the foods he DISLIKES, and put them in the DOM
    //     htmlString += ' and dislikes ';
    //
    //     for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
    //         if (ii == 0) {
    //             htmlString += data[i].foods.dislikes[ii];
    //         } else {
    //             htmlString += ' and ' + data[i].foods.dislikes[ii]
    //         }
    //     }

    // htmlString += '.</p>';

}

    quoteContainer.insertAdjacentHTML('beforeend', htmlString);
}

// htmlString

// TODO: add "I believe it was " + author + "who said: " + quote




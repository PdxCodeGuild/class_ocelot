
// Name the variable anything.  Set the variable to equal a new instance of the XMLHttpRequest tool.
var ourRequest = new XMLHttpRequest();

// Now we tell our variable to actually do something.
// The web browser will expect our variable to use a METHOD named OPEN, so we want to specify that.  This is our chance to say what we want to do.

// We will want to pass this OPEN method TWO arguments.
// The first argument is whether we want to SEND data (POST) or (RECEIVE) data (GET).
// The second argument is simply the url that we want to talk to, where the JSON lives.
ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json')

// Next, we need to actually DO something WIH that data.
// Again, we START WITH OUR VARIABLE (ourRequest), and this time we want to use a METHOD called "onload".  This will tell the browser what do DO with the data when it is actually loaded.

// We're going to set this to equal an ANONYMOUS FUNCTION,
ourRequest.onload = function() {
    // ... and in the BODY of this function, we can do whatever we like.
    // As a quick example/test - let's log out the data that we just downloaded, by saying 'ourRequest dot responseText'

    console.log(ourRequest.responseText);
};

// The FINAL step is to actually SEND the request. 'ourRequest dot send'
ourRequest.send();




var ourRequest = new XMLHttpRequest();

ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-1.json')


// We're going to set this to equal an ANONYMOUS FUNCTION,
ourRequest.onload = function() {
    // the following is intentionally wrong, returning only a left bracket, the first character of our JSON data. This illustrates that the browser does not yet KNOW that this is JSON data, and treats it like a string, returning only the first CHAR in the string.

    // var ourData = ourRequest.responseText;

    // Instead of the above, we'll use a tool our browser has for JSON data, JSON.parse.
    var ourData = JSON.parse(ourRequest.responseText)
    console.log(ourData[0])

};

// The FINAL step is to actually SEND the request. 'ourRequest dot send'
ourRequest.send();

// Now let's do something actually USEFUL with our data - let's try saving it to a variable.





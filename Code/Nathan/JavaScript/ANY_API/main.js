//<script></script>


function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

let allCharacters =function () {
    http_get("https://rickandmortyapi.com/api/character", function (data) {
        data.results.forEach(function(character){
            document.body.innerHTML += character.name + " / " + character.species +" <br>"
        })
        // for (i=0; i < data.results.length; i++){

    })
}
allCharacters()
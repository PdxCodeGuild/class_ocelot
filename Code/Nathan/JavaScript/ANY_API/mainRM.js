//<script></script>

var characterContainer = document.getElementById("characters")
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
    let url = "https://rickandmortyapi.com/api/character"
    var htmlString = ""
    http_get(url, function (data) {
        console.log(data)
        data.results.forEach(function(character){
            // for (i=0; i < data.results.length; i++)
            let div = document.createElement('div')
            div.innerText = character.name + " / " + character.species + " / " + character.type
            characterContainer.appendChild(div)
        })

    })
}
allCharacters()


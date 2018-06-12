const quote_url = "https://favqs.com/api/qotd"


// Gets quote from API
function getQuote() {


    axios.get(quote_url)
        .then(function (response) {
            // console.log(response)
            const quote = response.data.quote.body
            const author = response.data.quote.author

            let printQuote = "<p>" + quote + "</p>"
            document.querySelector("#quote-info").innerHTML = printQuote
        })
        // .catch(function (error) {
        //     console.log(error)
        // })
}


function setBackground(url) {
    document.body.style.background = "url(" + url + ")"
}

document.querySelector("#btn").onclick = getQuote

const url = "https://favqs.com/api/qotd"

function getQuote() {
    axios.get(url)
        .then(function(response) {
            // console.log(response)
            const quote = response.data.quote.body
            const author = response.data.quote.author

            let printQuote = "<p> I believe it was " + author + " who said, <br> \"" + quote + "\"</p>"

            document.querySelector("#quote-info").innerHTML = printQuote

        })
        .catch(function(error) {
            console.log(error)
        })

}

document.querySelector("#btn").onclick = getQuote




// axios.post('//www.goggle.com', { haha: 'haha'})
// .then(function() {
//     console.log('AHHHHHHHHHH')
// })
// .catch((error) => {
//     console.log(error)
// })


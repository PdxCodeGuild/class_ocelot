// const api1_url = "https://gateway.watsonplatform.net/text-to-speech/api/v1/pronunciation?text=rock%20the%20bells&voice=en-US_MichaelVoice&format=ipa"
const api1_url = "https://gateway.watsonplatform.net/text-to-speech/api/v1/pronunciation?text=rock%20the%20bells&voice=en-US_MichaelVoice&format=ipa"


watsonLanguageApi = {
  "url": "https://gateway.watsonplatform.net/natural-language-understanding/api",
  "username": "aaed3e25-0432-40ba-8a22-bd2f7ab14a70",
  "password": "lpy7kLfkN4M3"
}


// Gets quote from API
function getQuote() {


    axios.get(api1_url)
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

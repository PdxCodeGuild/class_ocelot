const quote_url = "https://favqs.com/api/qotd"
const bkgd_img_url = "test_image.jpg"
let astros_in_space = []

// Gets quote from API
function getQuote() {

    let rnd_choice = Math.floor(Math.random() * astros_in_space.length);
    let quotingAstronaut = astros_in_space[rnd_choice]
    axios.get(quote_url)
        .then(function (response) {
            // console.log(response)
            const quote = response.data.quote.body
            const author = response.data.quote.author

            // let printQuote = "<p> I believe it was astronaut " + author + " who said, <br> \"" + quote + "\"</p>"
            let printQuote = "<p> I believe it was astronaut " + quotingAstronaut + " who said, <br> \"" + quote + "\"</p>"
            document.querySelector("#quote-info").innerHTML = printQuote
        })
        // .catch(function (error) {
        //     console.log(error)
        // })
}

// Gets astronauts currently in space
function getAstronauts() {
    axios.get("http://api.open-notify.org/astros.json")
        .then(function (response) {
            // console.log(response)
            // Loop through the astronauts to get names
            for (let i = 0; i < response.data.people.length; i++) {
                astros_in_space.push(response.data.people[i].name)
            }

            getQuote()

        });
        console.log(astros_in_space)
}



function getBackground() {
    axios.get("https://api.nasa.gov/planetary/apod?api_key=KPzjbTjgFMcSMl1duvZZtnROCaSfbHAGc2AwT6FY&date=2017-07-12")
        .then(function (response) {
            setBackground(response.data.url)
        });
}


function setBackground(url) {
    document.body.style.background = "url(" + url + ")"
}

document.querySelector("#btn").onclick = getQuote

getAstronauts()
getBackground()

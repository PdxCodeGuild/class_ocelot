const quote_url = "https://favqs.com/api/qotd"
const bkgd_img_url = "https://api.nasa.gov/planetary/apod?api_key=KPzjbTjgFMcSMl1duvZZtnROCaSfbHAGc2AwT6FY&date=2017-07-12"
const years_ago = 3  // Get random APOD from the past 'years_ago' years.

let


// const picStartDate = new Date().setFullYear() - 3


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
        // console.log(astros_in_space)
}

function getRandPicDate() {                     // Generate random date between years_ago and now
    var d = new Date();                         // Set d to current date
    d.setFullYear(d.getFullYear() - years_ago); // Change d to years_ago years before current date
    let randDaysAfterStartDate = Math.floor(Math.random() * 365 * years_ago);  // Rand num of days
    d.setDate(d.getDate() + randDaysAfterStartDate);  // add rand days to years_ago

    return d


    // console.log(randDaysAfterStartDate)


    // Math.floor(Math.random() * 365 * apod_years_ago);


    // function addDays(date, days) {
    //     let result = new Date(date);
    //     result.setDate(result.getDate() + days);
    //     return result;
    // }



    // const picStartYear =
    // const picStartDate = new Date();


    // picStartDate.setFullYear(picStartDate.getFullYear(picStartDate)

    // console.log(picStartDate)

    // let years_ago = Math.floor(Math.random() * 3;
    // let months_ago = Math.floor(Math.random() * 12;
    // let days_ago = Math.floor(Math.random() * 30;



}


function getBackground() {
    axios.get(bkgd_img_url)
        .then(function (response) {
            setBackground(response.data.url)
        });
}


function setBackground(url) {
    document.body.style.background = "url(" + url + ")"
}

document.querySelector("#btn").onclick = getQuote

getAstronauts()
console.log(getRandPicDate())
getBackground()


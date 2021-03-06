function clearEmailPwd() {

    axios.get("/clearEmailPwd");
}

function createEmailPwdDB() {

    axios.get("/dbEmailPwd");
}

function addEmailPWD() {

    axios.get('/emailPwd')
    .then(function (response) {
        console.log(response);
        document.getElementById("emailpwd").innerHTML = response.data.map((e) => {
            return `${e.pie}: ${e.item} ${e.status}`
        }).join("\n");

    })
    .catch(function (error) {
        console.log(error);
    })
    .then(function () {
        // always executed
    });
}

function createPeopleDatabase() {

    axios.get("/dbPeopleDetails");
}

function clearPeopleDB() {

    axios.get("/clearPeopleDB");
}

function getPeopleDBDetails() {

    axios.get('/peopleDetailsFromDatabase')
    .then(function (response) {
        console.log(response);
        document.getElementById("peopledb").innerHTML = response.data.map((v) => {
            return `Name: ${v.name} Email: ${v.email} Notes: ${v.notes}`
        }).join("\n");

    })
    .catch(function (error) {
        console.log(error);
    })
    .then(function () {
        // always executed
    });
}

function createMangementDB() {

    axios.get("/makeManagementTable");
}

function clearManagementDB() {

    axios.get("/clearManagementTable");
}

function retriveManagementTask() {


    axios.get("/getTasksFromDB")
    .then(function (response) {
        console.log(response);
        document.getElementById("management").innerHTML = response.data.map(e => {
            return `<li><input type="checkbox">${e.task}</li>`
        }).join("\n");

    })
    .catch(function (error) {
        console.log(error);
    })
    .then(function () {
        // always executed
    });
}

var today = new Date();
var day;

switch (today.getDay() + 1) {

    case 1:

        day = "Sunday";
        break;
    case 2:

        day = "Monday";
        break;
    case 3:

        day = "Tuesday";
        break;
    case 4:

        day = "Wednesday";
        break;
    case 5:

        day = "Thursday";
        break;
    case 6: 

        day = "Friday";
        break;
    case 7:

        day = "Saturday";
        break;
}

var date = `${day} ${today.getDate()}-${(today.getMonth()+1)}-${today.getFullYear()}`;
document.getElementById("datetimeh6").innerText = date;

// Declaring the variables
let lon;
let lat;
let temperature = document.querySelector(".temp");
let summary = document.querySelector(".summary");
let loc = document.querySelector(".location");
let icon = document.querySelector(".icon");
const kelvin = 273;

window.addEventListener("load", () => {
if (navigator.geolocation) {
	navigator.geolocation.getCurrentPosition((position) => {
	console.log(position);
	lon = position.coords.longitude;
	lat = position.coords.latitude;

	// API ID
	const api = "266e49f047db0bc298dd9b142e82415e";

	// API URL
	const base =
`http://api.openweathermap.org/data/2.5/weather?lat=${lat}&` +
`lon=${lon}&appid=6d055e39ee237af35ca066f35474e9df`;

	// Calling the API
	fetch(base)
		.then((response) => {
		return response.json();
		})
		.then((data) => {
		console.log(data);
		temperature.textContent =
			`The temperature is ${Math.floor(data.main.temp - kelvin)}??C and there is a ${data.weather[0].description}`;
		});
	});
}
});

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
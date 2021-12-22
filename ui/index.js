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
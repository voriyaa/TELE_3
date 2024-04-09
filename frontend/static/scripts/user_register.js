function userRegister(first_name, last_name, dob, passport_number, gender, username, password) {
    fetch('/register', {
        method: 'POST',
        body: JSON.stringify({
            first_name: first_name,
            last_name: last_name,
            dob: dob,
            passport_number: passport_number,
            gender: gender,
            username: username,
            password: password
        }),
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}
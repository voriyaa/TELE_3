function adminEditTariff(Tariff) {
    fetch('/login/create_tariff', {
        method: 'PUT',
        body: JSON.stringify({Tariff: Tariff})
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

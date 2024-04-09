function userBuyMin(amountMin) {
    fetch('/login/create_tariff', {
        method: 'PUT',
        body: JSON.stringify(amountMin)
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
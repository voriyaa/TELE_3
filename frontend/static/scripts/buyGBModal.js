document.addEventListener('DOMContentLoaded', function () {
    const buyGBModal = document.getElementById('buy-gb-modal');
    const buyGBButton = document.getElementById('buy-gb-button');
    const closeGBModalButton = document.getElementById('close-buy-gb-modal-button');

    buyGBButton.addEventListener('click', function () {
        buyGBModal.style.display = 'flex';
    });

    closeGBModalButton.addEventListener('click', function () {
        buyGBModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === buyGBModal) {
            buyGBModal.style.display = 'none';
        }
    });

    const buyGBForm = document.getElementById('buy-gb-form');

    buyGBForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const gbAmount = document.getElementById('gb-amount').value;

        console.log(gbAmount)
        //Todo поменять ссыль
        fetch('http://93.175.7.10:5000/url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
            body: JSON.stringify(gbAmount)
        }).then(response => {
            if (!response.ok) {
                throw new Error('Неправильно введено количество гигабайт');
            }
            return response.json();
        })
            .then(data => {
                console.log('Успешная покупка:', data);
                window.location.href = `/user/${gbAmount['username']}/dashboard?jwt=${data['access_token']}`;
            })
            .catch(error => {
                console.error('Ошибка:', error);
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
                alert(error.message); // Отображаем сообщение об ошибке пользователю
                window.location.href = `/user/${gbAmount['username']}/dashboard?jwt=${data['access_token']}`;
            });
    });

    buyGBModal.style.display = 'none';
})
;

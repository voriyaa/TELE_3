document.addEventListener('DOMContentLoaded', function () {
    const buyMinutesModal = document.getElementById('buy-minutes-modal');
    const buyMinutesButton = document.getElementById('buy-minutes-button');
    const closeMinutesModalButton = document.getElementById('close-buy-minutes-modal-button');

    buyMinutesButton.addEventListener('click', function () {
        buyMinutesModal.style.display = 'flex';
    });

    closeMinutesModalButton.addEventListener('click', function () {
        buyMinutesModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === buyMinutesModal) {
            buyMinutesModal.style.display = 'none';
        }
    });

    const buyMinutesForm = document.getElementById('buy-minutes-form');

    buyMinutesForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const minutesAmount = document.getElementById('minutes-amount').value;
        //Todo поменять ссыль
        fetch('http://93.175.7.10:5000/url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
            body: JSON.stringify(minutesAmount)
        }).then(response => {
            if (!response.ok) {
                throw new Error('Неправильно введено количество гигабайт');
            }
            return response.json();
        })
            .then(data => {
                console.log('Успешная покупка:', data);
                window.location.href = `/user/${minutesAmount['username']}/dashboard?jwt=${data['access_token']}`;
            })
            .catch(error => {
                console.error('Ошибка:', error);
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
                alert(error.message); // Отображаем сообщение об ошибке пользователю
                window.location.href = `/user/${minutesAmount['username']}/dashboard?jwt=${data['access_token']}`;
            });
    });
    buyMinutesModal.style.display = 'none';
})
;

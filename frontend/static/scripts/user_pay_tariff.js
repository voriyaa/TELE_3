document.addEventListener('DOMContentLoaded', function () {
    const payTariffButton = document.getElementById('pay-tariff-button');

    payTariffButton.addEventListener('click', function (event) {
        event.preventDefault(); // Предотвращаем переход по ссылке по умолчанию

        const path = window.location.pathname;
        const parts = path.split('/');
        const username = parts[2]; // Получаем имя пользователя из пути URL

        fetch(`http://93.175.7.10:5000/user/pay_tariff/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Недостаточно средств на балансе');
                }
                return response.json(); // Возвращаем JSON-данные в следующий then()
            })
            .then(data => {
                console.log('Тариф успешно оплачен:', data);
                alert('Тариф успешно оплачен');
            })
            .catch(error => {
                console.error('Ошибка оплаты тарифа:', error);
                alert('Произошла ошибка при оплате тарифа');
            });
    });
});

function goBack() {
    window.location.href = "/user/login";
}

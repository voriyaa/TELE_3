document.addEventListener('DOMContentLoaded', function() {
    // Получаем доступ к модальному окну "Пополнить баланс" и кнопке, открывающей его
    const rechargeBalanceModal = document.getElementById('recharge-balance-modal');
    const rechargeBalanceButton = document.getElementById('recharge-balance-button');
    const closeRechargeBalanceButton = document.getElementById('close-recharge-balance-button');

    // Открытие модального окна при клике на кнопку "Пополнить баланс"
    rechargeBalanceButton.addEventListener('click', function() {
        rechargeBalanceModal.style.display = 'flex';
    });

    // Закрытие модального окна при клике на кнопку "закрыть" или на область вне окна
    closeRechargeBalanceButton.addEventListener('click', function() {
        rechargeBalanceModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === rechargeBalanceModal) {
            rechargeBalanceModal.style.display = 'none';
        }
    });

    // Обработка отправки формы
    const rechargeBalanceForm = document.getElementById('recharge-balance-form');

    rechargeBalanceForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        const amount = document.getElementById('amount').value;

        // Выполнение дополнительных действий с суммой для пополнения баланса
        console.log('Amount to Recharge:', amount);

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
        // Скрыть модальное окно после отправки формы
        rechargeBalanceModal.style.display = 'none';
});

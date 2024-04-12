document.addEventListener('DOMContentLoaded', function () {
    const changeTariffModal = document.getElementById('change-tariff-modal');
    const changeTariffButton = document.getElementById('change-tariff-button');
    const closeChangeTariffModalButton = document.getElementById('close-change-tariff-modal-button');
    const confirmChangeTariffButton = document.getElementById('confirm-change-tariff-button');
    const inputTariffId = document.getElementById('tariff-id');

    changeTariffButton.addEventListener('click', function () {
        changeTariffModal.style.display = 'flex';
    });

    closeChangeTariffModalButton.addEventListener('click', function () {
        changeTariffModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === changeTariffModal) {
            changeTariffModal.style.display = 'none';
        }
    });

    confirmChangeTariffButton.addEventListener('click', function () {
        const newTariffId = inputTariffId.value;
        changeTariff(newTariffId);
    });

    function changeTariff(newTariffId) {
        const path = window.location.pathname;
        const parts = path.split('/');
        const username = parts[2];

        fetch(`http://93.175.7.10:5000/user/change_tariff/${username}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tariff_id: newTariffId })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Ошибка при смене тарифа');
                }
                return response.json();
            })
            .then(data => {
                console.log('Тариф успешно изменен:', data);
                alert('Тариф успешно изменен');
                changeTariffModal.style.display = 'none'; // Скрываем модальное окно после успешной смены тарифа
            })
            .catch(error => {
                console.error('Ошибка при смене тарифа:', error);
                alert('Произошла ошибка при смене тарифа');
            });
    }
});

function goBack() {
    window.location.href = "/user/login";
}

document.addEventListener('DOMContentLoaded', function () {
    // Получаем username из URL
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2] // Предполагается, что username находится во второй части пути

    // Получаем доступ к модальному окну "Поделиться ГБ" и кнопке, открывающей его
    const shareGBModal = document.getElementById('share-gb-modal');
    const shareGBButton = document.getElementById('share-gb-button');
    const closeGBModalButton = document.getElementById('close-gb-modal-button');

    // Открытие модального окна при клике на кнопку "Поделиться ГБ"
    shareGBButton.addEventListener('click', function () {
        shareGBModal.style.display = 'flex';
    });

    // Закрытие модального окна при клике на кнопку "закрыть" или на область вне окна
    closeGBModalButton.addEventListener('click', function () {
        shareGBModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === shareGBModal) {
            shareGBModal.style.display = 'none';
        }
    });

    // Обработка отправки формы
    const shareGBForm = document.getElementById('share-gb-form');

    shareGBForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        const phone_number = document.getElementById('phone_number').value;
        const value = document.getElementById('value').value;

        // Выполнение дополнительных действий с получателем и количеством GB
        fetch(`http://93.175.7.10:5000/user/share_gb/2`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
            body: JSON.stringify(
                {
                    phone_number,
                    value
                })
        }).then(response => {
            if (!response.ok) {
                throw new Error('Неправильно введено количество гигабайт');
            }
            return response.json();
        })
            .then(data => {
                console.log('Успешная покупка:', data);
                window.location.href = `/user/${username}/dashboard?jwt=${data['access_token']}`;
            })
            .catch(error => {
                console.error('Ошибка:', error);
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
                alert(error.message); // Отображаем сообщение об ошибке пользователю
                window.location.href = `/user/${username}/dashboard?jwt=${data['access_token']}`;
            });
    });
});

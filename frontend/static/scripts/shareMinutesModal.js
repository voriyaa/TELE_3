document.addEventListener('DOMContentLoaded', function () {
    // Получаем username из URL
    const path = window.location.pathname;
    const parts = path.split('/');
    const username = parts[2] // Предполагается, что username находится во второй части пути

    // Получаем доступ к модальному окну "Поделиться ГБ" и кнопке, открывающей его
    const shareMINModal = document.getElementById('share-minutes-modal');
    const shareMINButton = document.getElementById('share-minutes-button');
    const closeMINModalButton = document.getElementById('close-minutes-modal-button');

    // Открытие модального окна при клике на кнопку "Поделиться ГБ"
    shareMINButton.addEventListener('click', function () {
        shareMINModal.style.display = 'flex';
    });

    // Закрытие модального окна при клике на кнопку "закрыть" или на область вне окна
    closeMINModalButton.addEventListener('click', function () {
        shareMINModal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === shareMINModal) {
            shareMINModal.style.display = 'none';
        }
    });

    // Обработка отправки формы
    const shareMINForm = document.getElementById('share-minutes-form');

    shareMINForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        const phone_number = document.getElementById('phone_number_min').value;
        const value = document.getElementById('value_min').value;

        // Выполнение дополнительных действий с получателем и количеством GB
        fetch(`http://93.175.7.10:5000/user/share_minute/${username}`, {
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
                if (response.status === 409) {
                    throw new Error('Пользователя с таким номером телефона не существует');
                } else if (response.status === 410) {
                    throw new Error('Не хватает средств для перевода');
                }
            }
        })
            .then(data => {
                console.log('Успешный перевод:', data);
                shareMINModal.style.display = 'none';
                alert('Перевод успешно завершен!');
            })
            .catch(error => {
                console.error('Ошибка:', error);
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
                alert(error.message); // Отображаем сообщение об ошибке пользователю
            });
    });
});

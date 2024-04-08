document.addEventListener('DOMContentLoaded', function() {
    // Получаем доступ к модальному окну "Поделиться ГБ" и кнопке, открывающей его
    const shareGBModal = document.getElementById('share-gb-modal');
    const shareGBButton = document.getElementById('share-gb-button');
    const closeGBModalButton = document.getElementById('close-gb-modal-button');

    // Открытие модального окна при клике на кнопку "Поделиться ГБ"
    shareGBButton.addEventListener('click', function() {
        shareGBModal.style.display = 'flex';
    });

    // Закрытие модального окна при клике на кнопку "закрыть" или на область вне окна
    closeGBModalButton.addEventListener('click', function() {
        shareGBModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === shareGBModal) {
            shareGBModal.style.display = 'none';
        }
    });

    // Обработка отправки формы
    const shareGBForm = document.getElementById('share-gb-form');

    shareGBForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        const recipient = document.getElementById('recipient').value;
        const gbToSend = document.getElementById('gb-to-share').value;

        // Выполнение дополнительных действий с получателем и количеством GB
        console.log('Recipient:', recipient);
        console.log('GB to Share:', gbToSend);

        // Скрыть модальное окно после отправки формы
        shareGBModal.style.display = 'none';
    });
});

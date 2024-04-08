document.addEventListener('DOMContentLoaded', function() {
    // Получаем доступ к модальному окну "Поделиться минутами" и кнопке, открывающей его
    const shareMinutesModal = document.getElementById('share-minutes-modal');
    const shareMinutesButton = document.getElementById('share-minutes-button');
    const closeMinutesModalButton = document.getElementById('close-minutes-modal-button');

    // Открытие модального окна при клике на кнопку "Поделиться минутами"
    shareMinutesButton.addEventListener('click', function() {
        shareMinutesModal.style.display = 'flex';
    });

    // Закрытие модального окна при клике на кнопку "закрыть" или на область вне окна
    closeMinutesModalButton.addEventListener('click', function() {
        shareMinutesModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === shareMinutesModal) {
            shareMinutesModal.style.display = 'none';
        }
    });

    // Обработка отправки формы
    const shareMinutesForm = document.getElementById('share-minutes-form');

    shareMinutesForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные из формы
        const recipient = document.getElementById('minutes-recipient').value;
        const minutesAmount = document.getElementById('minutes-to-share').value;

        // Выполнение дополнительных действий с получателем и количеством минут
        console.log('Recipient:', recipient);
        console.log('Minutes Amount:', minutesAmount);

        // Скрыть модальное окно после отправки формы
        shareMinutesModal.style.display = 'none';
    });
});

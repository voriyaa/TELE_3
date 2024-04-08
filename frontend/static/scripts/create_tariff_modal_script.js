// Открытие модального окна
function openModal() {
    document.getElementById('modal').classList.add('show-modal');
}

// Закрытие модального окна
function closeModal() {
    document.getElementById('modal').classList.remove('show-modal');
}

// Отправка данных формы
document.getElementById('create-tariff-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
    // Здесь вы можете получить данные формы и отправить их на сервер для обработки
    // После успешного создания тарифа закрываем модальное окно
    closeModal();
});

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

    // Получаем данные формы
    const formData = new FormData(this);
    const jsonData = {};

    // Преобразование formData в JSON
    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });

    // Отправляем данные на сервер
    fetch('http://93.175.7.10:5000/api/login/create_tariff', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось создать тариф');
        }
        // После успешного создания тарифа закрываем модальное окно
        closeModal();
         alert('Успешно!');
    })
    .catch(error => {
        console.error('Ошибка:', error);
        // Добавьте обработку ошибки, например, вывод сообщения пользователю
        alert(error.message);
    });
});

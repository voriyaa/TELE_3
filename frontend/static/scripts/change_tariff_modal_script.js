// Открытие модального окна изменения тарифа
function openChangeTariffModal() {
    document.getElementById('change-tariff-modal').classList.add('show-modal');
}

// Закрытие модального окна изменения тарифа
function closeChangeTariffModal() {
    document.getElementById('change-tariff-modal').classList.remove('show-modal');
}

// Отправка данных формы изменения тарифа
document.getElementById('change-tariff-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию

    // Получаем данные формы
    const formData = new FormData(this);
    const jsonData = {};

    // Преобразование formData в JSON
    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });
    // Отправляем данные на сервер
    const tariffId = parseInt(jsonData['id']);
    delete jsonData['id'];
    console.log(tariffId);
    fetch(`http://93.175.7.10:5000/api/edit_tariff/${tariffId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось изменить тариф');
        }
        // После успешного изменения тарифа закрываем модальное окно
        closeChangeTariffModal();
        alert('Тариф успешно изменён!');
    })
    .catch(error => {
        console.error('Ошибка:', error);
        // Добавьте обработку ошибки, например, вывод сообщения пользователю
        alert(error.message);
    });
});

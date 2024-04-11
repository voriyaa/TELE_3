// Функция для загрузки списка тарифов с сервера и отображения их в модальном окне
function openTariffList() {
    var modal = document.getElementById('tariff-list-modal');
    modal.style.display = 'block';

    // Очистка содержимого списка тарифов перед загрузкой новых данных
    document.getElementById('tariff-list').innerHTML = '';
    // Запрос на сервер для получения списка тарифов
    fetch('http://93.175.7.10:5000/api/list_tariff')
        .then(response => {
            if (!response.ok) {
                throw new Error('Не удалось получить список тарифов');
            }
            return response.json();
        })
        .then(data => {
        // Создание HTML для списка тарифов
        var html = '';
        data.forEach(function(tariff) {
        html += '<tr>';
        html += '<td>' + tariff.id + '</td>';
        html += '<td>' + tariff.gb + '</td>';
        html += '<td>' + tariff.minute + '</td>';
        html += '<td>' + tariff.cost_one_gb + '</td>';
        html += '<td>' + tariff.cost_one_minute + '</td>';
        html += '<td>' + tariff.price + '</td>';
        html += '</tr>';
        });
        // Отображение списка тарифов в модальном окне
        document.getElementById('tariff-list').innerHTML = html;
        })
        .catch(error => {
            console.error('Ошибка загрузки списка тарифов:', error);
            // Обработка ошибки, например, вывод сообщения пользователю
            alert('Произошла ошибка при загрузке списка тарифов');
        });
}

// Функция для закрытия модального окна со списком тарифов
function closeTariffListModal() {
    var modal = document.getElementById('tariff-list-modal');
    modal.style.display = 'none';
}

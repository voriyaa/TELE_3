function loadFirstThreeTariffs() {
        fetch('http://93.175.7.10:5000/api/list_tariff')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Не удалось получить список тарифов');
                }
                return response.json();
            })
            .then(data => {
                console.log(data); // Выводим данные в консоль
                // Создаем пустую строку для формирования HTML
                var html = '';
                // Отображаем только первые три тарифа
                for (let i = 0; i < 3 && i < data.length; i++) {
                    const tariff = data[i];
                    // Формируем HTML для каждого тарифа
                    html += '<option value="' + tariff.id + '">' + tariff.gb + 'GB, ' + tariff.minute + 'min - ' + tariff.cost_one_gb + ' руб/GB, ' + tariff.cost_one_minute + ' руб/min</option>';
                }
                // Находим элемент выбора тарифов и устанавливаем в него сгенерированный HTML
                document.getElementById('tariff_id').innerHTML = html;
            })
            .catch(error => {
                console.error('Ошибка загрузки списка тарифов:', error);
                // Обработка ошибки, например, вывод сообщения пользователю
                alert('Произошла ошибка при загрузке списка тарифов');
            });
    }

    // Вызываем функцию загрузки первых трех тарифов при загрузке страницы
    document.addEventListener('DOMContentLoaded', function () {
        loadFirstThreeTariffs();
    });

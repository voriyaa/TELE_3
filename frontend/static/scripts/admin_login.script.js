document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const formData = new FormData(loginForm);
        const jsonData = {};

        // Преобразование formData в JSON
        for (const [key, value] of formData.entries()) {
            jsonData[key] = value;
        }
        console.log(jsonData)

        fetch('http://93.175.7.10:5000/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
            body: JSON.stringify(jsonData)
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    // Проверяем статус ошибки
                    if (response.status === 409) {
                        throw new Error('Пользователь с таким номером паспорта уже зарегистрирован');
                    } else if (response.status === 410) {
                        throw new Error('Пользователь с таким номером телефона уже зарегистрирован');
                    } else if (response.status === 411) {
                        throw new Error('Пользователь с таким логином уже зарегистрирован');
                    } else {
                        throw new Error('Ошибка при регистрации');
                    }
                }
            })
            .then(data => {
                console.log('Успешная регистрация:', data);
                // Показываем встроенное уведомление об успешной регистрации
                Notification.requestPermission().then(function (result) {
                    if (result === 'granted') {
                        new Notification('Регистрация успешно завершена');
                    }
                });
                // Если регистрация прошла успешно, перенаправляем на страницу логина
                setTimeout(() => {
                    window.location.href = "/admin/login";
                }, 1000); // Перенаправление через 3 секунды
            })
            .catch(error => {
                console.error('Ошибка:', error);
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
                alert(error.message); // Отображаем сообщение об ошибке пользователю
                window.location.href = "/admin/register";
            });
    });
});

function goToLoginPage() {
    window.location.href = "/admin/login";
}

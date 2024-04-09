document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');

    loginForm.addEventListener('submit', async function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const formData = new FormData(loginForm); // Получаем данные формы
        const jsonData = {};

        // Преобразование formData в JSON
        for (const [key, value] of formData.entries()) {
            jsonData[key] = value;
        }

        fetch('http://93.175.7.10:5000/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type
            },
            body: JSON.stringify(jsonData)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Ошибка при входе');
                }
                return response.json();
            })
            .then(data => {
                console.log('Успешный вход:', data);
                // Если регистрация прошла успешно, перенаправляем на страницу логина
                window.location.href = "/admin/login";
            })
            .catch(error => {
                console.error('Ошибка:', error);
                window.location.href = "/admin/register";
                // Добавьте обработку ошибки, например, вывод сообщения пользователю
            });
    });
});
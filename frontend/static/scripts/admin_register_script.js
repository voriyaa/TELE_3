document.addEventListener('DOMContentLoaded', function () {
    const adminRegistrationForm = document.getElementById('adminRegistrationForm');

    adminRegistrationForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const formData = new FormData(adminRegistrationForm);
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
                if (!response.ok) {
                    throw new Error('Ошибка при регистрации');
                }
                return response.json();
            })
            .then(data => {
                console.log('Успешная регистрация:', data);
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

function goToLoginPage() {
    window.location.href = "/admin/login";
}

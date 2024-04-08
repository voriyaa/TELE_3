document.addEventListener('DOMContentLoaded', function() {
    const buyMinutesModal = document.getElementById('buy-minutes-modal');
    const buyMinutesButton = document.getElementById('buy-minutes-button');
    const closeMinutesModalButton = document.getElementById('close-buy-minutes-modal-button');

    buyMinutesButton.addEventListener('click', function() {
        buyMinutesModal.style.display = 'flex';
    });

    closeMinutesModalButton.addEventListener('click', function() {
        buyMinutesModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === buyMinutesModal) {
            buyMinutesModal.style.display = 'none';
        }
    });

    const buyMinutesForm = document.getElementById('buy-minutes-form');

    buyMinutesForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const minutesAmount = document.getElementById('minutes-amount').value;

        // Дополнительные действия с количеством минут
        console.log('Amount of Minutes to Buy:', minutesAmount);

        buyMinutesModal.style.display = 'none';
    });
});

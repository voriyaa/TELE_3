document.addEventListener('DOMContentLoaded', function() {
    const buyGBModal = document.getElementById('buy-gb-modal');
    const buyGBButton = document.getElementById('buy-gb-button');
    const closeGBModalButton = document.getElementById('close-buy-gb-modal-button');

    buyGBButton.addEventListener('click', function() {
        buyGBModal.style.display = 'flex';
    });

    closeGBModalButton.addEventListener('click', function() {
        buyGBModal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === buyGBModal) {
            buyGBModal.style.display = 'none';
        }
    });

    const buyGBForm = document.getElementById('buy-gb-form');

    buyGBForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const gbAmount = document.getElementById('gb-amount').value;

        // Дополнительные действия с количеством GB
        console.log('Amount of GB to Buy:', gbAmount);

        buyGBModal.style.display = 'none';
    });
});

const button = document.getElementById('myButton');

button.addEventListener('click', async () => {
    try {
        const response = await fetch('/game', {
            method: 'POST'
        });

        if (!response.ok) {
            throw new Error('Не удалось создать игру');
        }

        const result = await response.json();

        console.log(result);

        window.location.href = `/game/${result.id}`;

    } catch (error) {
        console.error(error);
    }
});
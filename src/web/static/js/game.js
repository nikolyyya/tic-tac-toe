const gameId = document.body.dataset.gameId;
let cells = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
let gameOver = false;

const SYMBOLS = { 0: '', 1: 'X', 2: 'O' };

function render() {
    document.querySelectorAll('.matrix td').forEach(td => {
        const r = Number(td.dataset.row);
        const c = Number(td.dataset.col);
        td.textContent = SYMBOLS[cells[r][c]];
    });
}

function showResult(result) {
    if (!result.game_over) return;

    gameOver = true;
    const status = document.getElementById('status');

    if (result.winner === 1) {
        status.textContent = 'Победили крестики (вы)!';
    } else if (result.winner === 2) {
        status.textContent = 'Победили нолики (компьютер)';
    } else {
        status.textContent = 'Ничья';
    }
}

async function loadGame() {
    try {
        const response = await fetch(`/game/${gameId}/state`);
        if (!response.ok) throw new Error('Не удалось загрузить игру');

        const result = await response.json();
        cells = result.cells;
        render();
        showResult(result);
    } catch (error) {
        console.error(error);
    }
}

async function makeMove(r, c) {
    if (gameOver || cells[r][c] !== 0) return;

    const newCells = cells.map(row => [...row]);
    newCells[r][c] = 1;

    try {
        const response = await fetch(`/game/${gameId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cells: newCells })
        });

        if (!response.ok) {
            console.error('Ход не принят');
            return;
        }

        const result = await response.json();
        cells = result.cells;
        render();
        showResult(result);
    } catch (error) {
        console.error(error);
    }
}

document.querySelectorAll('.matrix td').forEach(td => {
    td.addEventListener('click', () =>
        makeMove(Number(td.dataset.row), Number(td.dataset.col))
    );
});

loadGame();
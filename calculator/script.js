let display = document.getElementById('display');

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    updateToggleButton();
}

function updateToggleButton() {
    const toggleBtn = document.querySelector('.toggle-dark');
    if (document.body.classList.contains('dark-mode')) {
        toggleBtn.textContent = '☀️';
    } else {
        toggleBtn.textContent = '🌙';
    }
}

// Load dark mode preference
window.addEventListener('DOMContentLoaded', () => {
    const darkMode = localStorage.getItem('darkMode') === 'true';
    if (darkMode) {
        document.body.classList.add('dark-mode');
    }
    updateToggleButton();
});

function appendNumber(num) {
    display.value += num;
}

function appendOperator(op) {
    if (display.value !== '') {
        display.value += op;
    }
}

function appendDecimal() {
    if (display.value !== '' && !display.value.includes('.')) {
        display.value += '.';
    }
}

function clearDisplay() {
    display.value = '';
}

function deleteLastChar() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        let result = eval(display.value);
        display.value = result;
    } catch (error) {
        display.value = 'Error';
    }
}

// Allow keyboard input
document.addEventListener('keydown', (event) => {
    const key = event.key;

    if (key >= '0' && key <= '9') {
        appendNumber(key);
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        event.preventDefault();
        appendOperator(key);
    } else if (key === '.') {
        appendDecimal();
    } else if (key === 'Enter') {
        event.preventDefault();
        calculate();
    } else if (key === 'Backspace') {
        event.preventDefault();
        deleteLastChar();
    } else if (key === 'Escape') {
        clearDisplay();
    }
});

// test calculator functions
function testCalculator() {
    // Test appending numbers
    display.value = '';
    appendNumber('5');
    console.assert(display.value === '5', 'Test 1 Failed: appendNumber');
    // Test appending operators
    appendOperator('+');
    console.assert(display.value === '5+', 'Test 2 Failed: appendOperator');
    // Test appending decimal
    appendDecimal();
    console.assert(display.value === '5+.', 'Test 3 Failed: appendDecimal');
    // Test calculating result
    display.value = '5+3';
    calculate();
    console.assert(display.value === '8', 'Test 4 Failed: calculate');
    // Test clearing display    clearDisplay();
    console.assert(display.value === '', 'Test 5 Failed: clearDisplay');
    // Test deleting last character
    display.value = '123';
    deleteLastChar();
    console.assert(display.value === '12', 'Test 6 Failed: deleteLastChar');
    console.log('All tests passed!');
}
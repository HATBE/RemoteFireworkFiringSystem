let power = false;

const elPowerBtn = document.getElementById('power-btn');

function togglePower() {
    power = !power;
    alert(power)
}

elPowerBtn.addEventListener('click', () => {
    togglePower();
})
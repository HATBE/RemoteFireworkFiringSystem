let power = false;

const elPowerBtn = document.getElementById('power-btn');
const elFireAllBtn = document.getElementById('fire-all-btn');
const elDisplayText = document.getElementById('display-text');

const elsFireBtn = document.querySelectorAll('.fire-btn');

const textColorClassesList = {red: 'text-red', black: 'text-black', green: 'text-green'};

// -----------------------------------------
// ----------------------------------------- FUNCTIONS
// -----------------------------------------

function init() {
    power = false;
    disarm();
}

function togglePower() {
    power = !power;
    
    if(power) {
        arm();
    } else {
        disarm();
    }
}

function arm() {
    power = true;
    elsFireBtn.forEach(fireBtn => {
        fireBtn.disabled = false;
    });
    elFireAllBtn.disabled = false;

    setDisplayText('ARMED', textColorClassesList.red);
    elPowerBtn.classList.remove('off');
    elPowerBtn.classList.add('on');
}

function disarm() {
    power = false;
    elsFireBtn.forEach(fireBtn => {
        fireBtn.disabled = true;
    });
    elFireAllBtn.disabled = true;

    setDisplayText('NOT ARMED', textColorClassesList.green);
    elPowerBtn.classList.remove('on');
    elPowerBtn.classList.add('off');
}

function setDisplayText(text, color) {
    elDisplayText.textContent = text;
    Object.values(textColorClassesList).forEach(colorClass => {
        elDisplayText.classList.remove(colorClass);
    });
    elDisplayText.classList.add(color);
}

// -----------------------------------------
// ----------------------------------------- SCRIPT
// -----------------------------------------

init();

// ----------------------------------------- EVENT LISTENERS
elPowerBtn.addEventListener('click', () => {
    togglePower();
});

elFireAllBtn.addEventListener('click', () => {
    disarm(); // disarm until action was performed 
    alert('FIRE ALL');
});

elsFireBtn.forEach(fireBtn => {
    fireBtn.addEventListener('click', () => {
        disarm(); // disarm until action was performed 
        alert(fireBtn.dataset.id);
        
    });
});
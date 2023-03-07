let power = false;

const elPowerBtn = document.getElementById('power-btn');
const elFireAllBtn = document.getElementById('fire-all-btn');
const elResetBtn = document.getElementById('reset-btn');

const elDisplayText = document.getElementById('display-text');
const elDisplaySubText = document.getElementById('display-sub-text');

const elsFireBtn = document.querySelectorAll('.fire-btn');

const textColorClassesList = {red: 'text-red', black: 'text-black', green: 'text-green', white: 'text-white'};

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
        clearSubText();
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
    elResetBtn.disabled = true;

    setDisplayText('NOT ARMED', textColorClassesList.green);
    elPowerBtn.classList.remove('on');
    elPowerBtn.classList.add('off');
}

// \/ START ----------------------------------------- DISPLAY TEXT \/
function setDisplayText(text, color = textColorClassesList.white) {
    clearText();
    elDisplayText.textContent = text;
    elDisplayText.classList.add(color);
}

function setDisplaySubText(text, color = textColorClassesList.white) {
    clearSubText();
    elDisplaySubText.textContent = text;
    elDisplaySubText.classList.add(color);
}

function clearText() {
    elDisplayText.textContent = '';
    Object.values(textColorClassesList).forEach(colorClass => {
        elDisplayText.classList.remove(colorClass);
    });
}

function clearSubText() {
    elDisplaySubText.textContent = '';
    Object.values(textColorClassesList).forEach(colorClass => {
        elDisplaySubText.classList.remove(colorClass);
    });
}
// /\ END ----------------------------------------- DISPLAY TEXT /\

function resetBoard() {
    clearSubText();
    elFireAllBtn.disabled = false;
    elsFireBtn.forEach(fireBtn => {
        fireBtn.disabled = false;
    });
    elResetBtn.disabled = true;
}

function fireall() {
    elFireAllBtn.disabled = true;
    elsFireBtn.forEach(fireBtn => {
        fireBtn.disabled = true;
    });
    elResetBtn.disabled = false

    setDisplaySubText('Send signal to all channels', textColorClassesList.white);

    fetch('http://10.10.10.106/api.php/fireall', {
        method: 'POST'
    })
    .then(response=>response.text()).then(data=>{
        setDisplaySubText('Fired all channels', textColorClassesList.white);
     });
}

function fireSingle(fireBtn) {
    // if one of the channel fire buttons are pressed,
    // the fireall btn and the fire channel x btn is disabled

    const id = fireBtn.dataset.id;

    elResetBtn.disabled = false
    elFireAllBtn.disabled = true;
    fireBtn.disabled = true;
    setDisplaySubText(`Send signal to channel ${id}`, textColorClassesList.white);

    fetch(`http://10.10.10.106/api.php/fire/${id}`, {
        method: 'POST'
    })
    .then(response=>response.text()).then(data=>{
        setDisplaySubText(`Fired channel ${id}`, textColorClassesList.white);
     });
}

// -----------------------------------------
// ----------------------------------------- SCRIPT
// -----------------------------------------

init();

// ----------------------------------------- EVENT LISTENERS
// if power button was pressed
elPowerBtn.addEventListener('click', () => {
    togglePower();
});

// if reset button was pressed
elResetBtn.addEventListener('click', () => {
    resetBoard();
});

// if fire all button was pressed
elFireAllBtn.addEventListener('click', () => {
    fireall();
});

// if one of the channel fire buttons was pressed
elsFireBtn.forEach(fireBtn => {
    fireBtn.addEventListener('click', () => {
       fireSingle(fireBtn);
    });
});
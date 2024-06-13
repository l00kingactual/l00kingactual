// Assuming elements_dict is imported from elements00.js
const elementMenu = document.getElementById('elementMenu');

// Populate the menu dynamically
for (const [atomicNumber, elementData] of Object.entries(elements_dict)) {
  const li = document.createElement('li');
  li.className = 'nav-item';
  const a = document.createElement('a');
  a.className = 'nav-link';
  a.textContent = elementData['Symbol'];
  a.addEventListener('click', () => visualizeElement(atomicNumber));
  li.appendChild(a);
  elementMenu.appendChild(li);
}

// Function to visualize an element
function visualizeElement(atomicNumber) {
  const elementData = elements_dict[atomicNumber];
  const visualization = document.getElementById('visualization');
  visualization.innerHTML = ''; // Clear previous visualization

  // Create a point for the nucleus
  const nucleus = document.createElement('div');
  nucleus.className = 'nucleus';
  visualization.appendChild(nucleus);

  // Create rings for shells and populate with electrons
  for (const [index, shellElectrons] of elementData['Shells'].entries()) {
    const shell = document.createElement('div');
    shell.className = `shell shell-${index + 1}`;
    for (let i = 0; i < shellElectrons; i++) {
      const electron = document.createElement('div');
      electron.className = 'electron';
      shell.appendChild(electron);
    }
    visualization.appendChild(shell);
  }
}

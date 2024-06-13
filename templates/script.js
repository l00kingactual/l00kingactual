let elements_dict = {};
let theoretical_elements = {};
let extended_periodic_table = {};
let elements_description_type = {};

// Fetch and populate elements_dict
fetch('elements.json')
  .then(response => response.json())
  .then(data => {
    elements_dict = data;
    populateMenu(elements_dict, 'elementsMenu');
  });

// Fetch other JSON files similarly...

// Function to populate the Navbar menu
function populateMenu(elements, menuId) {
  const menu = document.getElementById(menuId);
  for (const [key, value] of Object.entries(elements)) {
    const li = document.createElement('li');
    li.className = 'nav-item';
    li.innerHTML = `<a class="nav-link" href="#" onclick="showElement(${key})">${value.Symbol}</a>`;
    menu.appendChild(li);
  }
}

// Function to show element visualization
function showElement(atomicNumber) {
  // Your visualization logic here
}

document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('container');
    
    // Función para obtener datos desde la API
    async function fetchData() {
        try {
            const response = await fetch('https://api.ejemplo.com/data'); // URL de tu API
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Función para crear y poblar las cartas
    function createCards(data) {
        data.forEach(item => {
            // Crear un nuevo div con la clase 'card'
            const div = document.createElement('div');
            div.className = 'card';

            // Crear el elemento h1 y añadir el título
            const h1 = document.createElement('h1');
            h1.textContent = item.title;
            div.appendChild(h1);

            // Crear el primer párrafo y añadir el texto
            const p1 = document.createElement('p');
            p1.textContent = item.para1;
            div.appendChild(p1);

            // Crear el segundo párrafo y añadir el texto
            const p2 = document.createElement('p');
            p2.textContent = item.para2;
            div.appendChild(p2);

            // Añadir el div al contenedor
            container.appendChild(div);
        });
    }

    // Obtener los datos y crear las cartas
    fetchData().then(data => {
        if (data && data.length > 0) {
            createCards(data);
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Hacer una solicitud AJAX para obtener los datos de Django
    fetch('')
        .then(response => response.json())
        .then(data => {
            // Obtener la suma de premios
            const sumaPremios = data.suma_premios;

            // Obtener la lista de premios
            const premios = data.premios;

            // Referencia al elemento HTML donde se mostrarán los premios
            const premiosContainer = document.getElementById('premios-container');

            // Iterar sobre cada premio y crear un div para representarlo
            premios.forEach(premio => {
                const premioDiv = document.createElement('div');
                premioDiv.classList.add('premio');

                const titulo = document.createElement('h2');
                titulo.textContent = premio.titulo;
                premioDiv.appendChild(titulo);

                const descripcion = document.createElement('p');
                descripcion.textContent = premio.descripcion;
                premioDiv.appendChild(descripcion);

                if (premio.imagen_url) {
                    const imagen = document.createElement('img');
                    imagen.src = premio.imagen_url;
                    premioDiv.appendChild(imagen);
                }

                premiosContainer.appendChild(premioDiv);
            });
        })
        .catch(error => console.error('Error al obtener datos de premios:', error));
});
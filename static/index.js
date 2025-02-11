// shows the API URL in the input field
document.getElementById("api-url").value = window.location.href;

// load routes from the API
async function loadRoutes() {
  try {
    const response = await fetch("/sitemap");
    const data = await response.json();
    const endpointsList = document.getElementById("endpoints");
   
    

    data.forEach((route) => {
      
      if (route !== "/admin" && route !== "/sitemap") {
        // exclude admin routes
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = route;
        a.textContent = route;
        li.appendChild(a);
        endpointsList.appendChild(li);
      }
    });
  } catch (error) {
    console.error("Error loading routes:", error);
  }
}

loadRoutes();

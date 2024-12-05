const searchField = document.querySelector('#search-field');
const tableOutput = document.querySelector('.table_output');
const appTable = document.querySelector('.app_table');
const paginationContainer = document.querySelector('.pagination-container');
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");

tableOutput.style.display = "none";

searchField.addEventListener('keyup', (e) => {
    const searchVal = e.target.value;

    if (searchVal.trim().length > 0) {
        paginationContainer.style.display = "none";
        tbody.innerHTML = "";
        fetch("search_appointments", {
          body: JSON.stringify({ searchText: searchVal }),
          method: "POST",
        })
          .then((res) => res.json())
          .then((data) => {
            
            appTable.style.display = "none";
            tableOutput.style.display = "block";
    
            if (data.length === 0) {
              noResults.style.display = "block";
              tableOutput.style.display = "none";
            } else {
              noResults.style.display = "none";
              data.forEach((item) => {
                tbody.innerHTML += `
                    <tr>
                    <td>${item.category}</td>
                    <td>${item.description}</td>
                    <td>${item.date}</td>
                    </tr>`;
              });
            }
          });
      } else {
        tableOutput.style.display = "none";
        appTable.style.display = "block";
        paginationContainer.style.display = "block";
      }
});
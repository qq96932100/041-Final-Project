var search_bar_btn = document.getElementById('search_bar_btn');


search_bar_btn.addEventListener('click', function () {
    console.log('Parent Capturing');
    show_stock_number();
    new_page();
  }, true);

  
function show_stock_number() {
      let search_bar_input = document.getElementById("search_bar_input")
      document.getElementById("stock_number").innerHTML = search_bar_input.value;
  }

function new_page() {
    location.replace("http://127.0.0.1:5500/django/sample/templates/index.html")
  }
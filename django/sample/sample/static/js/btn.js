var search_bar_btn = document.getElementById('search_bar_btn');


search_bar_btn.addEventListener('click', function () {
    console.log('Parent Capturing');
    if(get_input() != ''){
      show_stock_number();   
      post_data();  
    }
    // reload();
  }, true);
 
function get_input() {
      let search_bar_input = document.getElementById("search_bar_input").value;
      // document.getElementById("stock_number").innerHTML = search_bar_input.value;
      return search_bar_input;
  }

function show_stock_number() {
      document.getElementById("stock_number").innerHTML = get_input();
  }

function reload() {
    location.reload()
  }

function post_data() {
  var xhr = new XMLHttpResquest; //創建xhr
  var data = { //創建json
    input : get_input()
  }
  xhr.open('post',location,true);
  // 傳送資料的格式選擇為 JSON
  xhr.setRequestHeader('Content-type', 'application/json');
  // 用另一個變數儲存字串化的 JSON
  var data = JSON.stringify(account);
  // 傳送
  xhr.send(data);  
} 
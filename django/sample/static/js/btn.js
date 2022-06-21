const search_bar_btn = document.getElementById('search_bar_btn');
// let url = "http://127.0.0.1:5500/django/sample/templates/index/?q=123&input=avasdemon";
const menu_bar_btn = document.getElementById('menu_button');
let bool = 1;

search_bar_btn.addEventListener('click', function () {
    if(get_input() != ''){
      set_stock_number();
      send_data();

      // console.log('par:' + url.search());
    }
    // reload();
  }, true);

function get_input() {
      let search_bar_input = document.getElementById("search_bar_input").value;
      return search_bar_input;
  }

function set_stock_number() {
      document.getElementById("stock_number").innerHTML = get_input();
  }

function reload() {
    location.reload()
  }

function send_data() {
    var xhr;
    if (window.XMLHttpRequest) { //檢查瀏覽器的XMLHttpRequest屬性，如果為真則支持XMLHttpRequest
      // IE7+, Firefox, Chrome, Opera, Safari 瀏覽器執行代碼
      xhr=new XMLHttpRequest();
    } else {
      // IE6, IE5 瀏覽器執行代碼
      xhr=new ActiveXObject("Microsoft.XMLHTTP");
    }

  /*
    xhr.open(get,url,async);
    send(string);  //post請求時才使用字符串參數，否則不用帶參數。

    method：請求的類型，常見的get或post方法
    url：向伺服器請求的地址
    async：true（異步）或 false（同步）,默認為true異步
  */

  // get方式：
  // xhr.open('GET', location + 'stock_search/?input='+ get_input());
  // xhr.send();
  window.location.href = location.origin + '/stock_search?input='+ get_input();
  console.log(window.location.href);
  // POST方式
  // xhr.open('POST', "/articles/" + article_id + "/likes/");
  // xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=utf-8"); //必須寫在open和send中間

  // xhr.send("key=value&key2=value2");

  /*
  注意：
  1) post請求一定要設置請求頭的格式內容;
  2) post請求參數放在send裡面，即請求體.
  */
}

menu_bar_btn.addEventListener('click', function () {
  // myFunction();
  bool = !bool;
  if(bool){
    openNav();
  }else{
    closeNav();
  }
  // reload();
}, true);

// function myFunction() {
//   menu_bar_btn.classList.toggle("change");
// }

function openNav() {
  menu = document.getElementsByClassName("menu")[0];
  menu_btn = document.getElementById('menu_button');
  // menu.style.visibility = "hidden";
  menu.style.width = "15vw";
  menu.style.opacity = 1;
  // menu_btn.style.visibility = "visible";
  menu.style.transition = "0.25s";
  // menu_btn.style.opacity = 0;
  // menu.style.visibility = "collapse";
}

function closeNav() {
  menu = document.getElementsByClassName("menu")[0];
  menu_btn = document.getElementById('menu_button');
  // menu.style.visibility = "hidden";
  menu.style.width = "0vw";
  menu.style.opacity = 0;
  // menu_btn.style.visibility = "visible";
  menu.style.transition = "0.25s";
  // menu_btn.style.opacity = 1;
  // menu.style.visibility = "collapse";
}

// closeNav()
const chart_date_btn = document.getElementById('chart_date_btn');

chart_date_btn.addEventListener('click', function () {
  let begin_date = get_input()[0];
  let end_date = get_input()[1];
  
  if(begin_date != '' & end_date != ''){ //避免空值error
        console.log('begin_date='+begin_date + ', end_date=' + end_date);
        console.log("suscces")
        set_chart(chart_1='trend.jpg', chart_2='kline.jpg'); //這裡輸入圖表檔名
        send_data();
    }
    // reload();
  }, true);

function get_input() {
        // let search_bar_input = document.getElementById("search_bar_input").value;
        let begin_date = document.getElementById("begin_date").value;
        let end_date =  document.getElementById("end_date").value;
        // document.getElementById("stock_number").innerHTML = search_bar_input.value;
        return [search_bar_input,begin_date, end_date]; // 我是數組
    }

function set_chart(chart_1, chart_2) {
        document.getElementById("chart_1").src = "../static/" + chart_1;
        document.getElementById("chart_2").src = "../static/" + chart_2;
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
      let dates = get_input();
      xhr.open('GET', location + '?begin_date='+ dates[0] + '&end_date=' + dates[1]);
      xhr.send();
    
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
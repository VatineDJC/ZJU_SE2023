<template>
  <div class="hello">
 
      <font size="5">  
      <ul style="text-align: left;"> 
        <li><a href="/home">首页</a></li>  
        <li><a href="#">关于我们</a></li> 
        <li><a href="#">服务项目</a></li>  
        <li><a href="#">联系我们</a></li>   
      </ul>
      <div style="text-align: right;">
        <li><a href="#">历史</a></li>  
        <li><a href="#">购物车({{ cart_items_number }})</a></li>  
        <li><a href="#">个人中心({{ username }})</a></li>  
      </div>
      </font> 

     <br/>
     <div>
     	 <div>
	     	 <el-input v-model="input" placeholder="关键词" maxlength="10" show-word-limit style="width: 1000px;" @keyup.enter.native="search_key(input)"></el-input>
	     	  <el-button type="primary" icon="el-icon-search"  @click="search_key(input)">查询</el-button>  	
        </div>
     </div>
    <br/>
     <el-row>
      <el-button type="success" @click="search_tag('stationery')">文具</el-button>
      <el-button type="success" @click="search_tag('book')">书籍</el-button>
      <el-button type="success" @click="search_tag('daily')">日用品</el-button>
      <el-button type="success" @click="search_tag('snack')">零食饮料</el-button>
      <el-button type="success" @click="search_tag('equipment')">电器设备</el-button>
    </el-row>
    <br/>

    <div id="group">
    <div id="div1" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image1[0]">
      <font size="4.8">  
      <div class="title">{{ images1[0].title }}</div>
        <div class="info">{{ images1[0].info }}</div>
        <div class="money">{{ images1[0].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div2" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image1[1]">
      <font size="4.8">  
        <div class="title">{{ images1[1].title }}</div>
        <div class="info">{{ images1[1].info }}</div>
        <div class="money">{{ images1[1].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div3" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image1[2]">
      <font size="4.8">  
        <div class="title">{{ images1[2].title }}</div>
        <div class="info">{{ images1[2].info }}</div>
        <div class="money">{{ images1[2].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div4" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image1[3]">
      <font size="4.8">  
        <div class="title">{{ images1[3].title }}</div>
        <div class="info">{{ images1[3].info }}</div>
        <div class="money">{{ images1[3].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    </div>
    <div id="group">
    <div id="div1" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image2[0]">
      <font size="4.8">  
      <div class="title">{{ images2[0].title }}</div>
        <div class="info">{{ images2[0].info }}</div>
        <div class="money">{{ images2[0].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div2" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image2[1]">
      <font size="4.8">  
        <div class="title">{{ images2[1].title }}</div>
        <div class="info">{{ images2[1].info }}</div>
        <div class="money">{{ images2[1].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div3" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image2[2]">
      <font size="4.8">  
        <div class="title">{{ images2[2].title }}</div>
        <div class="info">{{ images2[2].info }}</div>
        <div class="money">{{ images2[2].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    <div id="div4" style="background-color: #f3cbcb;
            text-align: center;">
      <img :src="image2[3]">
      <font size="4.8">  
        <div class="title">{{ images2[3].title }}</div>
        <div class="info">{{ images2[3].info }}</div>
        <div class="money">{{ images2[3].price }}</div>
        <a href="#">details</a>
      </font>
    </div>
    </div>
  </div>
</template>
 
<script>
import axios from "axios"
import querystring from "querystring"
export default {
  name: "home",
  data(){
    return{
      cart_items_number: 0,
      username: "user",
      input: '',
      images1: [
        {src: '../assets/1.jpeg', title: '晨光圆珠笔', info: '新买的,低价出十支', price: '10.0元'},
        {src: '../assets/2.jpg', title: '小米路由器', info: '用了三个月,支持WIFI6', price: '100.0元'},
        {src: '../assets/3.jpg', title: '抽纸', info: '清风抽纸5包', price: '5.0元'},
        {src: '../assets/logo.png', title: 'title', info: 'info', price: 'CNY'}
      ],
      images2: [
        {src: '../assets/1.jpeg', title: '晨光圆珠笔', info: '新买的,低价出十支', price: '10.0元'},
        {src: '../assets/2.jpg', title: '小米路由器', info: '用了三个月,支持WIFI6', price: '100.0元'},
        {src: '../assets/logo.png', title: 'title', info: 'info', price: 'CNY'},
        {src: '../assets/logo.png', title: 'title', info: 'info', price: 'CNY'}
      ],
      image1:[
        require( '../assets/1.jpeg' ),
        require( '../assets/2.jpg' ),
        require( '../assets/3.jpg' ),
        require( '../assets/logo.png' )
      ],
      image2:[
        require( '../assets/1.jpeg' ),
        require( '../assets/2.jpg' ),
        require( '../assets/logo.png' ),
        require( '../assets/logo.png' )
      ]
    }
  },
  methods:{
    search_key(input){ 
    axios.post("/api/item/search_key", querystring.stringify({ input: input})).then(function (response){
    console.log(rsponse);
    this.images1 = [
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''}
        ];
    this.images2 = [
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''}
        ];
        this.image1 = [null, null, null, null];
        this.image2 = [null, null, null, null];
    this.item_count = 0;
    for (var item in response.data){
      this.item_count += 1;
      if(this.item_count == 9) break;  
      if(this.item_count <= 4)
      {
        this.images1[this.item_count-1]['src'] = string(response.data[item].images[0]['imageData']);
        this.images1[this.item_count-1]['title'] = response.data[item].name;
        this.images1[this.item_count-1]['info'] = response.data[item].description;
        this.images1[this.item_count-1]['price'] = response.data[item].price;
        img = string(response.data[item].images[0]['imageData']);
        this.image1[this.item_count-1] = require(`${img}`);
      }else{
        this.images2[this.item_count-5]['src'] = string(response.data[item].images[0]['imageData']);
        this.images2[this.item_count-5]['title'] = response.data[item].name;
        this.images2[this.item_count-5]['info'] = response.data[item].description;
        this.images2[this.item_count-5]['price'] = response.data[item].price;
        img = string(response.data[item].images[0]['imageData']);
        this.image2[this.item_count-5] = require(`${img}`);
      } 
    }
    }).catch(function (error){
      console.log(error);
    });
  },

  search_tag(string){ 
    axios.post("/api/item/search_tag", querystring.stringify({sting: string})).then(function (response){
      console.log(rsponse);
    this.images1 = [
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''}
        ];
    this.images2 = [
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''},
      {src: '', title: '', info: '', price: ''}
        ];
        this.image1 = [null, null, null, null];
        this.image2 = [null, null, null, null];
    this.item_count = 0;
    for (var item in response.data){
      this.item_count += 1;
      if(this.item_count == 9) break;    
      if(this.item_count <= 4)
      {
        this.images1[this.item_count-1]['src'] = string(response.data[item].images[0]['imageData']);
        this.images1[this.item_count-1]['title'] = response.data[item].name;
        this.images1[this.item_count-1]['info'] = response.data[item].description;
        this.images1[this.item_count-1]['price'] = response.data[item].price;
        img = string(response.data[item].images[0]['imageData']);
        this.image1[this.item_count-1] = require(`${img}`);
      }else{
        this.images2[this.item_count-5]['src'] = string(response.data[item].images[0]['imageData']);
        this.images2[this.item_count-5]['title'] = response.data[item].name;
        this.images2[this.item_count-5]['info'] = response.data[item].description;
        this.images2[this.item_count-5]['price'] = response.data[item].price;
        img = string(response.data[item].images[0]['imageData']);
        this.image2[this.item_count-5] = require(`${img}`);
      } 
    }
    }).catch(function (error){
      console.log(error);
    });
  }
 }
};
</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#group{
  display: flex;
  justify-content: center;
}
#group > div{
  flex-grow: 4;
  width: 25%;
  max-width: 25%;
  height:auto;
}
div img{
  width: 100%;
  height: 70%;
}
a{text-decoration: none;}
a:hover{text-decoration: none;}
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
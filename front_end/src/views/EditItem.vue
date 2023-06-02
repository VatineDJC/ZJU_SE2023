<template>
    <div class="hello">
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="商品名称">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="商品类别">
                <el-select v-model="form.kind" placeholder="请选择商品类别">
                    <el-option label="无" value="wu"></el-option>
                    <el-option label="文具" value="wenju"></el-option>
                    <el-option label="书籍" value="shuji"></el-option>
                    <el-option label="电器" value="dianqi"></el-option>
                    <el-option label="日用品" value="riyongpin"></el-option>
                    <el-option label="化妆品" value="huazhuangpin"></el-option>
                    <el-option label="零食饮料" value="lingshiyinliao"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="商品价格">
                <el-input v-model="form.price" placeholder="元"></el-input>
            </el-form-item>
            <el-form-item label="商品简介">
                <el-input type="textarea" v-model="form.desc" placeholder="10字以内"></el-input>
            </el-form-item>
            <el-form-item label="商品详情">
                <el-input type="textarea" v-model="form.details"></el-input>
            </el-form-item>

            <el-form-item>
                <el-upload class="upload-demo" action="" :on-preview="handlePreview" :on-remove="handleRemove"
                    :file-list=fileList list-type="picture">
                    <el-button size="small" type="primary">上传图片</el-button>
                    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件</div>
                </el-upload>
            </el-form-item>

            <el-form-item>
                <el-button type="primary" @click="onSubmit">保存</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
   
<script>
import axios from "axios"
import querystring from "querystring"
export default {
    name: "edit",
    data() {
        return {
            form: {
                name: '',
                kind: '',
                price: '',
                desc: '',
                details: '',
            },
            fileList: [{ name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100' }],
        }
    },
    created() {
        this.form.name = 'name';
        this.form.kind = 'wu';
        this.form.price = '0';
        this.form.desc = 'desc';
        this.form.details = 'datails';
        this.fileList = [];
    },
    methods: {
        onSubmit() {
            console.log('submit!');
            console.log(this.form);
            this.$message({
                message: '成功',
                type: 'success'
            });
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        }
    }
};
</script>
   
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
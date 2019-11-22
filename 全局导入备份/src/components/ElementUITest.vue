<template>
  <div class="elui">
  <el-row :gutter="20">
    <el-col :span="6" align="center"><div class="grid-content bg-purple" style="font-size:18px">Section One</div></el-col>
    <el-col :span="6" align="center"><div class="grid-content bg-purple" style="font-size:18px">Section Two</div></el-col>
    <el-col :span="6" align="center"><div class="grid-content bg-purple" style="font-size:18px">Section Three</div></el-col>
    <el-col :span="6" align="center"><div class="grid-content bg-purple" style="font-size:18px">Section Four</div></el-col>
  </el-row>
  <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="item in imgList" :key="item.id">
      <img :src="item.idView" class="image">
    </el-carousel-item>
  </el-carousel>
  <el-tabs type="border-card" style="height: 300px">
    <el-tab-pane label="按钮">
      <el-row>
        <el-button icon="el-icon-search" circle></el-button>
        <el-button type="primary" icon="el-icon-edit" circle></el-button>
        <el-button type="success" icon="el-icon-check" circle></el-button>
        <el-button type="info" icon="el-icon-message" circle></el-button>
        <el-button type="warning" icon="el-icon-star-off" circle></el-button>
        <el-button type="danger" icon="el-icon-delete" circle></el-button>
      </el-row>
    </el-tab-pane>
    <el-tab-pane label="日期">
      <div class="block">
        <span class="demonstration">默认</span>
        <el-date-picker
          v-model="value1"
          type="date"
          placeholder="选择日期">
        </el-date-picker>
      </div>
      <div class="block">
        <span class="demonstration">带快捷选项</span>
        <el-date-picker
          v-model="value2"
          align="right"
          type="date"
          placeholder="选择日期"
          :picker-options="pickerOptions">
        </el-date-picker>
      </div>
    </el-tab-pane>
    <el-tab-pane label="评分">
      <div class="block">
        <span class="demonstration">默认不区分颜色</span>
        <el-rate v-model="value11"></el-rate>
      </div>
      <div class="block">
        <span class="demonstration">区分颜色</span>
        <el-rate
          v-model="value22"
          :colors="colors">
        </el-rate>
      </div>
    </el-tab-pane>
    <el-tab-pane label="上传">
      <el-upload
        class="upload-demo"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        list-type="picture">
      <el-button size="small" type="primary">点击上传</el-button>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
    </el-tab-pane>
    <el-tab-pane label="图预览">
      <el-image style="width: 100px; height: 100px" :src="url" :preview-src-list="srcList"></el-image>
    </el-tab-pane>
  </el-tabs>
  <el-steps :active="active" finish-status="success">
    <el-step title="step 1"></el-step>
    <el-step title="step 2"></el-step>
    <el-step title="step 3"></el-step>
  </el-steps>
  <el-button @click="next">下一步</el-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      srcList: [
        'https://fuss10.elemecdn.com/8/27/f01c15bb73e1ef3793e64e6b7bbccjpeg.jpeg',
        'https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg',
        'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
        'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
        'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
        'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg'
      ],
      imgList: [
        {id: 0, idView: require('./assets/logo.png')},
        {id: 1, idView: require('./assets/logo.png')},
        {id: 2, idView: require('./assets/logo.png')},
        {id: 3, idView: require('./assets/logo.png')},
        {id: 4, idView: require('./assets/logo.png')},
        {id: 5, idView: require('./assets/logo.png')}
      ],
      active: 0,
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      },
      value1: '',
      value11: null,
      value2: '',
      value22: null,
      colors: ['#99A9BF', '#F7BA2A', '#FF9900'],
      fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}]
    }
  },
  name: 'ElementUITest',
  mounted () {
    this.$message({
      type: 'success',
      message: 'element-ui安装成功'
    })
    this.$notify({
      title: '成功',
      message: 'element-ui安装成功',
      type: 'success'
    })
  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    next () {
      if (this.active++ > 2) this.active = 0
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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

<style>
  .el-row {
    margin-bottom: 20px;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    line-height:1.7;
    font-family: 'Microsoft YaHei';
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>

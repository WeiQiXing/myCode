<template>
  <div class="myform">
    <el-form style="width:430px" status-icon :rules="rules2" label-width="100px">
      <el-form-item label="账号">
        <el-input v-model="form.userId" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item :rules="[{ required: true, message: '姓名不能为空'}]" label="姓名" prop="userName">
        <el-input v-model="form.userName" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item label="手机号码" prop="phone">
        <el-input v-model="form.phone" auto-complete="off" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item label="出生日期">
        <el-date-picker v-model="datevalue" type="datetime" placeholder="选择日期时间" :picker-options="pickerOptions"></el-date-picker>
      </el-form-item>
      <el-form-item label="性别">
        <div class="fl">
          <el-radio-group v-model="form.sex">
            <el-radio label="MAN">男</el-radio>
            <el-radio label="WOMAN">女</el-radio>
          </el-radio-group>
        </div>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="form.email" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" style="position:fixed; bottom:-9999px"></el-input>
        <el-input type="password" v-model="form.password" auto-complete="new-password" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="checkPass">
        <el-input type="password" style="position:fixed; bottom:-9999px"></el-input>
        <el-input type="password" v-model="form.checkPass" auto-complete="new-password" size="small" clearable ></el-input>
      </el-form-item>
      <el-form-item label="附件上传">
        <el-upload drag action="https://jsonplaceholder.typicode.com/posts/" multiple >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" size="small" @click="submitCheck">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>

export default {
  name: 'MyForm',
  data () {
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback()
      } else {
        if (this.form.checkPass !== '') {
          this.$refs.form.validateField('checkPass')
        }
        callback()
      }
    }
    let validatePass2 = (rule, value, callback) => {
      if (this.form.password !== '' && value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.form.password) {
        callback(new Error('两次输入密码不一致！'))
      } else {
        callback()
      }
    }
    return {
      pickerOptions: {
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
      datevalue: '',
      form: {
        userId: '',
        userName: '',
        phone: '',
        sex: '',
        password: '',
        email: '',
        checkPass: ''
      },
      rules2: {
        phone: [
          {required: true, message: '手机号不能为空'},
          {type: 'number', message: '手机号码必须为数字值', trigger: 'blur'},
          {pattern: /^[1][3,4,5,7,8][0-9]{9}$/, message: '格式错误', trigger: 'blur'}
        ],
        password: [
          {validator: validatePass, required: false, trigger: 'blur'},
          { pattern: /^([A-Z])(?=.*[a-z])(?=.*\d)[^]{7,23}$/, message: '首字母必须大写，并且包含大小写和数字，长度在 8 到 24 个字符', trigger: 'blur' }
        ],
        checkPass: [
          {validator: validatePass2, trigger: 'blur', required: false}
        ]
      }
    }
  },
  methods: {
    submitCheck () {
      console.log('ok')
    }
  }
}
</script>
<style scoped>

</style>

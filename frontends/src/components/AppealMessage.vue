<template ref="form" label-width="80px">
    <el-form>
        <el-form-item :label="form.type" >
            <el-select v-model='form.reasonValue' placeholder="请选择申诉原因">
                <el-option v-for='item in reasons' 
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>

        <el-form-item label="当前文章" v-model='form.obj'>
            {{form.obj}}
        </el-form-item>

        
        <el-form-item label="问题描述" prop="desc">
            <el-input type="textarea" v-model="form.content"></el-input>
        </el-form-item>

        
        <el-form-item>
            <p>上传图片</p>
            <el-upload
                ref="upload"
                class="upload-demo"
                :action="uploadUrl"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                multiple
                :auto-upload="false"
                list-type="picture-card"
                :limit="3"
                :data="form"
                :on-exceed="handleExceed"
                :on-success="handleSuccess"
                :on-error="handleError"
                :file-list="fileList">
            <i class="el-icon-plus"></i>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submit">提交</el-button>
            <el-button>取消</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
export default{
    name: 'AppealMessage',
    data:function(){
        return {
            reasons:[
                {label:"作者错误",value: 0},
                {label:"内容错误",value: 1}
            ],
            form:{
                type:'申诉原因',
                obj:12345678,
                resonValue:'',
                content:''
            },
            uploadUrl:'',
            file:'',
            fileList:[]
        }
    },
    methods: {
        submit:function(){
            this.uploadUrl="www.baidu.com"
            this.$refs.upload.submit();
            console.log(this.$refs.upload.data)
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        },
        handleExceed(files, fileList) {
            this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${ file.name }？`);
        },
        handleSuccess:function(response, file, fileList){
            this.$message.warning("上传成功！")
        },
        handleError:function(response, file, fileList){
            this.$message.warning("上传失败，请检查网络环境_(:з)∠)_")
        }
    }
}
</script>
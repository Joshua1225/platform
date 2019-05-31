<<template>
    <div>
        <el-row>
          <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="8">
            <div class="grid-content bg-purple">
                <router-view></router-view>
            </div>
            
            </el-col>
           
        </el-row>
        <el-row>
          <el-col :span="24"><div class="grid-content bg-purple"></div></el-col>
        </el-row>
    </div>
</template>>
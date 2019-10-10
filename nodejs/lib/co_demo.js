const co = require('co');
// 登录请求
let loginReq = new Promise((resolve,reject)=>{
    setTimeout(function () {
        resolve({success:true})
    },2000)
});

// 获取用户信息
let userInfoReq = new Promise((resolve,reject)=>{
    setTimeout(function () {
        resolve({nickName:'dounine'})
    },2000)
});

// 异步处理过程
loginReq.then(res=>{
  if(res.success){
    userInfoReq.then(userInfo=>{
      console.log('获取成功')
      // 如果还有信赖,需要继续写,还没有逻辑业务参与
    })
  }
})

// 同步处理过程
co(function *(){
  let loginInfo = yield loginReq;
  if(loginInfo.success){
    let userInfo = yield userInfoReq;
    console.log('获取成功')
  }
})

console.log('done');
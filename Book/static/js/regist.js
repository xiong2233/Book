/**
 * Created by Python on 2019/6/13.
 */
var css = {
    'color':'red'
}
$(function(){
    $("#email").blur(function(){
     $.ajax({
       url:"/emailajax",
       type:"get", //get为默认值,可以省略
       data:{'email':$(" input[ name='email' ] ").val()},
       dataType:'text',
       async:true, //true为默认值,可以省略
       success:function (data) {
           $("#emailajax").text(data)
           if(data=="成功"){
               $("#emailajax").css(css)
           }
       },
     });
   });
   $("#name").blur(function(){
     $.ajax({
       url:"/userajax",
       type:"get", //get为默认值,可以省略
       data:{'name':$(" input[ name='name' ] ").val()},
       dataType:'text',
       async:true, //true为默认值,可以省略
       success:function (data) {
           $("#userajax").text(data)
           if(data=="成功"){
               $("#userajax").css(css)
           }
       },
     });
   });
   $("#password").blur(function(){
     $.ajax({
       url:"/passwordajax",
       type:"get", //get为默认值,可以省略
       data:{'password':$(" input[ name='password' ] ").val()},
       dataType:'text',
       async:true, //true为默认值,可以省略
       success:function (data) {
           $("#pwdajax").text(data)
           if(data=="成功"){
               $("#pwdajax").css(css)
           }
       },
     });
   });
   $("#confirm_password").blur(function(){
     $.ajax({
       url:"/pwdajax",
       type:"get", //get为默认值,可以省略
       data:{
           'pwd':$(" input[ name='confirm_password' ] ").val(),
           'password':$(" input[ name='password' ] ").val()
       },
       dataType:'text',
       async:true, //true为默认值,可以省略
       success:function (data) {
           $("#apwdajax").text(data)
           if(data=="成功"){
               $("#apwdajax").css(css)
           }
       },
     });
   });
   // $("#submit").click(function() {
   //    if($('#checkbox').is(':checked')==false) {
   //        alert("请阅读政策条款")
   //    }
   // })
});
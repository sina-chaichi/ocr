login ={
init: function(){
  alert('Hello')

  function send_login(){
    console.log("login works!");
    $.ajax({
        url : '/users/user_login/',
        type : 'POST',
        data : {
          password : $('#pass').val(),
          email : $('#email').val(),
          csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
       },

     }).done(function(data){
         console.log(data);
         if (response_data['status'] == False){
           $('#message-div').html(data['message']);
         }
     }};

  $('#signin').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    send_login();
});

}
}

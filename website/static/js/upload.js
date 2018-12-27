upload ={
init: function(){
  alert('Hello');
  upload.eventHandler()
  },

  eventHandler: function(){
    $('#process').click(function(){
      upload.processOrder()
    }),
  },
  
  processOrder: function(){
    $.ajax({
      url: '/users/process/',
      type: 'POST',
      data:{
        csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
      },
    }).done(function(result){
      console.log(result)
    })
  },

}

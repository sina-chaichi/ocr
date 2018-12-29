show ={
init: function(){

  show.eventHandler()
  },

  eventHandler: function(){
    $('#process').click(function(){
      show.processOrder()
    }),

    $('.delete').click(function(){

      var el =$(this)
      show.deleteDocument(el)
    })

  },

  deleteDocument: function(el){
    id = el.attr('document-id')
    $.ajax({
      url: '/users/document-delete/',
      type: 'POST',
      data:{
        id:id,
        csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
      },
    }).done(function(result){
      console.log(result)
      if(result.status == true){
        console.log(el);
         el.parent().remove()

      }
    })
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

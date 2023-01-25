// event listener with jquery

$('DIV#add_item').click(function(){
    $('ul').append('<li>Item</li>');
})

$('div#remove_item').click(function(){
    $('li').remove();
})

$('div#clear_list').click(function(){
    $('ul').empty();
})

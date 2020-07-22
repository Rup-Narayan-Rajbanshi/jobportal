$(function(){
  $(document).on("click", ".pagination a", function(event){
    event.preventDefault()

    paginationContainer = $(this).closest(".ajax-paginate")
    if (paginationContainer){
      url = $(paginationContainer).data("url")

      if (url.indexOf("?")){
        url = url.slice(0, url.indexOf("?"))
      }    
      query = $(this).attr("href").substr($(this).attr("href").indexOf("?"))
      console.log(url+query)
      $(paginationContainer).load(url+query)
    }else{
      return true
    }

  });
})
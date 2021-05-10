
window.onload=function(){
    $("#spinner-modal").hide(); // I needed the loading icon to hide once the page loads
  }
  var onBeforeUnLoadEvent = false;
  window.onunload = window.onbeforeunload= function(){
  if(!onBeforeUnLoadEvent){ // for avoiding dual calls in browsers that support both events 
    onBeforeUnLoadEvent = true;
      $("#spinner-modal").show();
    }
  };
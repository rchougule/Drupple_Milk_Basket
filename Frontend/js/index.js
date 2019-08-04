
$(document).ready(function(){
//   $('.sidenav').sidenav();
//   $('ul.tabs').tabs();
//   $('.tooltipped').tooltip();
//   $('.fixed-action-btn').floatingActionButton();
//   $('.modal').modal();
//   $('.tap-target').tapTarget();
  $('select').formSelect();

  // $(".button-collapse").sideNav();
  // $('.tooltipped').tooltip({delay: 50});
  // window.dispatchEvent(new Event('resize'));
  // $('ul.tabs').tabs();
})

const serverURL = 'http://10.105.17.32:3003/';

var captionInterval;

window.onload = function(){

}

function showLoader(){
    $("#loaderDiv").css('display','block');
}

function hideLoader(){
    $("#loaderDiv").css('display','none');
}

function ajaxCallFunction(method, requestPath, headers, data, successAction, errorAction){
  
    showLoader();
    
    if(typeof(data) == 'object'){
      data = JSON.stringify(data);
    }
  
    const url = serverURL + requestPath;
  
    var settings = {
      "async": true,
      "crossDomain": true,
      url,
      method,
      headers,
      "mimeType": "multipart/form-data",
      data
    }
  
    $.ajax(settings).done(function (response) {
      hideLoader();
      if(response){
        successAction(response);
      }else{
        errorAction();
      }
    }).fail(function(err){
      hideLoader();
      const { responseJSON={} } = err;
      const { error:errorMessage='Request Sending Failed'} = responseJSON;
      errorAction(errorMessage);
    });
}

function inputCitySubmit(){
    $('#landing-page').css('display','none');
    $('#dashboard').css('display','block');
    dsahboardAPiCityData();
}

function dsahboardAPiCityData(){
 
    const errorFunction = (error)=>{
        console.log('Error occured',error);
    }

    const succesFunction = (response)=>{
        console.log('City Data Fetched Succesfully');

        const { statusCode,message='',data={} } = response;
        if(statusCode === 200){
            M.toast({html: message});

            const { descriptive, predictive }= data;
            
            // start filling the data
            $("#city-customer-result").val(descriptive.noOfUsers);
            $("#city-average-order-result").val(descriptive.avgOrdersPerDay);
            $("#city-average-value-result").val(descriptive.avgValuePerDay);

            $("#city-mean-order-cost-result").val(descriptive.meanOrderCost);
            $("#city-warehouse-result").val(descriptive.noOfWarehouses);
            $("#city-max-distance-result").val(descriptive.maxDistanceFromWarehouse);

            $("#city-lat-long-warehouse-result").val(descriptive.warehouseLocation.lat+", "+descriptive.warehouseLocation.long);

            // graph value

            
        }

    }

    const headers = {
        "User-Agent": "PostmanRuntime/7.15.0",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Postman-Token": "f75178af-561c-4dfd-ae72-9eb490407a5a,1a896093-56d5-41d5-a462-e1ac8815ea50",
        "Host": "10.105.17.32:3003",
        "accept-encoding": "gzip, deflate",
        "content-length": "168",
        "Connection": "keep-alive",
        "cache-control": "no-cache"
    };

    ajaxCallFunction('GET','city-insights',headers,{},succesFunction,errorFunction);
}









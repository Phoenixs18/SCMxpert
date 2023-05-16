async function createShipment(){
  
    let Invoice_no = document.querySelector("#inv_no").value
    let container_no = document.querySelector("#cont_no").value
    let shipmentDescription = document.querySelector("#ship_des").value                
    let description_pattern = new RegExp("[A-Za-z0-9? ,_-]+$")
    if (description_pattern.test(shipmentDescription)){
        var shipment_description = await shipmentDescription
    } else {
        shipment_description = ''
        alert ("no special character in shipment Description")
    }
    let route_details = document.querySelector("#route_det ")
    var route_values = route_details.options[route_details.selectedIndex].value;
    let goods_type = document.querySelector("#goods_type ")
    var goods_values = goods_type.options[goods_type.selectedIndex].value;
    let device = document.querySelector("#dev").value
    let expected_delivery_date = document.querySelector("#exp_del_d").value
    let PONumber = document.querySelector("#po_no").value
    if (PONumber.toString().length == 6){
        var PO_number = await PONumber
    }
    else {
        PO_number = null
        alert("Type Six digit for the po_number")
    }
    let delivery_no = document.querySelector("#del_no").value      
    let NDC_no = document.querySelector("#ndc_no").value
    let batch_id = document.querySelector("#batch_id").value
    let Serial_no_of_goods = document.querySelector("#s_no").value                

    $.ajax({
    
    url:"http://"+window.location.hostname+":8000/shipment",
    type:"POST",
    headers:{"Authorization": 'Bearer ' + localStorage.getItem('access_token'),
},
    contentType:"application/json",
    data:JSON.stringify({
       
        invoice_no:Invoice_no,
        container_no:container_no,
        shipment_description:shipment_description,
        route_details:route_values,
        goods_type:goods_values,
        device:device,
        expected_delivery_date:expected_delivery_date,
        PO_number:PO_number,
        delivery_no:delivery_no,
        NDC_no:NDC_no,
        batch_id:batch_id,
        serial_no_of_goods:Serial_no_of_goods,
    }),
    success:function(data) {

     window.location.href = "http://"+window.location.hostname+":5500/../../Frontend/templates/dashboard.html";
        return(data)
    },
    error:function(xhr, ajaxOptions, thrownError){
        alert("fill all details")
    }
    })
}
function logout(){
    localStorage.removeItem('access_token')
    window.location.href = "../../../Frontend/login.html"
  }
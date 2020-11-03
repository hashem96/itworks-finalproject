var priceArr = document.getElementsByName("productPrice")
    var tot=0;
    for(var i=0;i<priceArr.length;i++){
        if(parseInt(priceArr[i].textContent))
            tot += parseFloat(priceArr[i].textContent);
    }
    document.getElementById("total").textContent = "Total : " + tot + " " + "$";

    console.log(tot)
//Post purchases to database logic //

const confirmButton = document.getElementById("confirmButton")
const handleConfirm = () => {
    const xhr = new XMLHttpRequest()
    const data = new FormData()
    console.log(tot)
    data.append("total_price" ,tot)
    xhr.open("POST", "/purchases")
    xhr.send(data)
    window.location.replace = "/confirm"
    
  }
  

  confirmButton.addEventListener('click', handleConfirm)
